# Options

## Overview

### Available Operations

* [get_activity](#get_activity) - Get Options Activity
* [get_last_trade](#get_last_trade) - Get Options Last Trade
* [get_open_close_data](#get_open_close_data) - Get Option Open/Close Data
* [get_previous_day](#get_previous_day) - Get Previous Day Option Data
* [get_quotes](#get_quotes) - Get Options Quotes
* [get_option_chain_snapshot](#get_option_chain_snapshot) - Get option chain snapshot
* [get_option_contract_snapshot](#get_option_contract_snapshot) - Get option contract snapshot
* [get_trades](#get_trades) - Get Options Trades
* [get_unusual_activity](#get_unusual_activity) - Get Options Unusual Activity by Symbol
* [get_contracts](#get_contracts) - Get Options Contract Symbols
* [get_expiry_dates](#get_expiry_dates) - Get Options Expiry Dates

## get_activity

Retrieve unusual options activity including large block trades, high volume contracts, and significant changes in open interest.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionsActivity" method="get" path="/v1/options/activity" example="success" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_activity()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `date_from`                                                                                              | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                             | :heavy_minus_sign:                                                                                       | Start date for filtering options activity in YYYY-MM-DD format                                           |
| `date_to`                                                                                                | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                             | :heavy_minus_sign:                                                                                       | End date for filtering options activity in YYYY-MM-DD format                                             |
| `tickers`                                                                                                | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | Comma-separated list of ticker symbols to filter results                                                 |
| `page`                                                                                                   | *Optional[int]*                                                                                          | :heavy_minus_sign:                                                                                       | Page number for pagination (zero-based)                                                                  |
| `page_size`                                                                                              | *Optional[int]*                                                                                          | :heavy_minus_sign:                                                                                       | Number of results per page. Use this to control pagination size in list views. (default: 100, max: 1000) |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[models.GetOptionsActivityResponse](../../models/getoptionsactivityresponse.md)**

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

Get the most recent trade for an options contract.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionLastTrade" method="get" path="/v1/options/last-trade" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_last_trade(ticker="O:AAPL230120C00150000")

    assert res.option_last_trade_response is not None

    # Handle response
    print(res.option_last_trade_response)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 | Example                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `ticker`                                                                                                    | *str*                                                                                                       | :heavy_check_mark:                                                                                          | Options contract ticker symbol. Enter the exact option symbol returned by option search or chain endpoints. | O:AAPL230120C00150000                                                                                       |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |                                                                                                             |

### Response

**[models.GetOptionLastTradeResponse](../../models/getoptionlasttraderesponse.md)**

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

## get_open_close_data

Retrieve option contract opening and closing prices with intraday trading ranges for specific option contracts.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionOpenClose" method="get" path="/v1/options/open-close" example="success" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_open_close_data(ticker="<value>", date_=date.fromisoformat("2024-10-03"))

    assert res.option_open_close_response is not None

    # Handle response
    print(res.option_open_close_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `ticker`                                                                       | *str*                                                                          | :heavy_check_mark:                                                             | OCC option ticker symbol (e.g., O:AAPL251219C00150000)                         |
| `date_`                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)   | :heavy_check_mark:                                                             | Date in YYYY-MM-DD format. Enter the specific calendar date you want to query. |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[models.GetOptionOpenCloseResponse](../../models/getoptionopencloseresponse.md)**

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

## get_previous_day

Retrieve the previous trading day's OHLC bar (open, high, low, close), volume, volume-weighted average price (VWAP), bar timestamp, and trade count for a single option contract. Useful for change-vs-yesterday comparisons, daily charts, and volatility/volume baselines.

### Example Usage: minimal

<!-- UsageSnippet language="python" operationID="getOptionPreviousDay" method="get" path="/v1/options/previous-day" example="minimal" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_previous_day(ticker="<value>")

    assert res.option_previous_day_response is not None

    # Handle response
    print(res.option_previous_day_response)

```
### Example Usage: success

<!-- UsageSnippet language="python" operationID="getOptionPreviousDay" method="get" path="/v1/options/previous-day" example="success" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_previous_day(ticker="<value>")

    assert res.option_previous_day_response is not None

    # Handle response
    print(res.option_previous_day_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ticker`                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                  | Option contract identifier in OCC/OSI format. The 21-character form is `ROOT + YYMMDD + C/P + strike-in-cents` (e.g. `AAPL251219C00150000` = AAPL Dec-19-2025 $150 Call). The optional `O:` prefix is accepted and stripped (so `O:AAPL251219C00150000` works too). |
| `retries`                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                 |

### Response

**[models.GetOptionPreviousDayResponse](../../models/getoptionpreviousdayresponse.md)**

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

Get quote data for options contracts including bid, ask, and Greeks.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionQuotes" method="get" path="/v1/options/quotes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_quotes(ticker="O:AAPL230120C00150000", timestamp="2024-01-15", timestamp_from="2024-01-01", timestamp_after="2024-01-01", timestamp_to="2024-01-31", timestamp_before="2024-01-31", order=models.GetOptionQuotesOrder.DESC, limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        | Example                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ticker`                                                                                                                                                           | *str*                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                 | Options contract ticker symbol. Enter the exact option symbol returned by option search or chain endpoints.                                                        | O:AAPL230120C00150000                                                                                                                                              |
| `timestamp`                                                                                                                                                        | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Query by timestamp (YYYY-MM-DD or nanoseconds)                                                                                                                     | 2024-01-15                                                                                                                                                         |
| `timestamp_from`                                                                                                                                                   | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp start filter. Returns records at or after this timestamp.                                                                                                | 2024-01-01                                                                                                                                                         |
| `timestamp_after`                                                                                                                                                  | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp lower-bound filter. Returns records after this timestamp, excluding the timestamp itself.                                                                | 2024-01-01                                                                                                                                                         |
| `timestamp_to`                                                                                                                                                     | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp end filter. Returns records at or before this timestamp.                                                                                                 | 2024-01-31                                                                                                                                                         |
| `timestamp_before`                                                                                                                                                 | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp upper-bound filter. Returns records before this timestamp, excluding the timestamp itself.                                                               | 2024-01-31                                                                                                                                                         |
| `order`                                                                                                                                                            | [Optional[models.GetOptionQuotesOrder]](../../models/getoptionquotesorder.md)                                                                                      | :heavy_minus_sign:                                                                                                                                                 | Sort order for returned records. Use asc for oldest first or desc for newest first when supported.                                                                 |                                                                                                                                                                    |
| `limit`                                                                                                                                                            | *Optional[int]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits.                                              | 1000                                                                                                                                                               |
| `sort`                                                                                                                                                             | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Sort field used for ordering. Massive documents this separately from `order`, so enter the provider-supported field name in the text box, for example `timestamp`. |                                                                                                                                                                    |
| `next`                                                                                                                                                             | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Pagination cursor from the previous response. Omit it on the first request, then send the returned cursor to fetch the next page.                                  |                                                                                                                                                                    |
| `retries`                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                |                                                                                                                                                                    |

### Response

**[models.GetOptionQuotesResponse](../../models/getoptionquotesresponse.md)**

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

## get_option_chain_snapshot

Returns a paginated snapshot of option contracts for an underlying equity. Supports optional filters on strike, expiration, and contract type. Query parameters use camelCase; pagination uses `nextUrl` in the response body. Uses the upstream chain snapshot data source.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionChainSnapshot" method="get" path="/v1/options/snapshot/chain/{underlyingAsset}" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_option_chain_snapshot(underlying_asset="AAPL", strike_price="190", expiration_date=date.fromisoformat("2024-01-19"), contract_type="call", order=models.GetOptionChainSnapshotOrder.ASC, limit=50)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              | Example                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `underlying_asset`                                                                                                                                                                                       | *str*                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                       | Underlying equity symbol (for example AAPL).                                                                                                                                                             | AAPL                                                                                                                                                                                                     |
| `strike_price`                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Filter by exact strike price (numeric string).                                                                                                                                                           | 190                                                                                                                                                                                                      |
| `expiration_date`                                                                                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                       | Filter by expiration date (typically YYYY-MM-DD).                                                                                                                                                        | 2024-01-19                                                                                                                                                                                               |
| `contract_type`                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Filter by contract type (for example call or put).                                                                                                                                                       | call                                                                                                                                                                                                     |
| `strike_price_gte`                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Strike price greater than or equal to this value.                                                                                                                                                        |                                                                                                                                                                                                          |
| `strike_price_gt`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Strike price strictly greater than this value.                                                                                                                                                           |                                                                                                                                                                                                          |
| `strike_price_lte`                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Strike price less than or equal to this value.                                                                                                                                                           |                                                                                                                                                                                                          |
| `strike_price_lt`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Strike price strictly less than this value.                                                                                                                                                              |                                                                                                                                                                                                          |
| `expiration_date_gte`                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Expiration date greater than or equal to this value.                                                                                                                                                     |                                                                                                                                                                                                          |
| `expiration_date_gt`                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Expiration date strictly greater than this value.                                                                                                                                                        |                                                                                                                                                                                                          |
| `expiration_date_lte`                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Expiration date less than or equal to this value.                                                                                                                                                        |                                                                                                                                                                                                          |
| `expiration_date_lt`                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Expiration date strictly less than this value.                                                                                                                                                           |                                                                                                                                                                                                          |
| `order`                                                                                                                                                                                                  | [Optional[models.GetOptionChainSnapshotOrder]](../../models/getoptionchainsnapshotorder.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                       | Sort order for returned records. Use asc for oldest first or desc for newest first when supported. for results.                                                                                          |                                                                                                                                                                                                          |
| `limit`                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Maximum number of contracts per page (1–250).                                                                                                                                                            | 50                                                                                                                                                                                                       |
| `sort`                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Sort field used for ordering. Massive documents this separately from `order`, so enter the provider-supported field name in the text box.                                                                |                                                                                                                                                                                                          |
| `next`                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Pagination cursor from the previous response. Omit it on the first request, then send the returned cursor to fetch the next page. You can also follow the absolute `nextUrl` from the previous response. |                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                      |                                                                                                                                                                                                          |

### Response

**[models.GetOptionChainSnapshotResponse](../../models/getoptionchainsnapshotresponse.md)**

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

## get_option_contract_snapshot

Returns a point-in-time snapshot for a single option contract: details, day bar, last quote, last trade, Greeks, implied volatility, and underlying context when available. Responses may be cached for approximately five minutes. Uses the upstream contract snapshot data source.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionContractSnapshot" method="get" path="/v1/options/snapshot/{underlyingAsset}/{optionContract}" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_option_contract_snapshot(underlying_asset="AAPL", option_contract="O:AAPL260410C00110000")

    assert res.option_contract_snapshot_response is not None

    # Handle response
    print(res.option_contract_snapshot_response)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `underlying_asset`                                                          | *str*                                                                       | :heavy_check_mark:                                                          | Underlying equity symbol (for example AAPL).                                | AAPL                                                                        |
| `option_contract`                                                           | *str*                                                                       | :heavy_check_mark:                                                          | OCC-format options contract identifier (for example O:AAPL240119C00190000). | O:AAPL260410C00110000                                                       |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.GetOptionContractSnapshotResponse](../../models/getoptioncontractsnapshotresponse.md)**

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

Get tick-level trade data for options contracts with precise timestamps.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionTrades" method="get" path="/v1/options/trades" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_trades(ticker="O:AAPL230120C00150000", timestamp="2024-01-15", timestamp_from="2024-01-01", timestamp_after="2024-01-01", timestamp_to="2024-01-31", timestamp_before="2024-01-31", order=models.GetOptionTradesOrder.DESC, limit=1000)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        | Example                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ticker`                                                                                                                                                           | *str*                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                 | Options contract ticker symbol. Enter the exact option symbol returned by option search or chain endpoints.                                                        | O:AAPL230120C00150000                                                                                                                                              |
| `timestamp`                                                                                                                                                        | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Query by timestamp (YYYY-MM-DD or nanoseconds)                                                                                                                     | 2024-01-15                                                                                                                                                         |
| `timestamp_from`                                                                                                                                                   | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp start filter. Returns records at or after this timestamp.                                                                                                | 2024-01-01                                                                                                                                                         |
| `timestamp_after`                                                                                                                                                  | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp lower-bound filter. Returns records after this timestamp, excluding the timestamp itself.                                                                | 2024-01-01                                                                                                                                                         |
| `timestamp_to`                                                                                                                                                     | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp end filter. Returns records at or before this timestamp.                                                                                                 | 2024-01-31                                                                                                                                                         |
| `timestamp_before`                                                                                                                                                 | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Timestamp upper-bound filter. Returns records before this timestamp, excluding the timestamp itself.                                                               | 2024-01-31                                                                                                                                                         |
| `order`                                                                                                                                                            | [Optional[models.GetOptionTradesOrder]](../../models/getoptiontradesorder.md)                                                                                      | :heavy_minus_sign:                                                                                                                                                 | Sort order for returned records. Use asc for oldest first or desc for newest first when supported.                                                                 |                                                                                                                                                                    |
| `limit`                                                                                                                                                            | *Optional[int]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits.                                              | 1000                                                                                                                                                               |
| `sort`                                                                                                                                                             | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Sort field used for ordering. Massive documents this separately from `order`, so enter the provider-supported field name in the text box, for example `timestamp`. |                                                                                                                                                                    |
| `next`                                                                                                                                                             | *Optional[str]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Pagination cursor from the previous response. Omit it on the first request, then send the returned cursor to fetch the next page.                                  |                                                                                                                                                                    |
| `retries`                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                |                                                                                                                                                                    |

### Response

**[models.GetOptionTradesResponse](../../models/getoptiontradesresponse.md)**

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

## get_unusual_activity

Retrieve options unusual activity for a specific underlying symbol (e.g. AAPL, TSLA). Returns options unusual activity data such as unusual volume and block trades. **Required scope:** options:information

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionsUnusualActivity" method="get" path="/v1/options/unusual_activity/{symbol}" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_unusual_activity(symbol="<value>", source=models.Source.DELAYED)

    assert res.options_unusual_activity_response is not None

    # Handle response
    print(res.options_unusual_activity_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `symbol`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Underlying stock symbol (e.g. AAPL, TSLA).                          |
| `source`                                                            | [Optional[models.Source]](../../models/source.md)                   | :heavy_minus_sign:                                                  | Data source. Values are case-insensitive.                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOptionsUnusualActivityResponse](../../models/getoptionsunusualactivityresponse.md)**

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

## get_contracts

Retrieve all option contract symbols (OCC symbols) for a specific underlying ticker and expiration date. Returns the complete list of available call and put contracts with their strike prices.

### Example Usage

<!-- UsageSnippet language="python" operationID="listOptionContracts" method="get" path="/v1/options/{symbol}/contracts/{expiryDate}" example="success" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_contracts(symbol="<value>", expiry_date=date.fromisoformat("2024-11-10"))

    assert res.option_contracts_response is not None

    # Handle response
    print(res.option_contracts_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `symbol`                                                                     | *str*                                                                        | :heavy_check_mark:                                                           | The underlying stock symbol (e.g., AAPL, TSLA, SPY)                          |
| `expiry_date`                                                                | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | The expiration date in YYYY-MM-DD format                                     |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.ListOptionContractsResponse](../../models/listoptioncontractsresponse.md)**

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

## get_expiry_dates

Retrieve all available expiration dates for options contracts of a specific underlying symbol. Returns a list of dates when options for the specified ticker expire.

### Example Usage

<!-- UsageSnippet language="python" operationID="listOptionExpiryDates" method="get" path="/v1/options/{symbol}/expiry-dates" example="success" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.options.get_expiry_dates(symbol="<value>")

    assert res.option_expiry_dates_response is not None

    # Handle response
    print(res.option_expiry_dates_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `symbol`                                                            | *str*                                                               | :heavy_check_mark:                                                  | The underlying stock symbol (e.g., AAPL, TSLA, SPY)                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListOptionExpiryDatesResponse](../../models/listoptionexpirydatesresponse.md)**

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