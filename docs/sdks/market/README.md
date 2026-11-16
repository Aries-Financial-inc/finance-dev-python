# Market

## Overview

### Available Operations

* [get_etb_list](#get_etb_list) - Get Easy-to-Borrow List
* [get_holidays](#get_holidays) - Get Market Holidays
* [get_status](#get_status) - Get Market Status

## get_etb_list

Returns every symbol on today's easy-to-borrow (ETB) list: the complete set of US equities that can be sold short without first locating shares. A symbol on the list is easy to borrow and can be shorted normally; a symbol absent from it is hard to borrow (HTB) and cannot be shorted without a locate. Absence is a positive answer, not missing data. The list is replaced once per trading day before the market opens and does not change intraday. It is not account-scoped — borrowability is a property of the symbol, so every caller gets the same answer. The response can reach a few hundred KB because the borrowable universe runs to thousands of symbols; fetch it once per trading day and check membership locally, or use POST /v1/etb/search when you only care about a handful of symbols.

### Example Usage: not_loaded

<!-- UsageSnippet language="python" operationID="getEtbList" method="get" path="/v1/etb" example="not_loaded" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market.get_etb_list()

    assert res.etb_list_response is not None

    # Handle response
    print(res.etb_list_response)

```
### Example Usage: success

<!-- UsageSnippet language="python" operationID="getEtbList" method="get" path="/v1/etb" example="success" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market.get_etb_list()

    assert res.etb_list_response is not None

    # Handle response
    print(res.etb_list_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetEtbListResponse](../../models/getetblistresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_holidays

Retrieve market holiday schedules showing dates when exchanges are closed for official holidays and early close days.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMarketHolidays" method="get" path="/v1/market/holiday" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market.get_holidays(exchange=models.ExchangeCode.US)

    assert res.market_holiday_response is not None

    # Handle response
    print(res.market_holiday_response)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    | Example                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `exchange`                                                                                                                                     | [models.ExchangeCode](../../models/exchangecode.md)                                                                                            | :heavy_check_mark:                                                                                                                             | exchange code (case-insensitive). Select from the Try it dropdown or use any value from the supported exchange list in the API reference page. | US                                                                                                                                             |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |                                                                                                                                                |

### Response

**[models.GetMarketHolidaysResponse](../../models/getmarketholidaysresponse.md)**

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

## get_status

Retrieve current market status indicating whether exchanges are open, closed, or in pre-market/after-hours trading sessions. Returns 400 when `exchange` is not a supported Finnhub exchange code; the error message lists the supported codes.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMarketStatus" method="get" path="/v1/market/status" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market.get_status(exchange=models.ExchangeCode.US)

    assert res.market_status is not None

    # Handle response
    print(res.market_status)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    | Example                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `exchange`                                                                                                                                     | [models.ExchangeCode](../../models/exchangecode.md)                                                                                            | :heavy_check_mark:                                                                                                                             | exchange code (case-insensitive). Select from the Try it dropdown or use any value from the supported exchange list in the API reference page. | US                                                                                                                                             |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |                                                                                                                                                |

### Response

**[models.GetMarketStatusResponse](../../models/getmarketstatusresponse.md)**

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