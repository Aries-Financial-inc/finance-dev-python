# Analytics

## Overview

### Available Operations

* [get_insights](#get_insights) - Get Analyst Insights
* [get_market_breadth](#get_market_breadth) - Get Market Breadth
* [get_net_inflow](#get_net_inflow) - Get Net Inflow
* [get](#get) - Get Analyst Ratings
* [get_sector_tickers](#get_sector_tickers) - Get Sector Tickers
* [get_sector_wise_change](#get_sector_wise_change) - Get Sector-wise Change
* [get_top_gainers](#get_top_gainers) - Get Top Gaining Stocks
* [get_top_losers](#get_top_losers) - Get Top Losing Stocks
* [get_top_most_active](#get_top_most_active) - Get Most Active Stocks
* [get_options_et_fs_top_volume](#get_options_et_fs_top_volume) - Get Top ETF Options by Volume
* [get_options_stocks_top_gainers](#get_options_stocks_top_gainers) - Get Top Stock Options by Gains
* [get_options_stocks_top_volume](#get_options_stocks_top_volume) - Get Top Stock Options by Volume
* [stock_screener](#stock_screener) - Stock Screener

## get_insights

Retrieve analyst insights and research data. All query parameters are optional. Supports pagination and filtering by symbols, analyst, ratingId, and firm.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalystInsights" method="get" path="/v1/analytics/insights" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_insights()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Zero-based page number. Enter 0 for the first page, 1 for the second page, and so on.                                                                                                    |
| `page_size`                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Number of results per page. Use this to control pagination size in list views. Use this to control page size; default is 10.                                                             |
| `symbols`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Comma-separated ticker symbols, such as AAPL,MSFT. Use this to request or filter multiple companies in one call. (e.g. AAPL,MSFT)                                                        |
| `analyst`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Comma-separated analyst IDs. Use this to limit insight results to specific analysts.                                                                                                     |
| `rating_id`                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Comma-separated rating IDs. Use this to limit insight results to specific rating records.                                                                                                |
| `search_keys_type`                                                                                                                                                                       | [Optional[models.GetAnalystInsightsSearchKeysType]](../../models/getanalystinsightssearchkeystype.md)                                                                                    | :heavy_minus_sign:                                                                                                                                                                       | Tells the API how to interpret the value you send in `searchKeys`. Allowed values:<br/>- `firm_id` — the value is a firm/company internal ID.<br/>- `firm` — the value is the firm/company name. |
| `search_keys`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Search key value (based on searchKeysType)                                                                                                                                               |
| `retries`                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                      |

### Response

**[models.GetAnalystInsightsResponse](../../models/getanalystinsightsresponse.md)**

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

## get_market_breadth

Retrieve market breadth data showing advancers vs decliners

### Example Usage

<!-- UsageSnippet language="python" operationID="getMarketBreadth" method="get" path="/v1/analytics/market-breadth" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_market_breadth()

    assert res.market_breadth_response is not None

    # Handle response
    print(res.market_breadth_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetMarketBreadthResponse](../../models/getmarketbreadthresponse.md)**

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

## get_net_inflow

Retrieve net inflow data for NASDAQ and NYSE

### Example Usage

<!-- UsageSnippet language="python" operationID="getNetInflow" method="get" path="/v1/analytics/net-inflow" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_net_inflow()

    assert res.net_inflow_response is not None

    # Handle response
    print(res.net_inflow_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetNetInflowResponse](../../models/getnetinflowresponse.md)**

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

## get

Retrieve analyst ratings for stocks. All query parameters are optional.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRatings" method="get" path="/v1/analytics/ratings" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get(tickers="AAPL,GOOGL")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     | Example                                                                                                         |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `tickers`                                                                                                       | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Comma-separated list of ticker symbols to filter by                                                             | AAPL,GOOGL                                                                                                      |
| `page`                                                                                                          | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Page number for pagination (0-based)                                                                            |                                                                                                                 |
| `page_size`                                                                                                     | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Number of results per page. Use this to control pagination size in list views.                                  |                                                                                                                 |
| `date_`                                                                                                         | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                    | :heavy_minus_sign:                                                                                              | Filter by specific date (YYYY-MM-DD)                                                                            |                                                                                                                 |
| `date_from`                                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                    | :heavy_minus_sign:                                                                                              | Start date for date range (YYYY-MM-DD)                                                                          |                                                                                                                 |
| `date_to`                                                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                    | :heavy_minus_sign:                                                                                              | End date for date range (YYYY-MM-DD)                                                                            |                                                                                                                 |
| `importance`                                                                                                    | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Minimum importance level to include. Use higher values to filter for more market-moving events or ratings.      |                                                                                                                 |
| `action`                                                                                                        | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Rating action filter. Use it to return only upgrades, downgrades, initiations, or other supported action types. |                                                                                                                 |
| `analyst_id`                                                                                                    | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Comma-separated analyst IDs. Use this to limit insight results to specific analysts. to filter by               |                                                                                                                 |
| `firm_id`                                                                                                       | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Comma-separated firm IDs to filter by                                                                           |                                                                                                                 |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |                                                                                                                 |

### Response

**[models.GetRatingsResponseResponse](../../models/getratingsresponseresponse.md)**

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

## get_sector_tickers

Retrieves all stock symbols within a specified sector, sorted by trading volume.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSectorTickers" method="get" path="/v1/equity/sector-tickers" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_sector_tickers(sector=models.Sector.TECHNOLOGY)

    assert res.symbol_details is not None

    # Handle response
    print(res.symbol_details)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sector`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [models.Sector](../../models/sector.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Which industry sector to list tickers for. Use the exact uppercase value (including spaces) — these match the values returned by [GET /v1/equity/sector-wise-change](/api-reference/analytics/equity-sector-wise-change).<br/>- `TECHNOLOGY` — software, hardware, semiconductors<br/>- `HEALTHCARE` — pharma, biotech, medical devices, providers<br/>- `FINANCIAL SERVICES` — banks, insurance, asset managers<br/>- `CONSUMER CYCLICAL` — discretionary spending (autos, retail, travel)<br/>- `CONSUMER DEFENSIVE` — staples (food, household goods, drugstores)<br/>- `INDUSTRIALS` — manufacturing, transport, defense, machinery<br/>- `ENERGY` — oil & gas, renewable energy<br/>- `UTILITIES` — power, water, gas distribution<br/>- `BASIC MATERIALS` — mining, chemicals, paper, metals<br/>- `COMMUNICATION SERVICES` — telecom, media, internet platforms<br/>- `REAL ESTATE` — REITs and real-estate operators<br/>- `OTHER` — uncategorized<br/>- `NONE` — no sector classification | TECHNOLOGY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### Response

**[models.GetSectorTickersResponse](../../models/getsectortickersresponse.md)**

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

## get_sector_wise_change

Retrieves the average percentage change for all available sectors, sorted by change. Use limit=all to return all sectors.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSectorWiseChange" method="get" path="/v1/equity/sector-wise-change" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_sector_wise_change(limit="15", size="15")

    assert res.sector_avg_changes is not None

    # Handle response
    print(res.sector_avg_changes)

```

### Parameters

| Parameter                                                                                                                                                                                       | Type                                                                                                                                                                                            | Required                                                                                                                                                                                        | Description                                                                                                                                                                                     | Example                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Maximum number of sectors to return. Two formats are accepted:<br/>- An integer like `5`, `10`, `15` to cap the list (default `15`).<br/>- The literal string `all` to return every sector with no cap. | 15                                                                                                                                                                                              |
| `size`                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Alias for limit. Ignored when limit is supplied.                                                                                                                                                | 15                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                             |                                                                                                                                                                                                 |

### Response

**[models.GetSectorWiseChangeResponse](../../models/getsectorwisechangeresponse.md)**

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

## get_top_gainers

Retrieves stocks with the highest positive percentage changes, sorted by change percentage in descending order.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTopGainers" method="get" path="/v1/equity/top-gainers" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_top_gainers(limit=10, size=10)

    assert res.symbol_details is not None

    # Handle response
    print(res.symbol_details)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                      | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits. (optional, default 10) |
| `size`                                                                                                                                       | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Alias for limit. Ignored when limit is supplied.                                                                                             |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[models.GetTopGainersResponse](../../models/gettopgainersresponse.md)**

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

## get_top_losers

Retrieves stocks with the largest negative percentage changes, sorted by change percentage in ascending order.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTopLosers" method="get" path="/v1/equity/top-losers" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_top_losers(limit=10, size=10)

    assert res.symbol_details is not None

    # Handle response
    print(res.symbol_details)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                      | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits. (optional, default 10) |
| `size`                                                                                                                                       | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Alias for limit. Ignored when limit is supplied.                                                                                             |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[models.GetTopLosersResponse](../../models/gettoplosersresponse.md)**

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

## get_top_most_active

Retrieves stocks sorted by trading volume in descending order.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTopMostActive" method="get" path="/v1/equity/top-most-active" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_top_most_active(limit=10, size=10)

    assert res.symbol_details is not None

    # Handle response
    print(res.symbol_details)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                      | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits. (optional, default 10) |
| `size`                                                                                                                                       | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Alias for limit. Ignored when limit is supplied.                                                                                             |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[models.GetTopMostActiveResponse](../../models/gettopmostactiveresponse.md)**

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

## get_options_et_fs_top_volume

Retrieve ETF options with the highest trading volume showing the most actively traded contracts across all ETFs.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionsETFsTopVolume" method="get" path="/v1/options/etfs/top-volume" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_options_et_fs_top_volume(size=10)

    assert res.options_screener_items is not None

    # Handle response
    print(res.options_screener_items)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `size`                                                                                                                                       | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits. (optional, default 10) |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[models.GetOptionsETFsTopVolumeResponse](../../models/getoptionsetfstopvolumeresponse.md)**

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

## get_options_stocks_top_gainers

Retrieve stock options with the largest percentage gains showing the best performing options contracts.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionsStocksTopGainers" method="get" path="/v1/options/stocks/top-gainers" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_options_stocks_top_gainers(size=10)

    assert res.options_screener_items is not None

    # Handle response
    print(res.options_screener_items)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `size`                                                                                                                                       | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits. (optional, default 10) |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[models.GetOptionsStocksTopGainersResponse](../../models/getoptionsstockstopgainersresponse.md)**

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

## get_options_stocks_top_volume

Retrieve stock options with the highest trading volume identifying the most actively traded equity options contracts.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionsStocksTopVolume" method="get" path="/v1/options/stocks/top-volume" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_options_stocks_top_volume(size=10)

    assert res.options_screener_items is not None

    # Handle response
    print(res.options_screener_items)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `size`                                                                                                                                       | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits. (optional, default 10) |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[models.GetOptionsStocksTopVolumeResponse](../../models/getoptionsstockstopvolumeresponse.md)**

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

## stock_screener

Screen securities by sending a JSON body with operator and clauses (and optional groups). At least one clause or group is required. Query params: page_size, order_column, order_direction, primary_only. **Required scope:** analytics:information

### Example Usage: flat

<!-- UsageSnippet language="python" operationID="stockScreener" method="post" path="/v1/stock/screener" example="flat" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.stock_screener(stock_screener_request={
        "clauses": [],
        "operator": models.StockScreenerRequestOperator1.AND,
    }, order_direction=models.SortOrderEnum.ASC)

    assert res.stock_screener_response is not None

    # Handle response
    print(res.stock_screener_response)

```
### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="stockScreener" method="post" path="/v1/stock/screener" example="flat_message" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.stock_screener(stock_screener_request={
        "clauses": [],
        "operator": models.StockScreenerRequestOperator1.AND,
    }, order_direction=models.SortOrderEnum.ASC)

    assert res.stock_screener_response is not None

    # Handle response
    print(res.stock_screener_response)

```
### Example Usage: flat_string

<!-- UsageSnippet language="python" operationID="stockScreener" method="post" path="/v1/stock/screener" example="flat_string" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.stock_screener(stock_screener_request={
        "clauses": [],
        "operator": models.StockScreenerRequestOperator1.AND,
    }, order_direction=models.SortOrderEnum.ASC)

    assert res.stock_screener_response is not None

    # Handle response
    print(res.stock_screener_response)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="stockScreener" method="post" path="/v1/stock/screener" example="flat_with_codes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.stock_screener(stock_screener_request={
        "groups": [],
        "operator": models.StockScreenerRequestOperator2.NOT,
    }, order_direction=models.SortOrderEnum.ASC)

    assert res.stock_screener_response is not None

    # Handle response
    print(res.stock_screener_response)

```
### Example Usage: marketCapAndPE

<!-- UsageSnippet language="python" operationID="stockScreener" method="post" path="/v1/stock/screener" example="marketCapAndPE" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.stock_screener(stock_screener_request={
        "clauses": [
            {
                "field": "marketcap",
                "operator": models.ScreenClauseOperator.GTE,
                "value": "1000000000",
            },
            {
                "field": "pricetoearnings",
                "operator": models.ScreenClauseOperator.GTE,
                "value": "5",
            },
            {
                "field": "pricetoearnings",
                "operator": models.ScreenClauseOperator.LTE,
                "value": "25",
            },
        ],
        "operator": models.StockScreenerRequestOperator1.AND,
    }, order_direction=models.SortOrderEnum.ASC)

    assert res.stock_screener_response is not None

    # Handle response
    print(res.stock_screener_response)

```
### Example Usage: nested

<!-- UsageSnippet language="python" operationID="stockScreener" method="post" path="/v1/stock/screener" example="nested" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.stock_screener(stock_screener_request={
        "groups": [],
        "operator": models.StockScreenerRequestOperator2.NOT,
    }, order_direction=models.SortOrderEnum.ASC)

    assert res.stock_screener_response is not None

    # Handle response
    print(res.stock_screener_response)

```
### Example Usage: nested_bad_request

<!-- UsageSnippet language="python" operationID="stockScreener" method="post" path="/v1/stock/screener" example="nested_bad_request" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.stock_screener(stock_screener_request={
        "groups": [],
        "operator": models.StockScreenerRequestOperator2.NOT,
    }, order_direction=models.SortOrderEnum.ASC)

    assert res.stock_screener_response is not None

    # Handle response
    print(res.stock_screener_response)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="stockScreener" method="post" path="/v1/stock/screener" example="nested_error_object" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.stock_screener(stock_screener_request={
        "groups": [],
        "operator": models.StockScreenerRequestOperator2.NOT,
    }, order_direction=models.SortOrderEnum.ASC)

    assert res.stock_screener_response is not None

    # Handle response
    print(res.stock_screener_response)

```
### Example Usage: nested_shared_http_error

<!-- UsageSnippet language="python" operationID="stockScreener" method="post" path="/v1/stock/screener" example="nested_shared_http_error" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.stock_screener(stock_screener_request={
        "groups": [],
        "operator": models.StockScreenerRequestOperator2.NOT,
    }, order_direction=models.SortOrderEnum.ASC)

    assert res.stock_screener_response is not None

    # Handle response
    print(res.stock_screener_response)

```
### Example Usage: roeAndEps

<!-- UsageSnippet language="python" operationID="stockScreener" method="post" path="/v1/stock/screener" example="roeAndEps" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.stock_screener(stock_screener_request={
        "clauses": [
            {
                "field": "roe",
                "operator": models.ScreenClauseOperator.GTE,
                "value": "0.15",
            },
            {
                "field": "dilutedeps",
                "operator": models.ScreenClauseOperator.GTE,
                "value": "1",
            },
        ],
        "operator": models.StockScreenerRequestOperator1.AND,
    }, order_direction=models.SortOrderEnum.ASC)

    assert res.stock_screener_response is not None

    # Handle response
    print(res.stock_screener_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `stock_screener_request`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [models.StockScreenerRequest](../../models/stockscreenerrequest.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Screener request with operator (AND, OR, or NOT), clauses (field, operator, value), and optional groups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Number of results to return per page. Use smaller values (10–50) for UI screens, larger (100–500) for batch exports. Defaults to the upstream provider's default.                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `order_column`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Which data column to sort the screened results by. Accepts any column the upstream screener exposes — not a fixed enum on our side. Common columns:<br/>- `marketcap` — market capitalization.<br/>- `pricetoearnings` — trailing P/E ratio.<br/>- `pricetobook` — price-to-book ratio.<br/>- `roe` — return on equity.<br/>- `volume` — average daily volume.<br/>- `open_price` / `close_price` — most recent open / close.<br/>- `dilutedeps` — diluted earnings per share (TTM).<br/>- `cashandequivalents` — cash + cash equivalents on the balance sheet.<br/><br/>Pair with `order_direction` (`asc` / `desc`). |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `order_direction`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Direction to sort `order_column` in:<br/>- `asc` — ascending (smallest first).<br/>- `desc` — descending (largest first).                                                                                                                                                                                                                                                                                                                                                                                                                                                      | asc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `primary_only`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | When `true`, return only the primary listing for each company (e.g. NYSE for a U.S. dual-listed stock) instead of every listing. Defaults to `false`.                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### Response

**[models.StockScreenerResponseResponse](../../models/stockscreenerresponseresponse.md)**

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