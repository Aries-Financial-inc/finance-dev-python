# StockEstimates

## Overview

### Available Operations

* [get_earnings](#get_earnings) - Get Earnings Surprises
* [get_ebit_estimate](#get_ebit_estimate) - Get EBIT Estimates
* [get_ebitda_estimate](#get_ebitda_estimate) - Get EBITDA Estimates
* [get_eps_estimate](#get_eps_estimate) - Get EPS Estimates
* [get_price_target](#get_price_target) - Get Analyst Price Targets
* [get_revenue_estimate](#get_revenue_estimate) - Get Revenue Estimates
* [get_upgrade_downgrade](#get_upgrade_downgrade) - Get Analyst Upgrades & Downgrades

## get_earnings

Retrieve historical earnings surprises comparing actual reported earnings to analyst estimates with surprise percentages.

If `limit` cannot be parsed as a signed 64-bit integer, returns 400 Bad Request with error code `INVALID_PARAMETER` and message `invalid limit parameter`.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEarningsSurprises" method="get" path="/v1/stock/earnings" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_estimates.get_earnings(symbol="AAPL")

    assert res.earnings_surprises_response is not None

    # Handle response
    print(res.earnings_surprises_response)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                            | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`, `TSLA`. | AAPL                                                                                                                                |
| `limit`                                                                                                                             | *Optional[int]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | (Optional) Number of results to return                                                                                              |                                                                                                                                     |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[models.GetEarningsSurprisesResponse](../../models/getearningssurprisesresponse.md)**

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

## get_ebit_estimate

Retrieve analyst EBIT (Earnings Before Interest and Taxes) estimates showing projected operating profitability.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEbitEstimates" method="get" path="/v1/stock/ebit-estimate" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_estimates.get_ebit_estimate(symbol="AAPL", freq=models.ReportingFrequency.QUARTERLY)

    assert res.ebit_estimates_response is not None

    # Handle response
    print(res.ebit_estimates_response)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                            | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`, `TSLA`. | AAPL                                                                                                                                |
| `freq`                                                                                                                              | [Optional[models.ReportingFrequency]](../../models/reportingfrequency.md)                                                           | :heavy_minus_sign:                                                                                                                  | (Optional) Frequency: annual, quarterly                                                                                             | quarterly                                                                                                                           |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[models.GetEbitEstimatesResponse](../../models/getebitestimatesresponse.md)**

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

## get_ebitda_estimate

Retrieve analyst EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization) estimates for profitability forecasting.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEbitdaEstimates" method="get" path="/v1/stock/ebitda-estimate" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_estimates.get_ebitda_estimate(symbol="AAPL", freq=models.ReportingFrequency.QUARTERLY)

    assert res.ebitda_estimates_response is not None

    # Handle response
    print(res.ebitda_estimates_response)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                            | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`, `TSLA`. | AAPL                                                                                                                                |
| `freq`                                                                                                                              | [Optional[models.ReportingFrequency]](../../models/reportingfrequency.md)                                                           | :heavy_minus_sign:                                                                                                                  | (Optional) Frequency: annual, quarterly                                                                                             | quarterly                                                                                                                           |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[models.GetEbitdaEstimatesResponse](../../models/getebitdaestimatesresponse.md)**

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

## get_eps_estimate

Retrieve analyst earnings per share (EPS) estimates including consensus forecasts, estimate ranges, and earnings growth projections.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEpsEstimates" method="get" path="/v1/stock/eps-estimate" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_estimates.get_eps_estimate(symbol="AAPL", freq=models.ReportingFrequency.QUARTERLY)

    assert res.eps_estimates_response is not None

    # Handle response
    print(res.eps_estimates_response)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                            | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`, `TSLA`. | AAPL                                                                                                                                |
| `freq`                                                                                                                              | [Optional[models.ReportingFrequency]](../../models/reportingfrequency.md)                                                           | :heavy_minus_sign:                                                                                                                  | (Optional) Frequency: annual, quarterly                                                                                             | quarterly                                                                                                                           |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[models.GetEpsEstimatesResponse](../../models/getepsestimatesresponse.md)**

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

## get_price_target

Retrieve analyst price targets including consensus estimates, high/low targets, and individual analyst projections for stock valuation.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPriceTarget" method="get" path="/v1/stock/price-target" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_estimates.get_price_target(symbol="AAPL")

    assert res.price_target_response is not None

    # Handle response
    print(res.price_target_response)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                            | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`, `TSLA`. | AAPL                                                                                                                                |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[models.GetPriceTargetResponse](../../models/getpricetargetresponse.md)**

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

## get_revenue_estimate

Retrieve analyst revenue estimates including quarterly and annual projections with consensus forecasts and estimate revisions.

### Example Usage

<!-- UsageSnippet language="python" operationID="getRevenueEstimates" method="get" path="/v1/stock/revenue-estimate" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_estimates.get_revenue_estimate(symbol="AAPL", freq=models.ReportingFrequency.QUARTERLY)

    assert res.revenue_estimates_response is not None

    # Handle response
    print(res.revenue_estimates_response)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                            | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`, `TSLA`. | AAPL                                                                                                                                |
| `freq`                                                                                                                              | [Optional[models.ReportingFrequency]](../../models/reportingfrequency.md)                                                           | :heavy_minus_sign:                                                                                                                  | (Optional) Frequency: annual, quarterly                                                                                             | quarterly                                                                                                                           |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[models.GetRevenueEstimatesResponse](../../models/getrevenueestimatesresponse.md)**

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

## get_upgrade_downgrade

Retrieve analyst rating changes including upgrades, downgrades, and reiterations from investment banks and research firms.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUpgradesDowngrades" method="get" path="/v1/stock/upgrade-downgrade" example="default" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_estimates.get_upgrade_downgrade(from_=date.fromisoformat("2024-01-01"), to=date.fromisoformat("2024-12-31"))

    assert res.upgrades_downgrades_response is not None

    # Handle response
    print(res.upgrades_downgrades_response)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   | Example                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                      | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | Stock ticker to filter by. Send the plain uppercase symbol (e.g. `AAPL`). Omit to return data across all symbols.             |                                                                                                                               |
| `from_`                                                                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                  | :heavy_minus_sign:                                                                                                            | Start of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-01-01`). Omit to read from the earliest available data. | 2024-01-01                                                                                                                    |
| `to`                                                                                                                          | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                  | :heavy_minus_sign:                                                                                                            | End of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-12-31`). Omit to read up to today.                        | 2024-12-31                                                                                                                    |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |                                                                                                                               |

### Response

**[models.GetUpgradesDowngradesResponse](../../models/getupgradesdowngradesresponse.md)**

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