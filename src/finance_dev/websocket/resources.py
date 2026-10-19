"""Endpoint-specific connection factories and topic helpers."""

# Resources share request IDs and subscription state with their connections.
# pylint: disable=protected-access

from datetime import datetime
from typing import Sequence
from .auth import (
    AsyncClientCredentialsTokenProvider,
    ClientCredentialsTokenProvider,
    StaticTokenProvider,
)
from .config import ACCOUNT_URL, CHART_URL, MARKET_URL
from .errors import WebSocketAuthenticationError
from .models import MarketSubscription, MarketUnsubscribe, PnlSubscription
from .transport.async_connection import AsyncConnection
from .transport.sync_connection import SyncConnection


class Resource:
    endpoint = ""

    def __init__(self, sdk_configuration):
        self.sdk_configuration = sdk_configuration

    def _provider(self, access_token, token_provider, asynchronous=False):
        if access_token is not None and token_provider is not None:
            raise WebSocketAuthenticationError(
                "Supply either access_token or token_provider, not both"
            )
        if access_token is not None:
            if not isinstance(access_token, str) or not access_token:
                raise WebSocketAuthenticationError(
                    "access_token must be a non-empty string"
                )
            return StaticTokenProvider(access_token)
        if token_provider is not None:
            return token_provider
        security = self.sdk_configuration.security
        if callable(security):
            security = security()
        cid = getattr(security, "client_id", None) if security else None
        secret = getattr(security, "client_secret", None) if security else None
        if not cid or not secret:
            raise WebSocketAuthenticationError(
                "Supply an access_token or token_provider, or configure client_id and client_secret"
            )
        token_url = (
            getattr(security, "token_url", None)
            or "https://api.aries.com/v1/oauth2/token"
        )
        return (
            AsyncClientCredentialsTokenProvider(token_url, cid, secret)
            if asynchronous
            else ClientCredentialsTokenProvider(token_url, cid, secret)
        )

    def connect(self, *, access_token=None, token_provider=None, url=None, config=None):
        stream = SyncConnection(
            url or self.endpoint, self._provider(access_token, token_provider), config
        )
        stream.resource = self
        return stream

    def connect_async(
        self, *, access_token=None, token_provider=None, url=None, config=None
    ):
        stream = AsyncConnection(
            url or self.endpoint,
            self._provider(access_token, token_provider, True),
            config,
        )
        stream.resource = self
        return stream


class MarketResource(Resource):
    protocol = "market"
    endpoint = MARKET_URL

    def subscribe(self, stream, items: Sequence[MarketSubscription]):
        body = [
            (
                i.model_dump(exclude_none=True, by_alias=True)
                if isinstance(i, MarketSubscription)
                else i
            )
            for i in items
        ]
        ident = stream._id("subscribe")
        stream.send_message({"type": "subscribe", "id": ident, "payload": body})
        return ident

    async def subscribe_async(self, stream, items):
        body = [
            (
                i.model_dump(exclude_none=True, by_alias=True)
                if isinstance(i, MarketSubscription)
                else i
            )
            for i in items
        ]
        ident = stream._id("subscribe")
        await stream.send_message({"type": "subscribe", "id": ident, "payload": body})
        return ident

    def unsubscribe(self, stream, items: Sequence[str | MarketUnsubscribe]):
        body = [
            i if isinstance(i, str) else i.model_dump(exclude_none=True, by_alias=True)
            for i in items
        ]
        ident = stream._id("unsubscribe")
        stream.send_message({"type": "unsubscribe", "id": ident, "payload": body})
        return ident

    async def unsubscribe_async(self, stream, items):
        body = [
            i if isinstance(i, str) else i.model_dump(exclude_none=True, by_alias=True)
            for i in items
        ]
        ident = stream._id("unsubscribe")
        await stream.send_message({"type": "unsubscribe", "id": ident, "payload": body})
        return ident

    def request(self, stream, method, path, *, query=None, body=None):
        return stream.request(method, path, query=query, body=body)

    async def request_async(self, stream, method, path, *, query=None, body=None):
        return await stream.request(method, path, query=query, body=body)

    def get_option_expiry_dates(self, stream, symbol):
        return stream.request("GET", f"/options/{symbol}/expiry-dates")

    async def get_option_expiry_dates_async(self, stream, symbol):
        return await stream.request("GET", f"/options/{symbol}/expiry-dates")

    def get_option_contract_symbols(self, stream, symbol, expiration):
        return stream.request("GET", f"/options/{symbol}/contracts/{expiration}")

    async def get_option_contract_symbols_async(self, stream, symbol, expiration):
        return await stream.request("GET", f"/options/{symbol}/contracts/{expiration}")


class ChartResource(Resource):
    protocol = "chart"
    endpoint = CHART_URL

    def subscribe(self, stream, symbol, *, data_type="quotes", symbol_type=None):
        ident = stream._id("subscribe")
        payload = {"type": data_type, "symbol": symbol}
        if symbol_type:
            payload["symbolType"] = symbol_type
        stream.send_message({"type": "subscribe", "id": ident, "payload": payload})
        return ident

    async def subscribe_async(
        self, stream, symbol, *, data_type="quotes", symbol_type=None
    ):
        ident = stream._id("subscribe")
        payload = {"type": data_type, "symbol": symbol}
        if symbol_type:
            payload["symbolType"] = symbol_type
        await stream.send_message(
            {"type": "subscribe", "id": ident, "payload": payload}
        )
        return ident

    def unsubscribe(self, stream, symbol):
        ident = stream._id("unsubscribe")
        stream.send_message(
            {
                "type": "unsubscribe",
                "id": ident,
                "payload": {"type": "quotes", "symbol": symbol},
            }
        )
        return ident

    async def unsubscribe_async(self, stream, symbol):
        ident = stream._id("unsubscribe")
        await stream.send_message(
            {
                "type": "unsubscribe",
                "id": ident,
                "payload": {"type": "quotes", "symbol": symbol},
            }
        )
        return ident


class AccountResource(Resource):
    protocol = "account"
    endpoint = ACCOUNT_URL

    def _sub(self, stream, topic, params=None):
        payload = {"topic": topic}
        if params:
            payload["params"] = {k: v for k, v in params.items() if v is not None}
        message = {
            "type": "subscribe",
            "id": stream._id("subscribe"),
            "payload": payload,
        }
        result = stream.exchange(message)
        stream._active[topic + ":" + str(payload.get("params", {}))] = message
        return result

    async def _suba(self, stream, topic, params=None):
        payload = {"topic": topic}
        if params:
            payload["params"] = {k: v for k, v in params.items() if v is not None}
        message = {
            "type": "subscribe",
            "id": stream._id("subscribe"),
            "payload": payload,
        }
        result = await stream.exchange(message)
        stream._active[topic + ":" + str(payload.get("params", {}))] = message
        return result

    def subscribe_account(self, stream, account_id):
        return self._sub(stream, "account", {"accountId": account_id})

    async def subscribe_account_async(self, stream, account_id):
        return await self._suba(stream, "account", {"accountId": account_id})

    def subscribe_pnl(self, stream, account_id, start_time, *, interval="1m"):
        item = PnlSubscription.model_validate(
            {"account_id": account_id, "start_time": start_time, "interval": interval}
        )
        if interval not in {"15s", "1m", "5m", "15m", "1h", "1d", "1mo"}:
            raise ValueError("unsupported P&L interval")
        return self._sub(
            stream,
            "pnl",
            {
                "accountId": account_id,
                "startTime": (
                    item.start_time.isoformat()
                    if isinstance(item.start_time, datetime)
                    else item.start_time
                ),
                "interval": interval,
            },
        )

    async def subscribe_pnl_async(
        self, stream, account_id, start_time, *, interval="1m"
    ):
        item = PnlSubscription.model_validate(
            {"account_id": account_id, "start_time": start_time, "interval": interval}
        )
        if interval not in {"15s", "1m", "5m", "15m", "1h", "1d", "1mo"}:
            raise ValueError("unsupported P&L interval")
        return await self._suba(
            stream,
            "pnl",
            {
                "accountId": account_id,
                "startTime": (
                    item.start_time.isoformat()
                    if isinstance(item.start_time, datetime)
                    else item.start_time
                ),
                "interval": interval,
            },
        )

    def subscribe_watchlist(self, stream):
        return self._sub(stream, "watchlist")

    async def subscribe_watchlist_async(self, stream):
        return await self._suba(stream, "watchlist")

    def subscribe_news(self, stream, *, symbols=None, topics=None):
        return self._sub(stream, "news", {"symbols": symbols, "topics": topics})

    async def subscribe_news_async(self, stream, *, symbols=None, topics=None):
        return await self._suba(stream, "news", {"symbols": symbols, "topics": topics})

    def _unsub(self, stream, topic, params=None):
        payload = {"topic": topic}
        if params:
            payload["params"] = params
        result = stream.exchange(
            {"type": "unsubscribe", "id": stream._id("unsubscribe"), "payload": payload}
        )
        for key in list(stream._active):
            if key.startswith(topic + ":"):
                stream._active.pop(key, None)
        return result

    async def _unsuba(self, stream, topic, params=None):
        payload = {"topic": topic}
        if params:
            payload["params"] = params
        result = await stream.exchange(
            {"type": "unsubscribe", "id": stream._id("unsubscribe"), "payload": payload}
        )
        for key in list(stream._active):
            if key.startswith(topic + ":"):
                stream._active.pop(key, None)
        return result

    def unsubscribe_account(self, stream, account_id):
        return self._unsub(stream, "account", {"accountId": account_id})

    async def unsubscribe_account_async(self, stream, account_id):
        return await self._unsuba(stream, "account", {"accountId": account_id})

    def unsubscribe_pnl(self, stream, account_id):
        return self._unsub(stream, "pnl", {"accountId": account_id})

    async def unsubscribe_pnl_async(self, stream, account_id):
        return await self._unsuba(stream, "pnl", {"accountId": account_id})

    def unsubscribe_watchlist(self, stream):
        return self._unsub(stream, "watchlist")

    async def unsubscribe_watchlist_async(self, stream):
        return await self._unsuba(stream, "watchlist")

    def unsubscribe_news(self, stream):
        return self._unsub(stream, "news")

    async def unsubscribe_news_async(self, stream):
        return await self._unsuba(stream, "news")
