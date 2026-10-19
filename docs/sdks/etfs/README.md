# Etfs

## Overview

### Available Operations

* [get_country_allocation](#get_country_allocation) - Get ETF Country Allocation

## get_country_allocation

Retrieve ETF geographic allocation showing percentage exposure to different countries and regions for assessing international diversification.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEtfCountryAllocation" method="get" path="/v1/etf/country" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.etfs.get_country_allocation(symbol="<value>")

    assert res.etf_country_allocation_response is not None

    # Handle response
    print(res.etf_country_allocation_response)

```

### Parameters

| Parameter                                                                                                                                                                                     | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                                                                      | *str*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | ETF ticker to query. Send the plain uppercase symbol, e.g. `SPY`, `QQQ`, `IWM`.                                                                                                               |
| `isin`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | ISIN identifier — the 12-character International Securities Identification Number for the instrument (e.g. `US0378331005` for Apple). Provide this instead of `symbol` when you have an ISIN. |
| `retries`                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                           |

### Response

**[models.GetEtfCountryAllocationResponse](../../models/getetfcountryallocationresponse.md)**

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