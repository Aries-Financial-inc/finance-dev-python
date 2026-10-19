# Hand-maintained WebSocket tests; preserved by Speakeasy persistent edits.
import asyncio

import pytest
from finance_dev.websocket.auth import StaticTokenProvider
from finance_dev.websocket.config import WebSocketConfig
from finance_dev.websocket.errors import WebSocketConnectionStateError
from finance_dev.websocket.errors import WebSocketBackpressureError
from finance_dev.websocket.transport.async_connection import AsyncConnection
from finance_dev.websocket.transport.sync_connection import SyncConnection
from finance_dev import FinanceDev
from finance_dev.websocket.models import MarketSubscription, MarketUnsubscribe


@pytest.mark.asyncio
@pytest.mark.parametrize("endpoint", ["market", "chart"])
async def test_async_resource_subscription_reaches_server(local_ws_server, endpoint):
    url, received = local_ws_server
    sdk = FinanceDev()
    resource = getattr(sdk.websocket, endpoint)
    async with resource.connect_async(
        url=url, access_token="token", config=WebSocketConfig(ping_interval=60)
    ) as stream:
        if endpoint == "market":
            subscribe_id = await stream.subscribe([
                MarketSubscription(symbol="AAPL", quote_fields=["bidPrice"])
            ])
            unsubscribe_id = await stream.unsubscribe([MarketUnsubscribe(symbol="AAPL")])
            expected_subscribe = [{"symbol": "AAPL", "quoteFields": ["bidPrice"]}]
            expected_unsubscribe = [{"symbol": "AAPL"}]
        else:
            subscribe_id = await stream.subscribe("AAPL", data_type="bars", symbol_type="equity")
            unsubscribe_id = await stream.unsubscribe("AAPL")
            expected_subscribe = {"type": "bars", "symbol": "AAPL", "symbolType": "equity"}
            expected_unsubscribe = {"type": "quotes", "symbol": "AAPL"}
        # A correlated response ensures the server processed both preceding sends.
        await stream.request("GET", "/barrier")
        assert isinstance(subscribe_id, str)
        assert isinstance(unsubscribe_id, str)
        assert subscribe_id != unsubscribe_id
        assert received[1:3] == [
            {"type": "subscribe", "id": subscribe_id, "payload": expected_subscribe},
            {"type": "unsubscribe", "id": unsubscribe_id, "payload": expected_unsubscribe},
        ]

@pytest.mark.asyncio
async def test_async_connection_auth_correlation_and_account_ack(local_ws_server):
    url, received = local_ws_server
    connection = AsyncConnection(url, StaticTokenProvider("test-token"), WebSocketConfig(ping_interval=60))
    with pytest.raises(WebSocketConnectionStateError):
        await connection.subscribe({"topic":"account"})
    async with connection:
        ack = await connection.exchange({"type":"subscribe","payload":{"topic":"account"}})
        assert ack["type"] == "subscribed"
        response = await connection.request("GET", "/snapshot")
        assert response["payload"]["data"]["ok"] is True
        assert received[0]["payload"]["path"] == "/auth"
        assert received[1]["type"] == "subscribe"

@pytest.mark.asyncio
async def test_sync_connection_uses_single_reader(local_ws_server):
    url, received = local_ws_server
    def run():
        connection = SyncConnection(url, StaticTokenProvider("test-token"), WebSocketConfig(ping_interval=60))
        with connection:
            result = connection.request("GET", "/snapshot")
            return result["payload"]["data"]["ok"]
    assert await asyncio.to_thread(run)
    assert received[0]["payload"]["path"] == "/auth"

@pytest.mark.asyncio
async def test_full_event_queue_is_reported(local_ws_server):
    url, _ = local_ws_server
    config=WebSocketConfig(ping_interval=60,incoming_queue_size=1)
    connection=AsyncConnection(url,StaticTokenProvider("token"),config)
    async with connection:
        await connection.subscribe([{"symbol":"AAPL"}])
        await asyncio.sleep(0.05)
        assert (await connection.get_event()).payload["sequence"] == 0
        with pytest.raises(WebSocketBackpressureError): await connection.__anext__()
