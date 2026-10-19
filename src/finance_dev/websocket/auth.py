"""WebSocket access-token providers."""

import asyncio
import inspect
import threading
import time
from typing import Callable, Protocol
import httpx
from .errors import WebSocketAuthenticationError


class TokenProvider(Protocol):
    def get_token(self) -> str: ...
class AsyncTokenProvider(Protocol):
    async def get_token(self) -> str: ...


class StaticTokenProvider:
    def __init__(self, token: str):
        self.token = token

    def get_token(self) -> str:
        return self.token


class CallbackTokenProvider:
    def __init__(self, callback: Callable[[], str]):
        self.callback = callback

    def get_token(self) -> str:
        return self.callback()


class AsyncCallbackTokenProvider:
    def __init__(self, callback):
        self.callback = callback

    async def get_token(self) -> str:
        result = self.callback()
        return await result if inspect.isawaitable(result) else result


class ClientCredentialsTokenProvider:
    def __init__(self, token_url: str, client_id: str, client_secret: str):
        self.token_url, self.client_id, self.client_secret = (
            token_url,
            client_id,
            client_secret,
        )
        self._lock = threading.Lock()
        self._token: str | None = None
        self._expires = 0.0

    def get_token(self) -> str:
        with self._lock:
            if self._token and time.monotonic() < self._expires - 30:
                return self._token
            try:
                response = httpx.post(
                    self.token_url,
                    data={
                        "grant_type": "client_credentials",
                        "client_id": self.client_id,
                        "client_secret": self.client_secret,
                    },
                    timeout=15,
                )
                data = response.json()
                if response.is_error:
                    raise WebSocketAuthenticationError(
                        "Client credentials were rejected. For partner/business clients, supply a token obtained through Authorization Code or PKCE."
                    )
                token: str = data["access_token"]
                self._token = token
                self._expires = time.monotonic() + float(data.get("expires_in", 3600))
                return token
            except WebSocketAuthenticationError:
                raise
            except Exception as exc:
                raise WebSocketAuthenticationError(
                    "Unable to obtain websocket access token"
                ) from exc


class AsyncClientCredentialsTokenProvider:
    def __init__(self, token_url, client_id, client_secret):
        self.token_url, self.client_id, self.client_secret = (
            token_url,
            client_id,
            client_secret,
        )
        self._lock = asyncio.Lock()
        self._token = None
        self._expires = 0.0

    async def get_token(self):
        async with self._lock:
            if self._token and time.monotonic() < self._expires - 30:
                return self._token
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.post(
                        self.token_url,
                        data={
                            "grant_type": "client_credentials",
                            "client_id": self.client_id,
                            "client_secret": self.client_secret,
                        },
                        timeout=15,
                    )
                data = response.json()
                if response.is_error:
                    raise WebSocketAuthenticationError(
                        "Client credentials were rejected. For partner/business clients, supply a token obtained through Authorization Code or PKCE."
                    )
                self._token = data["access_token"]
                self._expires = time.monotonic() + float(data.get("expires_in", 3600))
                return self._token
            except WebSocketAuthenticationError:
                raise
            except Exception as exc:
                raise WebSocketAuthenticationError(
                    "Unable to obtain websocket access token"
                ) from exc
