# Chart

## Overview

### Available Operations

* [get_chart_config](#get_chart_config) - Get Chart Configuration
* [get_chart_history](#get_chart_history) - Get Historical Chart Data
* [get_quotes](#get_quotes) - Get Real-Time Quotes
* [search_symbols](#search_symbols) - Search Symbols
* [get_symbol_info](#get_symbol_info) - Get Symbol Information
* [get_tick_history](#get_tick_history) - Get Tick-Based Chart Data
* [get_chart_time](#get_chart_time) - Get Server Time

## get_chart_config

Returns the chart configuration including supported resolutions and charting capabilities. The response includes tick-based resolutions with a `T` suffix, minute-based resolutions, and daily, weekly, and monthly multipliers used by charting clients. It also indicates whether intraday, daily, weekly, and monthly data are available, plus search and time endpoint support.

### Example Usage

<!-- UsageSnippet language="python" operationID="getChartConfig" method="get" path="/v1/chart/config" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.chart.get_chart_config()

    assert res.chart_config is not None

    # Handle response
    print(res.chart_config)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetChartConfigResponse](../../models/getchartconfigresponse.md)**

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

## get_chart_history

Retrieves historical price bars (OHLCV - Open, High, Low, Close, Volume) for a specific symbol within a date range. This endpoint supports various time resolutions from seconds to months. The data is returned in arrays format optimized for charting libraries, with timestamps in Unix format (seconds).

### Example Usage

<!-- UsageSnippet language="python" operationID="getChartHistory" method="get" path="/v1/chart/history" example="success" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.chart.get_chart_history(symbol="AAPL", resolution=models.ChartResolution.D, from_=1672531200, to=1675209600, include_extended=False)

    assert res.chart_bars is not None

    # Handle response
    print(res.chart_bars)

```

### Parameters

| Parameter                                                                                                                                                                                                        | Type                                                                                                                                                                                                             | Required                                                                                                                                                                                                         | Description                                                                                                                                                                                                      | Example                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                               | Symbol to fetch bars for. Use the exact symbol returned by symbol search, such as `AAPL` for equities or the selected chart symbol for futures/options.                                                          | AAPL                                                                                                                                                                                                             |
| `resolution`                                                                                                                                                                                                     | [models.ChartResolution](../../models/chartresolution.md)                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                               | Candle size. Use minute values such as `1`, `5`, or `60` for intraday charts, `D` or `1D` for daily charts, `W` or `1W` for weekly charts, and `M`, `1M`, `3M`, `6M`, or `12M` for monthly views.                | D                                                                                                                                                                                                                |
| `from_`                                                                                                                                                                                                          | *int*                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                               | Start of the chart window as a Unix timestamp. Send seconds; millisecond timestamps are accepted and converted automatically. Negative timestamps are clamped to the Unix epoch.                                 | 1672531200                                                                                                                                                                                                       |
| `to`                                                                                                                                                                                                             | *int*                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                               | End of the chart window as a Unix timestamp. Must be greater than `from`. Send seconds; millisecond timestamps are accepted and converted automatically. A range entirely before the Unix epoch returns no_data. | 1675209600                                                                                                                                                                                                       |
| `first_data_request`                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                               | TradingView compatibility flag. Omit or send a non-zero value for the first chart request; send `0` for follow-up history requests.                                                                              |                                                                                                                                                                                                                  |
| `include_extended`                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                               | Set to `true` when the chart should include eligible pre-market and after-hours bars. Leave `false` for regular session charts.                                                                                  |                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                                              |                                                                                                                                                                                                                  |

### Response

**[models.GetChartHistoryResponse](../../models/getcharthistoryresponse.md)**

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

Retrieves quote data for one or multiple symbols. Returns current market data including last price, bid/ask prices, volume, high/low prices, change, and percent change. This endpoint supports bulk requests by providing comma-separated symbols, making it efficient for fetching quotes for multiple instruments simultaneously.

### Example Usage

<!-- UsageSnippet language="python" operationID="getQuotes" method="get" path="/v1/chart/quotes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.chart.get_quotes(symbols="AAPL,GOOGL,MSFT")

    assert res.quotes_response is not None

    # Handle response
    print(res.quotes_response)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `symbols`                                                                                                                                 | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | Comma-separated symbols to quote, such as `AAPL,MSFT`. Use one symbol for a quote tile or multiple symbols for watchlists and dashboards. | AAPL,GOOGL,MSFT                                                                                                                           |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.GetQuotesResponse](../../models/getquotesresponse.md)**

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

## search_symbols

Searches for trading symbols (stocks, indices, options, futures) based on a query string. Returns a list of matching symbols with symbol, ticker, description, exchange, and type. Supports equities, options (prefix query with '.'), and futures (prefix with '/'). Useful for symbol search autocomplete in charting UIs.

### Example Usage

<!-- UsageSnippet language="python" operationID="searchSymbols" method="get" path="/v1/chart/search" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.chart.search_symbols(query="Apple", limit=20)

    assert res.search_symbol_items is not None

    # Handle response
    print(res.search_symbol_items)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        | Example                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                            | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | Text to search. Use plain text for stocks and indices, `.` prefix for options such as `.AAPL`, and `/` prefix for futures such as `/ES`.           | Apple                                                                                                                                              |
| `limit`                                                                                                                                            | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Maximum number of results to return. Use smaller values for autocomplete and larger values for search result pages. Default is 20; maximum is 100. |                                                                                                                                                    |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |                                                                                                                                                    |

### Response

**[models.SearchSymbolsResponse](../../models/searchsymbolsresponse.md)**

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

## get_symbol_info

Retrieves detailed symbol information for charting: exchange, timezone, session, supported resolutions, price scale, format. Required for TradingView-style chart setup. For **futures**, symbol must start with '/' (e.g., /ES, /NQ).

### Example Usage

<!-- UsageSnippet language="python" operationID="getSymbolInfo" method="get" path="/v1/chart/symbols" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.chart.get_symbol_info(symbol="AAPL")

    assert res.symbol_info is not None

    # Handle response
    print(res.symbol_info)

```

### Parameters

| Parameter                                                                                                                                       | Type                                                                                                                                            | Required                                                                                                                                        | Description                                                                                                                                     | Example                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                        | *str*                                                                                                                                           | :heavy_check_mark:                                                                                                                              | Symbol to resolve for charting. Use equities like `AAPL` or futures with a leading slash such as `/ES`. Prefer values returned by chart search. | AAPL                                                                                                                                            |
| `retries`                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                | :heavy_minus_sign:                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                             |                                                                                                                                                 |

### Response

**[models.GetSymbolInfoResponse](../../models/getsymbolinforesponse.md)**

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

## get_tick_history

Retrieves tick-based chart bars for a specific symbol. Unlike time-based candles (which close every fixed number of minutes, hours, or days), a tick bar closes every time a fixed number of trades has occurred — for example, a `100T` bar closes after every 100 trades, whether that takes two seconds in a busy market or two minutes in a quiet one. This makes tick charts useful for visualizing market *activity* rather than the *passage of time*, which many traders use to spot momentum and unusual volume. Tick resolutions cannot be derived from time-based bars, so they are served from this dedicated endpoint rather than `/v1/chart/history`. Bar timestamps are returned in Unix milliseconds and are always strictly increasing, even for very actively traded symbols. Because tick bars are built from live trade activity rather than fixed calendar periods, older bars are loaded using the `cursor` pagination token instead of a date range — see the `cursor` and `nextTo` fields below.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTickHistory" method="get" path="/v1/chart/tick-history" example="success" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.chart.get_tick_history(symbol="AAPL", resolution=models.TickResolution.ONE_HUNDRED_T, countback=300, cursor="1784677563966606471")

    assert res.tick_chart_bars is not None

    # Handle response
    print(res.tick_chart_bars)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Symbol to fetch tick bars for. Use the exact symbol returned by symbol search, such as `AAPL` for equities.                                                                                                                                                                                                                                                                                                                                                                                                                                              | AAPL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `resolution`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [models.TickResolution](../../models/tickresolution.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Tick bar size: the number of trades that make up one bar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 100T                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `countback`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | How many bars to return, counting back from the most recent bar (or from `cursor`, if provided). Defaults to 300 when omitted. The maximum depends on `resolution`: each call is bounded by a fixed per-request trade budget, so low-count ticks (e.g. `1T`) can return up to 5000 bars, while high-count ticks (e.g. `1000T`) may cap out around 50. Requests above the resolution's maximum are silently reduced to it — this is normal, not an error. Use the `cursor` field to keep loading further back until you have as much history as you need. | 300                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `cursor`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Pagination token for loading OLDER bars, used when a user scrolls a chart backward in time. Omit this parameter for the initial chart load, which returns the most recent bars. To load the page before that, pass the `nextTo` value from the previous response as `cursor`. Treat this value as opaque — always pass it back exactly as received; do not attempt to construct, decode, or modify it.                                                                                                                                                   | 1784677563966606471                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

### Response

**[models.GetTickHistoryResponse](../../models/gettickhistoryresponse.md)**

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

## get_chart_time

Returns the current server time as a Unix timestamp in **seconds**. Response is plain text containing only the timestamp number (e.g., 1704067200). Useful for synchronizing client time with the server for charting.

### Example Usage

<!-- UsageSnippet language="python" operationID="getChartTime" method="get" path="/v1/chart/time" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.chart.get_chart_time()

    assert res.res is not None

    # Handle response
    print(res.res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetChartTimeResponse](../../models/getcharttimeresponse.md)**

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