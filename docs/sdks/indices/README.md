# Indices

## Overview

### Available Operations

* [get_bar](#get_bar) - Get Index Bar Data
* [get_bars](#get_bars) - Get Index Bars Data
* [get_by_group](#get_by_group) - Get Indices By Group
* [get_chart_bars](#get_chart_bars) - Get Index Chart Data
* [get_groups](#get_groups) - Get Index Groups
* [list](#list) - Get Index List
* [get_realtime_values](#get_realtime_values) - Get Realtime Indices Values
* [search](#search) - Search Indices

## get_bar

Retrieve OHLC (Open, High, Low, Close) bar data for indices across various timeframes for technical analysis.

### Example Usage

<!-- UsageSnippet language="python" operationID="getIndexBar" method="get" path="/v1/indices/bar" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.indices.get_bar(identifier="SPX.IND_CBOM", end_time="12/22/2025 10:30 am", identifier_type=models.IndicesIdentifierType.SYMBOL, precision=models.GetIndexBarPrecision.MINUTES, period=1)

    assert res.index_bar_response is not None

    # Handle response
    print(res.index_bar_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                           | Example                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifier`                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                    | Index identifier to query. For `Symbol`-type identifiers, use the full `<SYMBOL>.<GROUP>` form (e.g. `SPX.IND_CBOM` for the S&P 500 in the CBOE CSMI group). For other identifier types (CUSIP, ISIN, etc.), set `identifierType` accordingly.                                                        | SPX.IND_CBOM                                                                                                                                                                                                                                                                                          |
| `end_time`                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                    | End time for the bar window. Format: `MM/DD/YYYY hh:mm am/pm` in the index's native timezone (e.g. `12/22/2025 10:30 am`).                                                                                                                                                                            | 12/22/2025 10:30 am                                                                                                                                                                                                                                                                                   |
| `identifier_type`                                                                                                                                                                                                                                                                                     | [Optional[models.IndicesIdentifierType]](../../models/indicesidentifiertype.md)                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                    | How to interpret the value you sent in `identifier`. Defaults to `Symbol`. See `IndicesIdentifierType` for the full set of accepted values.                                                                                                                                                           | Symbol                                                                                                                                                                                                                                                                                                |
| `precision`                                                                                                                                                                                                                                                                                           | [Optional[models.GetIndexBarPrecision]](../../models/getindexbarprecision.md)                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                    | How long each bar covers. Pair with `period` to set the exact size (e.g. `precision=Minutes`, `period=5` = 5-minute bars). Allowed values:<br/>- `Minutes` — minute bars (combine with `period` for 1, 5, 15, 30-minute candles).<br/>- `Hours` — hour bars (combine with `period` for 1, 2, 4-hour candles). | Minutes                                                                                                                                                                                                                                                                                               |
| `period`                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                    | Multiplier on `precision` to set the bar size. Defaults to `1`. Examples: `precision=Minutes` + `period=5` = 5-minute bars; `precision=Hours` + `period=4` = 4-hour bars.                                                                                                                             | 1                                                                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                       |

### Response

**[models.GetIndexBarResponse](../../models/getindexbarresponse.md)**

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

## get_bars

Retrieve OHLC (Open, High, Low, Close) bar data for multiple market indices in a single request. Returns historical price bars with volume data for batch analysis of index movements.

### Example Usage

<!-- UsageSnippet language="python" operationID="getIndexBars" method="get" path="/v1/indices/bars" example="success" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.indices.get_bars(identifier="SPX.IND_CBOM", start_time="12/22/2025 9:30 am", end_time="12/22/2025 4:00 pm", identifier_type=models.IndicesIdentifierType.SYMBOL, precision=models.GetIndexBarsPrecision.MINUTES)

    assert res.index_bars_response is not None

    # Handle response
    print(res.index_bars_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                           | Example                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifier`                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                    | Index identifier to query. For `Symbol`-type identifiers, use the full `<SYMBOL>.<GROUP>` form (e.g. `SPX.IND_CBOM`). For other identifier types, set `identifierType` accordingly.                                                                                                                   | SPX.IND_CBOM                                                                                                                                                                                                                                                                                          |
| `start_time`                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                    | Start of the bars window. Format: `MM/DD/YYYY hh:mm am/pm` in the index's native timezone (e.g. `12/22/2025 9:30 am`).                                                                                                                                                                                | 12/22/2025 9:30 am                                                                                                                                                                                                                                                                                    |
| `end_time`                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                    | End of the bars window. Format: `MM/DD/YYYY hh:mm am/pm` in the index's native timezone (e.g. `12/22/2025 4:00 pm`).                                                                                                                                                                                  | 12/22/2025 4:00 pm                                                                                                                                                                                                                                                                                    |
| `identifier_type`                                                                                                                                                                                                                                                                                     | [Optional[models.IndicesIdentifierType]](../../models/indicesidentifiertype.md)                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                    | How to interpret the value you sent in `identifier`. Defaults to `Symbol`. See `IndicesIdentifierType` for the full set of accepted values.                                                                                                                                                           | Symbol                                                                                                                                                                                                                                                                                                |
| `precision`                                                                                                                                                                                                                                                                                           | [Optional[models.GetIndexBarsPrecision]](../../models/getindexbarsprecision.md)                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                    | How long each bar covers. Pair with `period` to set the exact size (e.g. `precision=Minutes`, `period=5` = 5-minute bars). Allowed values:<br/>- `Minutes` — minute bars (combine with `period` for 1, 5, 15, 30-minute candles).<br/>- `Hours` — hour bars (combine with `period` for 1, 2, 4-hour candles). | Minutes                                                                                                                                                                                                                                                                                               |
| `period`                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                    | Multiplier on `precision` to set the bar size. Defaults to `1`. Examples: `precision=Minutes` + `period=5` = 5-minute bars; `precision=Hours` + `period=4` = 4-hour bars.                                                                                                                             |                                                                                                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                       |

### Response

**[models.GetIndexBarsResponse](../../models/getindexbarsresponse.md)**

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

## get_by_group

Retrieve all market indices belonging to a specific group category. Returns detailed information about indices within groups like Technology, Healthcare, International, or Custom portfolios.

### Example Usage

<!-- UsageSnippet language="python" operationID="listIndicesByGroup" method="get" path="/v1/indices/by-group" example="success" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.indices.get_by_group(index_group="IND_CBOM")

    assert res.indices_by_group_response is not None

    # Handle response
    print(res.indices_by_group_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                           | Example                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `index_group`                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                    | Index group to retrieve recently-updated members from. Use [GET /v1/indices/groups](/api-reference/supplemental/indices-groups) to discover the live list — see `IndexGroup` for the current published set with plain-English labels. | IND_CBOM                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                   |                                                                                                                                                                                                                                       |

### Response

**[models.ListIndicesByGroupResponse](../../models/listindicesbygroupresponse.md)**

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

## get_chart_bars

Retrieve historical chart data for indices including price history, volume, and returns for creating index performance charts.

### Example Usage

<!-- UsageSnippet language="python" operationID="getIndexChartBars" method="get" path="/v1/indices/chart-bars" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.indices.get_chart_bars(identifier="SPX.IND_CBOM", start_time="12/15/2025 9:00 am", end_time="12/15/2025 9:30 am", identifier_type=models.IndicesIdentifierType.SYMBOL, precision=models.GetIndexChartBarsPrecision.MINUTE, period=15, include_extended=False)

    assert res.index_chart_bars_response is not None

    # Handle response
    print(res.index_chart_bars_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifier`                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                     | Index identifier to query. For `Symbol`-type identifiers, use the full `<SYMBOL>.<GROUP>` form (e.g. `SPX.IND_CBOM`). For other identifier types, set `identifierType` accordingly.                                                    | SPX.IND_CBOM                                                                                                                                                                                                                           |
| `start_time`                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                     | Start of the chart range, inclusive. Format: `MM/DD/YYYY hh:mm am/pm` in the index's native timezone (e.g. `12/15/2025 9:00 am`).                                                                                                      | 12/15/2025 9:00 am                                                                                                                                                                                                                     |
| `end_time`                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                     | End of the chart range, inclusive. Format: `MM/DD/YYYY hh:mm am/pm` in the index's native timezone (e.g. `12/15/2025 9:30 am`).                                                                                                        | 12/15/2025 9:30 am                                                                                                                                                                                                                     |
| `identifier_type`                                                                                                                                                                                                                      | [Optional[models.IndicesIdentifierType]](../../models/indicesidentifiertype.md)                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                     | How to interpret the value you sent in `identifier`. Defaults to `Symbol`. See `IndicesIdentifierType` for the full set of accepted values.                                                                                            | Symbol                                                                                                                                                                                                                                 |
| `precision`                                                                                                                                                                                                                            | [Optional[models.GetIndexChartBarsPrecision]](../../models/getindexchartbarsprecision.md)                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                     | How long each chart bar covers. Pair with `period` to set the exact size. Note the singular form (different from `/v1/indices/bar` and `/v1/indices/bars`). Allowed values:<br/>- `Minute` — minute bars (intraday).<br/>- `Hour` — hour bars. | Minute                                                                                                                                                                                                                                 |
| `period`                                                                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                     | Multiplier on `precision` to set the bar size. Defaults to `1`. Example: `precision=Minute` + `period=15` = 15-minute bars.                                                                                                            | 15                                                                                                                                                                                                                                     |
| `adjustment_method`                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                     | How to adjust historical prices for corporate actions like dividends and splits. Pass the literal value supported by the upstream data provider. Omit to leave prices unadjusted.                                                      |                                                                                                                                                                                                                                        |
| `include_extended`                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                     | Include pre-market and after-hours sessions in the returned chart bars. Defaults to `false` (regular hours only). Set `true` when you want a continuous extended-session chart.                                                        |                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                    |                                                                                                                                                                                                                                        |

### Response

**[models.GetIndexChartBarsResponse](../../models/getindexchartbarsresponse.md)**

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

## get_groups

List all index groups (publishers / index families) currently available. The response is the canonical source — fetch this and cache it locally to populate dropdown menus that drive other indices endpoints, instead of hard-coding the group list in your app.

### Example Usage

<!-- UsageSnippet language="python" operationID="listIndexGroups" method="get" path="/v1/indices/groups" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.indices.get_groups()

    assert res.index_groups_response is not None

    # Handle response
    print(res.index_groups_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListIndexGroupsResponse](../../models/listindexgroupsresponse.md)**

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

## list

Retrieve comprehensive list of available indices including major market indices, sector indices, and international benchmarks.

### Example Usage

<!-- UsageSnippet language="python" operationID="listIndices" method="get" path="/v1/indices/list" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.indices.list(index_group="IND_CBOM", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                      | Example                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `index_group`                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                               | Index group whose members you want to list (paginated). Use [GET /v1/indices/groups](/api-reference/supplemental/indices-groups) to discover the live list of groups — see `IndexGroup` for the current published set with plain-English labels. | IND_CBOM                                                                                                                                                                                                                                         |
| `page_size`                                                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Number of results per page. Use this to control pagination size in list views. (default: 100, max: 1000)                                                                                                                                         | 100                                                                                                                                                                                                                                              |
| `next_page`                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                               | Pagination token for the next page. Omit it on the first request, then send the returned token to continue paging.                                                                                                                               |                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                                                                              |                                                                                                                                                                                                                                                  |

### Response

**[models.ListIndicesResponse](../../models/listindicesresponse.md)**

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

## get_realtime_values

Retrieve real-time values for multiple market indices simultaneously. Returns current index levels, percentage changes, and last update timestamps for a batch of indices in a single request.

### Example Usage

<!-- UsageSnippet language="python" operationID="getIndexRealtimeValues" method="get" path="/v1/indices/realtime/values" example="success" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.indices.get_realtime_values(identifiers="<value>", identifier_type=models.IndicesIdentifierType.SYMBOL)

    assert res.indices_realtime_values_response is not None

    # Handle response
    print(res.indices_realtime_values_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifiers`                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                  | One or more index identifiers to fetch real-time values for, comma-separated. For `Symbol`-type identifiers, use the full `<SYMBOL>.<GROUP>` form (e.g. `SPX.IND_CBOM,COMP.IND_CBOM,DJI.IND_DJI`). All identifiers in one request must be the same type (set via `identifierType`). |                                                                                                                                                                                                                                                                                     |
| `identifier_type`                                                                                                                                                                                                                                                                   | [Optional[models.IndicesIdentifierType]](../../models/indicesidentifiertype.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                  | How to interpret each value in `identifiers`. Defaults to `Symbol`. See `IndicesIdentifierType` for the full set of accepted values. All identifiers in one request must be the same type.                                                                                          | Symbol                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                     |

### Response

**[models.GetIndexRealtimeValuesResponse](../../models/getindexrealtimevaluesresponse.md)**

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

## search

Search for market indices by name, symbol, or keyword to find specific benchmark indices and sector trackers.

### Example Usage

<!-- UsageSnippet language="python" operationID="searchIndices" method="get" path="/v1/indices/search" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.indices.search(index_name="S&P 500")

    assert res.index_search_response is not None

    # Handle response
    print(res.index_search_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                | Type                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                 | Description                                                                                                                                                                                                              | Example                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `index_name`                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                       | Full or partial index name to search for. Case-insensitive substring match against the index display name (e.g. `S&P 500`, `Dow`, `NASDAQ`). Returns matching indices with their `symbol`, `indexGroup`, and `currency`. | S&P 500                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                      |                                                                                                                                                                                                                          |

### Response

**[models.SearchIndicesResponse](../../models/searchindicesresponse.md)**

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