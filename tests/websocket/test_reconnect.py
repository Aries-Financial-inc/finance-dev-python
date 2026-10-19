# Hand-maintained WebSocket tests; preserved by Speakeasy persistent edits.
import asyncio
import threading

import pytest
from finance_dev.websocket.auth import StaticTokenProvider
from finance_dev.websocket.config import WebSocketConfig
from finance_dev.websocket.transport.async_connection import AsyncConnection
from finance_dev.websocket.transport.sync_connection import SyncConnection

@pytest.mark.asyncio
async def test_reauthenticates_and_replays_active_subscriptions(reconnecting_ws_server):
    url, received = reconnecting_ws_server
    config = WebSocketConfig(ping_interval=0.05, pong_timeout=0.2,
        reconnect_initial_delay=0.01, reconnect_max_delay=0.02, reconnect_jitter=0)
    async with AsyncConnection(url, StaticTokenProvider("token"), config) as stream:
        await stream.subscribe({"topic":"watchlist"})
        for _ in range(100):
            if any(number > 1 and message.get("type") == "subscribe" for number, message in received): break
            await asyncio.sleep(0.01)
        assert stream.state == "READY"
        assert sum(number > 1 and message.get("type") == "subscribe" for number, message in received) == 1

@pytest.mark.asyncio
async def test_sync_connection_reauthenticates_and_replays(reconnecting_ws_server):
    url, received = reconnecting_ws_server
    config = WebSocketConfig(ping_interval=0.05, pong_timeout=0.2,
        reconnect_initial_delay=0.01, reconnect_max_delay=0.02, reconnect_jitter=0)
    def run():
        with SyncConnection(url, StaticTokenProvider("token"), config) as stream:
            stream.subscribe({"topic":"watchlist"})
            for _ in range(100):
                if any(number > 1 and message.get("type") == "subscribe" for number, message in received): break
                threading.Event().wait(0.01)
            assert stream.state == "READY"
    await asyncio.to_thread(run)
    assert sum(number > 1 and message.get("type") == "subscribe" for number, message in received) == 1
