"""Threaded synchronous websocket connection with a single reader."""

import queue, random, threading, time, uuid
from contextlib import ExitStack
from concurrent.futures import Future, TimeoutError
from typing import Any
from ..codec import decode_frame, encode_message
from ..config import WebSocketConfig
from ..errors import (
    WebSocketAuthenticationError,
    WebSocketBackpressureError,
    WebSocketConnectionError,
    WebSocketConnectionStateError,
    WebSocketRequestError,
)
from .base import apply_unsubscribe, subscription_key


class SyncConnection:
    def __init__(self, url, token_provider, config=None):
        self.url, self.provider, self.config = (
            url,
            token_provider,
            config or WebSocketConfig(),
        )
        self._state = "DISCONNECTED"
        self._socket: Any = None
        self._socket_context: Any = None
        self._reader = None
        self.resource: Any = None
        self._queue = queue.Queue(self.config.incoming_queue_size)
        self._pending = {}
        self._lock = threading.Lock()
        self._closed = False
        self._active = {}
        self._keepalive = None
        self._keepalive_stop = threading.Event()
        self._recovering = False
        self._terminal = None
        self._terminal_reported = False

    @property
    def state(self):
        """Current read-only connection state."""
        return self._state

    def _id(self, prefix):
        return f"{prefix}-{uuid.uuid4()}"

    def _open_socket(self, connect):
        """Enter and retain the context that owns the current socket."""
        socket_context = ExitStack()
        try:
            socket = socket_context.enter_context(
                connect(
                    self.url,
                    open_timeout=self.config.connect_timeout,
                    close_timeout=self.config.close_timeout,
                    max_size=self.config.max_message_size,
                    ping_interval=self.config.ping_interval,
                    ping_timeout=self.config.pong_timeout,
                )
            )
        except Exception:
            socket_context.close()
            raise
        self._socket_context = socket_context
        self._socket = socket
        return socket

    def _close_socket_context(self):
        """Close the active socket through its owning context manager."""
        socket_context, self._socket_context = self._socket_context, None
        self._socket = None
        if socket_context is not None:
            socket_context.close()

    def connect(self):
        try:
            from websockets.sync.client import connect

            self._state = "CONNECTING"
            self._open_socket(connect)
            self._state = "AUTHENTICATING"
            self._reader = threading.Thread(target=self._read_loop, daemon=True)
            self._reader.start()
            ident = self._id("auth")
            self._auth_id = ident
            future = Future()
            with self._lock:
                self._pending[ident] = future
            self._socket.send(
                encode_message(
                    {
                        "type": "request",
                        "id": ident,
                        "payload": {
                            "method": "POST",
                            "path": "/auth",
                            "body": {"token": self.provider.get_token()},
                        },
                    }
                )
            )
            result = future.result(timeout=self.config.auth_timeout)
            if result.get("payload", {}).get("action") != "authSuccess":
                raise WebSocketAuthenticationError(
                    "WebSocket authentication was rejected"
                )
            self._state = "READY"
            self._keepalive = threading.Thread(target=self._keepalive_loop, daemon=True)
            self._keepalive.start()
            return self
        except TimeoutError as exc:
            self.close()
            raise WebSocketAuthenticationError(
                "WebSocket authentication timed out"
            ) from exc
        except (WebSocketAuthenticationError, WebSocketConnectionError):
            self.close()
            raise
        except WebSocketRequestError as exc:
            self.close()
            raise WebSocketAuthenticationError(
                "WebSocket authentication was rejected"
            ) from exc
        except Exception as exc:
            self.close()
            raise WebSocketConnectionError(
                "Unable to connect or authenticate websocket"
            ) from exc

    def _read_loop(self):
        while not self._closed:
            try:
                frame = self._socket.recv(timeout=1)
                if frame is None:
                    continue
                for msg in decode_frame(frame):
                    if not hasattr(msg, "original"):
                        msg = msg.model_dump(by_alias=True, exclude_none=True)
                    self._dispatch(msg)
            except TimeoutError:
                continue
            except Exception as exc:
                if self._closed:
                    return
                if self.config.reconnect and (
                    isinstance(exc, (OSError, ConnectionError, TimeoutError))
                    or exc.__class__.__name__.startswith("ConnectionClosed")
                ):
                    try:
                        self._reconnect()
                    except Exception as reconnect_error:
                        self._state = "FAILED"
                        self._closed = True
                        self._terminal = reconnect_error
                        self._put(reconnect_error)
                        return
                else:
                    self._state = "FAILED"
                    self._closed = True
                    self._terminal = exc
                    self._put(exc)
                    return

    def _dispatch(self, msg):
        if hasattr(msg, "original"):
            self._put(msg)
            return
        payload = msg.get("payload", {})
        ident = msg.get("id") or payload.get("id")
        action = payload.get("action")
        if action == "refreshAuth":
            threading.Thread(target=self._refresh_auth, daemon=True).start()
            self._put(msg)
            return
        if action in {"authRequired", "authTimeout"}:
            raise WebSocketAuthenticationError(str(payload.get("error", action)))
        if action == "authExpired":
            if not self.config.reconnect:
                raise WebSocketAuthenticationError("WebSocket session expired")
            raise ConnectionError("WebSocket session expired")
        with self._lock:
            future = self._pending.pop(ident, None) if ident else None
            if not future and action == "authSuccess":
                future = self._pending.pop(getattr(self, "_auth_id", None), None)
        if action == "authSuccess" and self._recovering:
            self._recovering = False
            self._state = "READY"
            if self.config.replay_subscriptions:
                for message in self._active.values():
                    self._socket.send(encode_message(message))
            self._keepalive = threading.Thread(target=self._keepalive_loop, daemon=True)
            self._keepalive.start()
        if future:
            if payload.get("error") or payload.get("status", 200) >= 400:
                if ident == getattr(self, "_auth_id", None):
                    future.set_exception(
                        WebSocketAuthenticationError(
                            "WebSocket authentication was rejected"
                        )
                    )
                    raise WebSocketAuthenticationError(
                        "WebSocket authentication was rejected"
                    )
                else:
                    future.set_exception(
                        WebSocketRequestError(
                            str(
                                payload.get(
                                    "message", payload.get("error", "request failed")
                                )
                            ),
                            status=payload.get("status"),
                            code=payload.get("code"),
                            request_id=ident,
                        )
                    )
            elif action == "error":
                future.set_exception(
                    WebSocketRequestError(
                        str(payload.get("error", "request failed")),
                        status=payload.get("status"),
                        code=payload.get("code"),
                        request_id=ident,
                    )
                )
            elif not future.done():
                future.set_result(msg)
        else:
            self._put(msg)

    def _refresh_auth(self):
        try:
            ident = self._id("auth")
            self._auth_id = ident
            future = Future()
            with self._lock:
                self._pending[ident] = future
            self._socket.send(
                encode_message(
                    {
                        "type": "request",
                        "id": ident,
                        "payload": {
                            "method": "POST",
                            "path": "/auth",
                            "body": {"token": self.provider.get_token()},
                        },
                    }
                )
            )
            result = future.result(timeout=self.config.auth_timeout)
            if result.get("payload", {}).get("action") != "authSuccess":
                raise WebSocketAuthenticationError(
                    "WebSocket token refresh was rejected"
                )
        except Exception as exc:
            self._terminal = exc
            self._state = "FAILED"
            self._closed = True
            self._put(exc)
            try:
                self._socket.close()
            except Exception:
                pass

    def _reconnect(self):
        from websockets.sync.client import connect

        self._state = "RECONNECTING"
        # The failed session's context must be exited before a new session is
        # entered. The reader thread then continues reading from the new socket.
        self._close_socket_context()
        for attempt in range(8):
            delay = min(
                self.config.reconnect_max_delay,
                self.config.reconnect_initial_delay * (2**attempt),
            )
            time.sleep(
                delay
                * random.uniform(
                    1 - self.config.reconnect_jitter, 1 + self.config.reconnect_jitter
                )
            )
            try:
                self._open_socket(connect)
                ident = self._id("auth")
                self._auth_id = ident
                self._recovering = True
                self._state = "AUTHENTICATING"
                with self._lock:
                    self._pending[ident] = Future()
                self._socket.send(
                    encode_message(
                        {
                            "type": "request",
                            "id": ident,
                            "payload": {
                                "method": "POST",
                                "path": "/auth",
                                "body": {"token": self.provider.get_token()},
                            },
                        }
                    )
                )
                return
            except WebSocketAuthenticationError:
                self._state = "FAILED"
                self._close_socket_context()
                raise
            except Exception:
                self._close_socket_context()
                continue
        raise WebSocketConnectionError("WebSocket reconnect attempts exhausted")

    def _keepalive_loop(self):
        while not self._closed and self._state == "READY":
            if self._keepalive_stop.wait(self.config.ping_interval):
                return
            if self._closed or self.state != "READY":
                return
            ident = self._id("ping")
            future = Future()
            with self._lock:
                self._pending[ident] = future
            try:
                self._socket.send(encode_message({"type": "ping", "id": ident}))
                future.result(timeout=self.config.pong_timeout)
            except Exception:
                try:
                    self._socket.close()
                except Exception:
                    pass
                return

    def _put(self, item):
        try:
            self._queue.put_nowait(item)
        except queue.Full:
            self._closed = True
            self._state = "FAILED"
            self._terminal = WebSocketBackpressureError(
                "Incoming websocket queue is full; drain events faster or increase incoming_queue_size"
            )
            try:
                self._socket.close()
            finally:
                try:
                    self._queue.put_nowait(self._terminal)
                except queue.Full:
                    pass

    def _require_ready(self):
        if self.state != "READY":
            raise WebSocketConnectionStateError(
                "WebSocket must be authenticated and READY before this operation"
            )

    def request(self, method, path, *, query=None, body=None, timeout=None):
        payload = {"method": method, "path": path}
        if query is not None:
            payload["query"] = query
        if body is not None:
            payload["body"] = body
        return self.exchange(
            {"type": "request", "id": self._id("request"), "payload": payload},
            timeout=timeout,
        )

    def send_message(self, message):
        self._require_ready()
        key = subscription_key(message)
        if message.get("type") == "subscribe" and key in self._active:
            return message.get("id")
        self._socket.send(encode_message(message))
        if message.get("type") == "subscribe":
            self._active[key] = dict(message)
        elif message.get("type") == "unsubscribe":
            apply_unsubscribe(self._active, message)
        return message.get("id")

    def exchange(self, message, *, timeout=None):
        self._require_ready()
        ident = message.get("id") or self._id("request")
        message["id"] = ident
        future = Future()
        with self._lock:
            self._pending[ident] = future
        self._socket.send(encode_message(message))
        try:
            return future.result(timeout=timeout or self.config.request_timeout)
        finally:
            with self._lock:
                self._pending.pop(ident, None)

    def subscribe(self, payload, *, data_type="quotes", symbol_type=None):
        resource: Any = getattr(self, "resource", None)
        if getattr(resource, "protocol", "") == "chart":
            return resource.subscribe(
                self, payload, data_type=data_type, symbol_type=symbol_type
            )
        if getattr(resource, "protocol", "") == "market":
            return resource.subscribe(self, payload)
        ident = self._id("subscribe")
        self.send_message({"type": "subscribe", "id": ident, "payload": payload})
        return ident

    def unsubscribe(self, payload):
        resource: Any = getattr(self, "resource", None)
        if getattr(resource, "protocol", "") == "chart":
            return resource.unsubscribe(self, payload)
        if getattr(resource, "protocol", "") == "market":
            return resource.unsubscribe(self, payload)
        ident = self._id("unsubscribe")
        self.send_message({"type": "unsubscribe", "id": ident, "payload": payload})
        return ident

    def __iter__(self):
        return self

    def __getattr__(self, name):
        resource = self.__dict__.get("resource")
        method = getattr(resource, name, None) if resource is not None else None
        if method is not None and callable(method):
            return lambda *args, **kwargs: method(self, *args, **kwargs)
        raise AttributeError(name)

    def __next__(self):
        if self._queue.empty() and self._terminal and not self._terminal_reported:
            self._terminal_reported = True
            raise self._terminal
        if self._closed and self._queue.empty():
            raise StopIteration
        item = self._queue.get()
        if isinstance(item, Exception):
            self._terminal_reported = True
            raise item
        return item

    def close(self):
        if self._state == "CLOSED":
            return
        self._closed = True
        self._keepalive_stop.set()
        self._state = "CLOSING"
        with self._lock:
            pending = list(self._pending.values())
            self._pending.clear()
        for future in pending:
            if not future.done():
                future.set_exception(
                    WebSocketConnectionError("WebSocket connection was closed")
                )
        try:
            self._close_socket_context()
        except Exception:
            pass
        if self._reader and self._reader is not threading.current_thread():
            self._reader.join(timeout=self.config.close_timeout)
        if self._keepalive and self._keepalive is not threading.current_thread():
            self._keepalive.join(timeout=self.config.close_timeout)
        self._state = "CLOSED"

    def __enter__(self):
        return self.connect()

    def __exit__(self, *_):
        self.close()
