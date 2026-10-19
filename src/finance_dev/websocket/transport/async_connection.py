"""Asyncio websocket connection with a single reader task."""

import asyncio
import inspect
import random
import uuid
from typing import Any
from ..auth import AsyncTokenProvider, TokenProvider, StaticTokenProvider
from ..codec import decode_frame, encode_message
from ..config import WebSocketConfig
from ..errors import (
    WebSocketAuthenticationError,
    WebSocketBackpressureError,
    WebSocketConnectionError,
    WebSocketConnectionStateError,
    WebSocketProtocolError,
    WebSocketRequestError,
)
from .base import apply_unsubscribe, subscription_key


class _SessionExpired(ConnectionError):
    """Internal signal to reconnect after server-side token expiry."""


class AsyncConnection:
    def __init__(
        self, url: str, token_provider: Any, config: WebSocketConfig | None = None
    ):
        self.url, self.provider, self.config = (
            url,
            token_provider,
            config or WebSocketConfig(),
        )
        self._state = "DISCONNECTED"
        self._socket: Any = None
        self._reader: asyncio.Task | None = None
        self.resource: Any = None
        self._pending: dict[str, asyncio.Future] = {}
        self._events: asyncio.Queue[Any] = asyncio.Queue(
            self.config.incoming_queue_size
        )
        self._closed = False
        self._auth_id: str | None = None
        self._active: dict[str, dict[str, Any]] = {}
        self._keepalive: asyncio.Task | None = None
        self._terminal: Exception | None = None
        self._terminal_reported = False

    async def connect(self):
        try:
            from websockets.asyncio.client import connect

            self._state = "CONNECTING"
            self._socket = await asyncio.wait_for(
                connect(
                    self.url,
                    open_timeout=self.config.connect_timeout,
                    close_timeout=self.config.close_timeout,
                    max_size=self.config.max_message_size,
                    ping_interval=self.config.ping_interval,
                    ping_timeout=self.config.pong_timeout,
                ),
                self.config.connect_timeout,
            )
            self._state = "AUTHENTICATING"
            self._reader = asyncio.create_task(self._read_loop())
            self._auth_id = self._id("auth")
            auth_future = self._pending_future(self._auth_id)
            await self._send(
                {
                    "type": "request",
                    "id": self._auth_id,
                    "payload": {
                        "method": "POST",
                        "path": "/auth",
                        "body": {"token": await self._get_token()},
                    },
                }
            )
            result = await asyncio.wait_for(auth_future, self.config.auth_timeout)
            if result.get("payload", {}).get("action") != "authSuccess":
                raise WebSocketAuthenticationError(
                    "WebSocket authentication was rejected"
                )
            self._state = "READY"
            self._keepalive = asyncio.create_task(self._keepalive_loop())
            return self
        except asyncio.TimeoutError as exc:
            await self.close()
            raise WebSocketAuthenticationError(
                "WebSocket authentication timed out"
            ) from exc
        except (WebSocketAuthenticationError, WebSocketConnectionError):
            await self.close()
            raise
        except WebSocketRequestError as exc:
            await self.close()
            raise WebSocketAuthenticationError(
                "WebSocket authentication was rejected"
            ) from exc
        except Exception as exc:
            await self.close()
            raise WebSocketConnectionError(
                "Unable to connect or authenticate websocket"
            ) from exc

    @property
    def state(self):
        """Current read-only connection state."""
        return self._state

    def _id(self, prefix):
        return f"{prefix}-{uuid.uuid4()}"

    async def _get_token(self):
        value = self.provider.get_token()
        return await value if inspect.isawaitable(value) else value

    def _pending_future(self, request_id):
        future = asyncio.get_running_loop().create_future()
        self._pending[request_id] = future
        return future

    async def _send(self, value):
        await self._socket.send(encode_message(value))

    async def send_message(self, message):
        self._require_ready()
        key = subscription_key(message)
        if message.get("type") == "subscribe" and key in self._active:
            return message.get("id")
        await self._send(message)
        if message.get("type") == "subscribe":
            self._active[key] = dict(message)
        elif message.get("type") == "unsubscribe":
            apply_unsubscribe(self._active, message)
        return message.get("id")

    async def exchange(self, message, *, timeout=None):
        self._require_ready()
        ident = message.get("id") or self._id("request")
        message["id"] = ident
        future = self._pending_future(ident)
        await self._send(message)
        try:
            return await asyncio.wait_for(
                future, timeout or self.config.request_timeout
            )
        finally:
            self._pending.pop(ident, None)

    async def _read_loop(self):
        try:
            async for frame in self._socket:
                for message in decode_frame(frame):
                    if hasattr(message, "original"):
                        await self._put(message)
                        continue
                    wire_message = message
                    message = message.model_dump(by_alias=True, exclude_none=True)
                    payload = message.get("payload", {})
                    ident = message.get("id") or payload.get("id")
                    action = payload.get("action")
                    if action == "authExpired":
                        raise _SessionExpired("WebSocket session expired")
                    if action in {"authRequired", "authTimeout"}:
                        raise WebSocketAuthenticationError(
                            str(payload.get("error", action))
                        )
                    if action == "refreshAuth":
                        asyncio.create_task(self._refresh_auth())
                        continue
                    if ident in self._pending and (
                        message.get("type") in {"response", "subscribed", "pong"}
                        or action in {"authSuccess", "error"}
                    ):
                        future = self._pending.pop(ident)
                        if payload.get("error") or payload.get("status", 200) >= 400:
                            if ident == self._auth_id:
                                future.set_exception(
                                    WebSocketAuthenticationError(
                                        "WebSocket authentication was rejected"
                                    )
                                )
                            else:
                                future.set_exception(
                                    WebSocketRequestError(
                                        str(
                                            payload.get(
                                                "message",
                                                payload.get("error", "request failed"),
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
                            future.set_result(message)
                    elif action == "authSuccess" and self._auth_id in self._pending:
                        self._pending.pop(self._auth_id).set_result(message)
                    else:
                        await self._put(wire_message)
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            if self._closed:
                return
            transient = isinstance(
                exc, (OSError, ConnectionError, TimeoutError)
            ) or exc.__class__.__name__.startswith("ConnectionClosed")
            if (
                self.config.reconnect
                and transient
                and not isinstance(
                    exc,
                    (
                        WebSocketProtocolError,
                        WebSocketAuthenticationError,
                        WebSocketRequestError,
                        WebSocketBackpressureError,
                    ),
                )
            ):
                try:
                    await self._recover()
                except Exception as reconnect_error:
                    self._state = "FAILED"
                    self._terminal = reconnect_error
                    await self._put_error(reconnect_error)
            else:
                self._state = "FAILED"
                self._terminal = exc
                await self._put_error(exc)

    async def _refresh_auth(self):
        try:
            token = await self._get_token()
            ident = self._id("auth")
            future = self._pending_future(ident)
            await self._send(
                {
                    "type": "request",
                    "id": ident,
                    "payload": {
                        "method": "POST",
                        "path": "/auth",
                        "body": {"token": token},
                    },
                }
            )
            result = await asyncio.wait_for(future, self.config.auth_timeout)
            if result.get("payload", {}).get("action") != "authSuccess":
                raise WebSocketAuthenticationError(
                    "WebSocket token refresh was rejected"
                )
        except Exception as exc:
            await self._put_error(exc)
            await self.close()

    async def _recover(self):
        self._state = "RECONNECTING"
        if self._keepalive:
            self._keepalive.cancel()
        if self._socket:
            try:
                await self._socket.close()
            except Exception:
                pass
        attempt = 0
        while not self._closed:
            delay = min(
                self.config.reconnect_max_delay,
                self.config.reconnect_initial_delay * (2**attempt),
            )
            await asyncio.sleep(
                delay
                * random.uniform(
                    1 - self.config.reconnect_jitter, 1 + self.config.reconnect_jitter
                )
            )
            try:
                from websockets.asyncio.client import connect

                self._socket = await asyncio.wait_for(
                    connect(
                        self.url,
                        open_timeout=self.config.connect_timeout,
                        close_timeout=self.config.close_timeout,
                        max_size=self.config.max_message_size,
                        ping_interval=self.config.ping_interval,
                        ping_timeout=self.config.pong_timeout,
                    ),
                    self.config.connect_timeout,
                )
                self._state = "AUTHENTICATING"
                self._auth_id = self._id("auth")
                future = self._pending_future(self._auth_id)
                self._reader = asyncio.create_task(self._read_loop())
                token = await self._get_token()
                await self._send(
                    {
                        "type": "request",
                        "id": self._auth_id,
                        "payload": {
                            "method": "POST",
                            "path": "/auth",
                            "body": {"token": token},
                        },
                    }
                )
                result = await asyncio.wait_for(future, self.config.auth_timeout)
                if result.get("payload", {}).get("action") != "authSuccess":
                    raise WebSocketAuthenticationError(
                        "WebSocket authentication was rejected"
                    )
                self._state = "READY"
                if self.config.replay_subscriptions:
                    for message in self._active.values():
                        await self._send(message)
                self._keepalive = asyncio.create_task(self._keepalive_loop())
                return
            except WebSocketAuthenticationError:
                self._state = "FAILED"
                raise
            except WebSocketRequestError as exc:
                self._state = "FAILED"
                raise WebSocketAuthenticationError(
                    "WebSocket authentication was rejected"
                ) from exc
            except Exception as exc:
                attempt += 1
                if attempt >= 8:
                    self._state = "FAILED"
                    raise WebSocketConnectionError(
                        "WebSocket reconnect attempts exhausted"
                    ) from exc

    async def _keepalive_loop(self):
        try:
            while not self._closed and self._state == "READY":
                await asyncio.sleep(self.config.ping_interval)
                ident = self._id("ping")
                future = self._pending_future(ident)
                await self._send({"type": "ping", "id": ident})
                await asyncio.wait_for(future, self.config.pong_timeout)
        except asyncio.CancelledError:
            pass
        except Exception:
            if self._socket and not self._closed:
                try:
                    await self._socket.close()
                except Exception:
                    pass

    async def _put(self, event):
        try:
            self._events.put_nowait(event)
        except asyncio.QueueFull:
            self._terminal = WebSocketBackpressureError(
                "Incoming websocket queue is full; drain events faster or increase incoming_queue_size"
            )
            self._closed = True
            self._state = "FAILED"
            try:
                await self._socket.close()
            finally:
                await self._put_error(self._terminal)

    async def _put_error(self, error):
        self._terminal = error
        self._closed = True
        try:
            self._events.put_nowait(error)
        except asyncio.QueueFull:
            pass

    async def request(self, method, path, *, query=None, body=None, timeout=None):
        payload = {"method": method, "path": path}
        if query is not None:
            payload["query"] = query
        if body is not None:
            payload["body"] = body
        return await self.exchange(
            {"type": "request", "id": self._id("request"), "payload": payload},
            timeout=timeout,
        )

    def _require_ready(self):
        if self.state != "READY":
            raise WebSocketConnectionStateError(
                "WebSocket must be authenticated and READY before this operation"
            )

    async def subscribe(self, payload, *, data_type="quotes", symbol_type=None):
        resource: Any = getattr(self, "resource", None)
        if getattr(resource, "protocol", "") == "chart":
            return await resource.subscribe_async(
                self, payload, data_type=data_type, symbol_type=symbol_type
            )
        if getattr(resource, "protocol", "") == "market":
            return await resource.subscribe_async(self, payload)
        ident = self._id("subscribe")
        await self.send_message({"type": "subscribe", "id": ident, "payload": payload})
        return ident

    async def unsubscribe(self, payload):
        resource: Any = getattr(self, "resource", None)
        if getattr(resource, "protocol", "") == "chart":
            return await resource.unsubscribe_async(self, payload)
        if getattr(resource, "protocol", "") == "market":
            return await resource.unsubscribe_async(self, payload)
        ident = self._id("unsubscribe")
        await self.send_message(
            {"type": "unsubscribe", "id": ident, "payload": payload}
        )
        return ident

    async def get_event(self):
        item = await self._events.get()
        if isinstance(item, Exception):
            self._terminal_reported = True
            raise item
        return item

    def __aiter__(self):
        return self

    def __getattr__(self, name):
        resource = self.__dict__.get("resource")
        method: Any = getattr(resource, name, None) if resource is not None else None
        if method is not None and callable(method):

            async def delegated(*args, **kwargs):
                result: Any = method(self, *args, **kwargs)
                return await result if inspect.isawaitable(result) else result

            return delegated
        raise AttributeError(name)

    async def __anext__(self):
        if self._closed and self._events.empty():
            if self._terminal and not self._terminal_reported:
                self._terminal_reported = True
                raise self._terminal
            raise StopAsyncIteration
        return await self.get_event()

    async def close(self):
        if self._closed and self._state == "CLOSED":
            return
        self._closed = True
        self._state = "CLOSING"
        for future in self._pending.values():
            if not future.done():
                future.cancel()
        self._pending.clear()
        if self._keepalive:
            self._keepalive.cancel()
            if self._keepalive is not asyncio.current_task():
                try:
                    await self._keepalive
                except BaseException:
                    pass
        if self._socket:
            try:
                await asyncio.wait_for(self._socket.close(), self.config.close_timeout)
            except Exception:
                pass
        if self._reader and self._reader is not asyncio.current_task():
            self._reader.cancel()
            try:
                await self._reader
            except BaseException:
                pass
        self._state = "CLOSED"

    async def __aenter__(self):
        return await self.connect()

    async def __aexit__(self, *_):
        await self.close()
