# Aries WebSockets

The SDK includes synchronous and asynchronous WebSocket clients for streaming
market data, TradingView-shaped chart updates, and account events. The
`websockets` transport is installed as a normal SDK dependency.

## Authentication

Pass an OAuth access token (recommended when using Authorization Code or
PKCE), a token provider, or configure `client_id` and `client_secret` on
`FinanceDev`. In the last case the SDK requests a client-credentials token for
personal clients. Partner/business clients should pass a token obtained
through Authorization Code or PKCE. Tokens are sent only in the protocol auth
message and are not written to logs.

```python
from finance_dev import FinanceDev
from finance_dev.websocket import MarketSubscription

sdk = FinanceDev()
with sdk.websocket.market.connect(access_token=access_token) as stream:
    stream.subscribe([MarketSubscription(symbol="AAPL", quote_fields=["bidPrice", "askPrice"])])
    for event in stream:
        print(event)
```

Async use follows the same context-managed lifecycle:

```python
async with sdk.websocket.market.connect_async(access_token=access_token) as stream:
    await stream.subscribe([MarketSubscription(symbol="AAPL", quote_fields=["bidPrice", "askPrice"])])
    async for event in stream:
        print(event)
```

## Endpoint examples

Market subscription requests accept an array, including for a single symbol.
Events distinguish the initial `snapshot` from incremental `update` payloads;
updates may contain only changed fields. WebSocket frames can contain multiple
newline-delimited JSON messages, all of which are decoded in order.

Use `quote_fields="*"` and `trade_fields="*"` to request all fields for each
stream. The string `"all"` is not a supported wildcard and produces a server
error event. Explicit field lists, such as `["bidPrice", "askPrice"]`, are also
supported. A subscription containing only `symbol` selects both quotes and trades.

Setting `time_and_sales=True` alone selects only Time & Sales; it does not
implicitly enable quotes or trades. To receive all three streams, subscribe with:

```python
MarketSubscription(
    symbol="AAPL",
    quote_fields="*",
    trade_fields="*",
    time_and_sales=True,
)
```

This also applies when selecting Level 2 alone. Request quote/trade fields
explicitly when combining them with Level 2 or Time & Sales.

### Market event data

Market events expose a dictionary in `event.payload`, with `action` (`snapshot`
or `update`), `type` (`quote`, `trade`, or `timeAndSales`), `symbol`, and `data`.
The exported `QuoteData`, `TradeData`, and `TimeAndSalesData` helpers provide
typed access to `data`; parse the helper matching the event type:

```python
from finance_dev.websocket import QuoteData

if event.payload.get("type") == "quote":
    quote = QuoteData.model_validate(event.payload["data"])
    print(quote.bid_price, quote.ask_price)
```

| Event type | Data fields (wire names) | Value types |
| --- | --- | --- |
| `quote` | `bidPrice`, `bidChange`, `askPrice`, `askChange`, `midPrice`, `spread` | float |
| `quote` | `bidSize`, `bidSizeChange`, `askSize`, `askSizeChange`, `bidTimestamp`, `askTimestamp`, `quoteTimestamp` | int |
| `quote` | `bidExchange`, `askExchange` | str |
| `trade` | `price`, `openPrice`, `highPrice`, `lowPrice`, `lastPrice`, `netChange`, `closePrice`, `previousClosePrice` | float |
| `trade` | `size`, `totalVolume`, `tickVolume`, `tradeSeq`, `tradeTimestamp` | int |
| `trade` | `tick` | str |
| `timeAndSales` | `symbol`, `price`, `size`, `tick`, `tradeSeq`, `tradeExchange`, `tradeTimestamp` | str |

Timestamps are Unix milliseconds, represented as strings in Time & Sales.
Python attributes use snake case, such as `trade_timestamp`. All helper fields
are optional because field selection and incremental updates can omit values.
Unknown fields are preserved. Merge updates into your previous snapshot if you
need a complete current quote or trade record.

### Chart and account streams

```python
with sdk.websocket.chart.connect(access_token=access_token) as stream:
    stream.subscribe("AAPL", data_type="quotes")
    for event in stream:
        print(event)
```

```python
async with sdk.websocket.chart.connect_async(access_token=access_token) as stream:
    await stream.subscribe("AAPL", data_type="bars")
    async for event in stream:
        print(event)  # bars currently arrive in the server's quotes-shaped form
```

```python
with sdk.websocket.account.connect(access_token=access_token) as stream:
    snapshot = stream.subscribe_account("ACC123")
    for event in stream:
        print(event)
```

```python
async with sdk.websocket.account.connect_async(access_token=access_token) as stream:
    snapshot = await stream.subscribe_account("ACC123")
    async for event in stream:
        print(event)
```

The account subscription acknowledgement includes its initial snapshot.
`account.balance.apex` is a partial balance update. Watchlist and news event
payloads are arrays. P&L start times must include a timezone and supported
intervals (`15s`, `1m`, `5m`, `15m`, `1h`, `1d`, and `1mo`) are validated locally.

## Reconnects, refresh, and cleanup

Connections authenticate before their context manager returns. Transient
disconnects use exponential backoff with jitter, authenticate again, then
replay active subscriptions. Static tokens cannot be refreshed; supply a
callback provider when tokens need renewal. A `refreshAuth` event also causes
the provider to be called for a fresh token.

```python
from finance_dev.websocket import CallbackTokenProvider

provider = CallbackTokenProvider(refresh_access_token)
with sdk.websocket.market.connect(token_provider=provider) as stream:
    stream.subscribe([MarketSubscription(symbol="AAPL")])
```

Context exit closes the socket and its reader task/thread. Iterators must be
drained promptly, especially for market data; a full bounded queue closes the stream and raises
`WebSocketBackpressureError`. Raise `incoming_queue_size` in `WebSocketConfig`
when a larger buffer is appropriate.

Handle `WebSocketAuthenticationError`, `WebSocketRequestError`,
`WebSocketProtocolError`, and `WebSocketConnectionError` separately where the
application needs different recovery behavior.
