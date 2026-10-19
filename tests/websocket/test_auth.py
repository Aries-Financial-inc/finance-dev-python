# Hand-maintained WebSocket tests; preserved by Speakeasy persistent edits.
import asyncio
import threading

import pytest
from finance_dev.websocket.auth import (
    AsyncCallbackTokenProvider, CallbackTokenProvider,
    ClientCredentialsTokenProvider, StaticTokenProvider,
)

def test_static_and_callback_token_providers():
    assert StaticTokenProvider("abc").get_token() == "abc"
    assert CallbackTokenProvider(lambda: "next").get_token() == "next"

@pytest.mark.asyncio
async def test_async_callback_provider_accepts_async_callbacks():
    provider = AsyncCallbackTokenProvider(lambda: asyncio.sleep(0, result="rotated"))
    assert await provider.get_token() == "rotated"

def test_client_credentials_refresh_is_serialized(monkeypatch):
    from types import SimpleNamespace
    calls = []
    def post(*args, **kwargs):
        calls.append(kwargs)
        return SimpleNamespace(is_error=False, json=lambda: {"access_token":"cached-token","expires_in":3600})
    monkeypatch.setattr("finance_dev.websocket.auth.httpx.post", post)
    provider = ClientCredentialsTokenProvider("https://tokens.invalid", "client", "secret")
    results = []
    threads = [threading.Thread(target=lambda: results.append(provider.get_token())) for _ in range(8)]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    assert results == ["cached-token"] * 8
    assert len(calls) == 1
    assert "secret" not in repr(provider)
