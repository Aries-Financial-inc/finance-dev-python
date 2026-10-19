# Stocks

## Overview

### Available Operations

* [get_aggregates](#get_aggregates) - Get Aggregate Bars
* [get_daily_summary](#get_daily_summary) - Get Daily Market Summary
* [get_last_quote](#get_last_quote) - Get Last Quote (NBBO)
* [get_last_trade](#get_last_trade) - Get Last Trade
* [get_open_close](#get_open_close) - Get Daily Ticker Summary
* [get_prev_day](#get_prev_day) - Get Previous Day Bar
* [get_quotes](#get_quotes) - Get Stock Quotes (NBBO)
* [get_snapshot](#get_snapshot) - Get Full Market Snapshot
* [get_trades](#get_trades) - Get Stock Trades
* [get_unified_snapshot](#get_unified_snapshot) - Get Unified Snapshot

## get_aggregates

Get aggregate bars for a stock over a time range with customizable time spans (second, minute, hour, day, week, month, quarter, year).

### Example Usage

<!-- UsageSnippet language="python" operationID="getStockAggregates" method="get" path="/v1/stocks/aggs" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stocks.get_aggregates(ticker="AAPL", multiplier=1, timespan=models.Timespan.DAY, from_="2024-01-01", to="2024-01-31", adjusted=True, limit=1000)

    assert res.stock_aggregates_response is not None

    # Handle response
    print(res.stock_aggregates_response)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       | Example                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `ticker`                                                                                                                          | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | Stock ticker symbol, such as AAPL. Use the exact ticker for the company you want to research.                                     | AAPL                                                                                                                              |
| `multiplier`                                                                                                                      | *int*                                                                                                                             | :heavy_check_mark:                                                                                                                | Size of each aggregate time window. Enter 1 or greater, such as 1 day or 5 minutes depending on `timespan`.                       | 1                                                                                                                                 |
| `timespan`                                                                                                                        | [models.Timespan](../../models/timespan.md)                                                                                       | :heavy_check_mark:                                                                                                                | Time span unit for each aggregate bar, such as minute, hour, day, week, month, quarter, or year when supported.                   | day                                                                                                                               |
| `from_`                                                                                                                           | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | Start date in YYYY-MM-DD format. Enter the first date to include in the research window. or timestamp                             | 2024-01-01                                                                                                                        |
| `to`                                                                                                                              | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | End date in YYYY-MM-DD format. Enter the last date to include in the research window. or timestamp                                | 2024-01-31                                                                                                                        |
| `adjusted`                                                                                                                        | *Optional[bool]*                                                                                                                  | :heavy_minus_sign:                                                                                                                | Whether to adjust historical prices for stock splits. Use true for normalized charting and false for raw market data.             | true                                                                                                                              |
| `sort`                                                                                                                            | [Optional[models.Sort]](../../models/sort.md)                                                                                     | :heavy_minus_sign:                                                                                                                | Sort direction for aggregate bars. Use `asc` for oldest first or `desc` for newest first.                                         |                                                                                                                                   |
| `limit`                                                                                                                           | *Optional[int]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits.             | 1000                                                                                                                              |
| `next`                                                                                                                            | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Pagination cursor from the previous response. Omit it on the first request, then send the returned cursor to fetch the next page. |                                                                                                                                   |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |                                                                                                                                   |

### Response

**[models.GetStockAggregatesResponse](../../models/getstockaggregatesresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_daily_summary

Get the daily open, high, low, and close (OHLC) for the entire market on a specific date.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDailyMarketSummary" method="get" path="/v1/stocks/grouped" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stocks.get_daily_summary(date_=date.fromisoformat("2024-01-15"), adjusted=True, include_otc=False)

    assert res.daily_market_summary_response is not None

    # Handle response
    print(res.daily_market_summary_response)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           | Example                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `date_`                                                                                                               | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                          | :heavy_check_mark:                                                                                                    | Date in YYYY-MM-DD format. Enter the specific calendar date you want to query.                                        | 2024-01-15                                                                                                            |
| `adjusted`                                                                                                            | *Optional[bool]*                                                                                                      | :heavy_minus_sign:                                                                                                    | Whether to adjust historical prices for stock splits. Use true for normalized charting and false for raw market data. | true                                                                                                                  |
| `include_otc`                                                                                                         | *Optional[bool]*                                                                                                      | :heavy_minus_sign:                                                                                                    | Whether to include over-the-counter securities. Use true only when your product needs OTC market coverage.            | false                                                                                                                 |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |                                                                                                                       |

### Response

**[models.GetDailyMarketSummaryResponse](../../models/getdailymarketsummaryresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_last_quote

Get the most recent NBBO (National Best Bid and Offer) quote for a stock.

### Example Usage

<!-- UsageSnippet language="python" operationID="getStockLastQuote" method="get" path="/v1/stocks/last-quote" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stocks.get_last_quote(ticker="AAPL")

    assert res.stock_last_quote_response is not None

    # Handle response
    print(res.stock_last_quote_response)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `ticker`                                                                                      | *str*                                                                                         | :heavy_check_mark:                                                                            | Stock ticker symbol, such as AAPL. Use the exact ticker for the company you want to research. | AAPL                                                                                          |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[models.GetStockLastQuoteResponse](../../models/getstocklastquoteresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_last_trade

Get the most recent trade for a stock.

### Example Usage

<!-- UsageSnippet language="python" operationID="getStockLastTrade" method="get" path="/v1/stocks/last-trade" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stocks.get_last_trade(ticker="AAPL")

    assert res.stock_last_trade_response is not None

    # Handle response
    print(res.stock_last_trade_response)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `ticker`                                                                                      | *str*                                                                                         | :heavy_check_mark:                                                                            | Stock ticker symbol, such as AAPL. Use the exact ticker for the company you want to research. | AAPL                                                                                          |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[models.GetStockLastTradeResponse](../../models/getstocklasttraderesponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_open_close

Get the open, close and afterhours prices of a stock on a specific date.

### Example Usage

<!-- UsageSnippet language="python" operationID="getStockOpenClose" method="get" path="/v1/stocks/open-close" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stocks.get_open_close(ticker="AAPL", date_=date.fromisoformat("2024-01-15"), adjusted=True)

    assert res.stock_open_close_response is not None

    # Handle response
    print(res.stock_open_close_response)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           | Example                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `ticker`                                                                                                              | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | Stock ticker symbol, such as AAPL. Use the exact ticker for the company you want to research.                         | AAPL                                                                                                                  |
| `date_`                                                                                                               | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                          | :heavy_check_mark:                                                                                                    | Date in YYYY-MM-DD format. Enter the specific calendar date you want to query.                                        | 2024-01-15                                                                                                            |
| `adjusted`                                                                                                            | *Optional[bool]*                                                                                                      | :heavy_minus_sign:                                                                                                    | Whether to adjust historical prices for stock splits. Use true for normalized charting and false for raw market data. | true                                                                                                                  |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |                                                                                                                       |

### Response

**[models.GetStockOpenCloseResponse](../../models/getstockopencloseresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_prev_day

Get the previous day's OHLCV (Open, High, Low, Close, Volume) data for a stock.

### Example Usage

<!-- UsageSnippet language="python" operationID="getStockPreviousDay" method="get" path="/v1/stocks/prev" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stocks.get_prev_day(ticker="AAPL", adjusted=True)

    assert res.stock_previous_day_response is not None

    # Handle response
    print(res.stock_previous_day_response)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           | Example                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `ticker`                                                                                                              | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | Stock ticker symbol, such as AAPL. Use the exact ticker for the company you want to research.                         | AAPL                                                                                                                  |
| `adjusted`                                                                                                            | *Optional[bool]*                                                                                                      | :heavy_minus_sign:                                                                                                    | Whether to adjust historical prices for stock splits. Use true for normalized charting and false for raw market data. | true                                                                                                                  |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |                                                                                                                       |

### Response

**[models.GetStockPreviousDayResponse](../../models/getstockpreviousdayresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_quotes

Get NBBO (National Best Bid and Offer) quotes for a stock with historical quote data.

### Example Usage

<!-- UsageSnippet language="python" operationID="getStockQuotes" method="get" path="/v1/stocks/quotes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stocks.get_quotes(ticker="AAPL", timestamp="2024-01-15", timestamp_from="2024-01-01", timestamp_after="2024-01-01", timestamp_to="2024-01-31", timestamp_before="2024-01-31", order=models.GetStockQuotesOrder.DESC, limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        | Example                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ticker`                                                                                                                                                           | *str*                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                 | Stock ticker symbol, such as AAPL. Use the exact ticker for the company you want to research.                                                                      | AAPL                                                                                                                                                               |
| `timestamp`                                                                                                                                                        | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Query by timestamp (YYYY-MM-DD or nanoseconds)                                                                                                                     | 2024-01-15                                                                                                                                                         |
| `timestamp_from`                                                                                                                                                   | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp start filter. Returns records at or after this timestamp.                                                                                                | 2024-01-01                                                                                                                                                         |
| `timestamp_after`                                                                                                                                                  | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp lower-bound filter. Returns records after this timestamp, excluding the timestamp itself.                                                                | 2024-01-01                                                                                                                                                         |
| `timestamp_to`                                                                                                                                                     | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp end filter. Returns records at or before this timestamp.                                                                                                 | 2024-01-31                                                                                                                                                         |
| `timestamp_before`                                                                                                                                                 | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp upper-bound filter. Returns records before this timestamp, excluding the timestamp itself.                                                               | 2024-01-31                                                                                                                                                         |
| `order`                                                                                                                                                            | [Optional[models.GetStockQuotesOrder]](../../models/getstockquotesorder.md)                                                                                        | :heavy_minus_sign:                                                                                                                                                 | Sort order for returned records. Use asc for oldest first or desc for newest first when supported.                                                                 |                                                                                                                                                                    |
| `limit`                                                                                                                                                            | *Optional[int]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits.                                              | 1000                                                                                                                                                               |
| `sort`                                                                                                                                                             | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Sort field used for ordering. Massive documents this separately from `order`, so enter the provider-supported field name in the text box, for example `timestamp`. |                                                                                                                                                                    |
| `next`                                                                                                                                                             | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Pagination cursor from the previous response. Omit it on the first request, then send the returned cursor to fetch the next page.                                  |                                                                                                                                                                    |
| `retries`                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                |                                                                                                                                                                    |

### Response

**[models.GetStockQuotesResponse](../../models/getstockquotesresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_snapshot

Get snapshot of all tickers or specific tickers with current day data including latest price, volume, and daily changes.

### Example Usage

<!-- UsageSnippet language="python" operationID="getStockSnapshots" method="get" path="/v1/stocks/snapshot" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stocks.get_snapshot(tickers="AAPL,TSLA,GOOG", include_otc=False)

    assert res.stock_snapshots_response is not None

    # Handle response
    print(res.stock_snapshots_response)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `tickers`                                                                                                  | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | Comma-separated list of tickers, such as AAPL,MSFT. Use this to request several companies in one call.     | AAPL,TSLA,GOOG                                                                                             |
| `include_otc`                                                                                              | *Optional[bool]*                                                                                           | :heavy_minus_sign:                                                                                         | Whether to include over-the-counter securities. Use true only when your product needs OTC market coverage. | false                                                                                                      |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |                                                                                                            |

### Response

**[models.GetStockSnapshotsResponse](../../models/getstocksnapshotsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_trades

Get tick-level trade data for a stock with precise timestamps.

### Example Usage

<!-- UsageSnippet language="python" operationID="getStockTrades" method="get" path="/v1/stocks/trades" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stocks.get_trades(ticker="AAPL", timestamp="2024-01-15", timestamp_from="2024-01-01", timestamp_after="2024-01-01", timestamp_to="2024-01-31", timestamp_before="2024-01-31", order=models.GetStockTradesOrder.DESC, limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        | Example                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ticker`                                                                                                                                                           | *str*                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                 | Stock ticker symbol, such as AAPL. Use the exact ticker for the company you want to research.                                                                      | AAPL                                                                                                                                                               |
| `timestamp`                                                                                                                                                        | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Query by timestamp (YYYY-MM-DD or nanoseconds)                                                                                                                     | 2024-01-15                                                                                                                                                         |
| `timestamp_from`                                                                                                                                                   | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp start filter. Returns records at or after this timestamp.                                                                                                | 2024-01-01                                                                                                                                                         |
| `timestamp_after`                                                                                                                                                  | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp lower-bound filter. Returns records after this timestamp, excluding the timestamp itself.                                                                | 2024-01-01                                                                                                                                                         |
| `timestamp_to`                                                                                                                                                     | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp end filter. Returns records at or before this timestamp.                                                                                                 | 2024-01-31                                                                                                                                                         |
| `timestamp_before`                                                                                                                                                 | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp upper-bound filter. Returns records before this timestamp, excluding the timestamp itself.                                                               | 2024-01-31                                                                                                                                                         |
| `order`                                                                                                                                                            | [Optional[models.GetStockTradesOrder]](../../models/getstocktradesorder.md)                                                                                        | :heavy_minus_sign:                                                                                                                                                 | Sort order for returned records. Use asc for oldest first or desc for newest first when supported.                                                                 |                                                                                                                                                                    |
| `limit`                                                                                                                                                            | *Optional[int]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits.                                              | 1000                                                                                                                                                               |
| `sort`                                                                                                                                                             | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Sort field used for ordering. Massive documents this separately from `order`, so enter the provider-supported field name in the text box, for example `timestamp`. |                                                                                                                                                                    |
| `next`                                                                                                                                                             | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Pagination cursor from the previous response. Omit it on the first request, then send the returned cursor to fetch the next page.                                  |                                                                                                                                                                    |
| `retries`                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                |                                                                                                                                                                    |

### Response

**[models.GetStockTradesResponse](../../models/getstocktradesresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_unified_snapshot

Get unified snapshots across asset classes (`stocks`, `options`, `fx`, `crypto`, `indices`). `ticker` accepts a single symbol only. Use `tickersAnyOf` for multiple symbols. If `ticker` contains multiple comma-separated values, the API returns 400: "Multiple tickers are not supported. Please provide a single ticker." If both `ticker` and `tickersAnyOf` are set, the API returns 400: "Cannot specify both ticker and tickersAnyOf. Use ticker for a single symbol or tickersAnyOf for multiple." For `type=options`, response items may include options-specific fields like `details`, `greeks`, `impliedVolatility`, `openInterest`, `breakEvenPrice`, and `underlyingAsset`; non-applicable fields are omitted.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUnifiedSnapshot" method="get" path="/v1/stocks/unified-snapshot" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stocks.get_unified_snapshot(type_=models.GetUnifiedSnapshotType.STOCKS, ticker="AAPL", tickers_any_of="AAPL,TSLA,GOOG", ticker_from="A", ticker_after="A", ticker_to="Z", ticker_before="Z", order=models.GetUnifiedSnapshotOrder.ASC, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                                                                                                                                                                  | [Optional[models.GetUnifiedSnapshotType]](../../models/getunifiedsnapshottype.md)                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                      | Which asset class to include in the snapshot. Allowed values:<br/>- `stocks` — equities and ETFs.<br/>- `options` — option contracts.<br/>- `fx` — foreign-exchange currency pairs.<br/>- `crypto` — cryptocurrencies.<br/>- `indices` — market indices like SPX, NDX, VIX. | stocks                                                                                                                                                                                                                                                  |
| `ticker`                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | Single ticker symbol filter. Enter one ticker such as AAPL to narrow results to one company. In the docs playground, if you enter `ticker`, do not select `type`, because selecting `type` can clear the `ticker` field.                                | AAPL                                                                                                                                                                                                                                                    |
| `tickers_any_of`                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | Comma-separated list of ticker symbols (maximum 250).                                                                                                                                                                                                   | AAPL,TSLA,GOOG                                                                                                                                                                                                                                          |
| `ticker_from`                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | Ticker lower-bound filter. Returns symbols alphabetically on or after this ticker.                                                                                                                                                                      | A                                                                                                                                                                                                                                                       |
| `ticker_after`                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | Ticker lower-bound filter. Returns symbols alphabetically after this ticker, excluding the ticker itself.                                                                                                                                               | A                                                                                                                                                                                                                                                       |
| `ticker_to`                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | Ticker upper-bound filter. Returns symbols alphabetically on or before this ticker.                                                                                                                                                                     | Z                                                                                                                                                                                                                                                       |
| `ticker_before`                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | Ticker upper-bound filter. Returns symbols alphabetically before this ticker, excluding the ticker itself.                                                                                                                                              | Z                                                                                                                                                                                                                                                       |
| `order`                                                                                                                                                                                                                                                 | [Optional[models.GetUnifiedSnapshotOrder]](../../models/getunifiedsnapshotorder.md)                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                      | Sort order for returned records. Use asc for oldest first or desc for newest first when supported.                                                                                                                                                      |                                                                                                                                                                                                                                                         |
| `limit`                                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits.                                                                                                                                   | 10                                                                                                                                                                                                                                                      |
| `sort`                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | Sort field used for ordering. Massive documents this separately from `order`, so enter the provider-supported field name in the text box, for example `ticker`.                                                                                         |                                                                                                                                                                                                                                                         |
| `next`                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | Pagination cursor from the previous response. Omit it on the first request, then send the returned cursor to fetch the next page.                                                                                                                       |                                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                     |                                                                                                                                                                                                                                                         |

### Response

**[models.GetUnifiedSnapshotResponse](../../models/getunifiedsnapshotresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |