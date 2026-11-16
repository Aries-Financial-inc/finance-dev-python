# Market.Equities

## Overview

### Available Operations

* [get_details](#get_details) - Get equity details

## get_details

Batch equity details from an internal cache with an automatic fallback when cached quotes are unavailable. Response includes `data` with per-symbol fields (camelCase: `bidPrice`, `openPrice`, `totalVolume`, etc.); see `EquityDetailsDTO` and `GetEquityDetailsResponse`. At least one symbol is required.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEquityDetails" method="get" path="/v1/marketdata/equities/details" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market.equities.get_details(symbols="AAPL,MSFT")

    assert res.get_equity_details_response is not None

    # Handle response
    print(res.get_equity_details_response)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          | Example                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbols`                                                                                                                                            | *str*                                                                                                                                                | :heavy_check_mark:                                                                                                                                   | One or more uppercase ticker symbols, separated by commas (e.g. `AAPL,MSFT,GOOGL`). Send at least one. The response order matches the request order. | AAPL,MSFT                                                                                                                                            |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |                                                                                                                                                      |

### Response

**[models.GetEquityDetailsResponseResponse](../../models/getequitydetailsresponseresponse.md)**

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