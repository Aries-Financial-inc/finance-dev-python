# Etf

## Overview

### Available Operations

* [get_holdings](#get_holdings) - Get ETF Holdings
* [get_profile](#get_profile) - Get ETF Profile
* [get_sector](#get_sector) - Get ETF Sector Allocation

## get_holdings

Retrieve detailed ETF holdings showing constituent securities, allocation percentages, share quantities, and market values.

If `skip` cannot be parsed as a signed 64-bit integer, returns 400 Bad Request with error code `INVALID_PARAMETER` and message `invalid skip parameter`.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEtfHoldings" method="get" path="/v1/etf/holdings" example="default" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.etf.get_holdings(date_=date.fromisoformat("2024-12-01"))

    assert res.etf_holdings_response is not None

    # Handle response
    print(res.etf_holdings_response)

```

### Parameters

| Parameter                                                                                                                                                                                     | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   | Example                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | ETF ticker to filter by. Send the plain uppercase symbol (e.g. `SPY`). Provide either `symbol` or `isin`.                                                                                     |                                                                                                                                                                                               |
| `isin`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | ISIN identifier — the 12-character International Securities Identification Number for the instrument (e.g. `US0378331005` for Apple). Provide this instead of `symbol` when you have an ISIN. |                                                                                                                                                                                               |
| `skip`                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | (Optional) Number of records to skip for pagination                                                                                                                                           |                                                                                                                                                                                               |
| `date_`                                                                                                                                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                            | (Optional) Date for historical holdings (YYYY-MM-DD)                                                                                                                                          | 2024-12-01                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                           |                                                                                                                                                                                               |

### Response

**[models.GetEtfHoldingsResponse](../../models/getetfholdingsresponse.md)**

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

## get_profile

Retrieve comprehensive ETF information including fund name, description, expense ratio, assets under management, and tracking methodology.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEtfProfile" method="get" path="/v1/etf/profile" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.etf.get_profile(symbol="SPY")

    assert res.etf_profile_response is not None

    # Handle response
    print(res.etf_profile_response)

```

### Parameters

| Parameter                                                                                                                                                                                     | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   | Example                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                                                                      | *str*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | ETF ticker symbol (e.g. SPY, QQQ, VTI)                                                                                                                                                        | SPY                                                                                                                                                                                           |
| `isin`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | ISIN identifier — the 12-character International Securities Identification Number for the instrument (e.g. `US0378331005` for Apple). Provide this instead of `symbol` when you have an ISIN. |                                                                                                                                                                                               |
| `retries`                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                           |                                                                                                                                                                                               |

### Response

**[models.GetEtfProfileResponse](../../models/getetfprofileresponse.md)**

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

## get_sector

Retrieve ETF sector allocation breakdown showing percentage exposure to different industries such as technology, healthcare, and financials.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEtfSectorAllocation" method="get" path="/v1/etf/sector" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.etf.get_sector(symbol="<value>")

    assert res.etf_sector_allocation_response is not None

    # Handle response
    print(res.etf_sector_allocation_response)

```

### Parameters

| Parameter                                                                                                                                                                                     | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                                                                      | *str*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | ETF ticker to query. Send the plain uppercase symbol, e.g. `SPY`, `QQQ`, `IWM`.                                                                                                               |
| `isin`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | ISIN identifier — the 12-character International Securities Identification Number for the instrument (e.g. `US0378331005` for Apple). Provide this instead of `symbol` when you have an ISIN. |
| `retries`                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                           |

### Response

**[models.GetEtfSectorAllocationResponse](../../models/getetfsectorallocationresponse.md)**

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