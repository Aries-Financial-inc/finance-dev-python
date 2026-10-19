# Signals

## Overview

### Available Operations

* [get_bull_bear](#get_bull_bear) - Get Bull & Bear Analysis

## get_bull_bear

Retrieve bullish and bearish investment cases including fundamental arguments, technical signals, and analyst opinions for balanced perspective.

### Example Usage

<!-- UsageSnippet language="python" operationID="getBullBearAnalysis" method="get" path="/v1/signals/bull-bear" example="success" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.signals.get_bull_bear(symbols="AAPL,MSFT", page=0, page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `symbols`                                                                              | *str*                                                                                  | :heavy_check_mark:                                                                     | Comma-separated list of ticker symbols                                                 | AAPL,MSFT                                                                              |
| `page`                                                                                 | *Optional[int]*                                                                        | :heavy_minus_sign:                                                                     | Page number for pagination (0-based)                                                   |                                                                                        |
| `page_size`                                                                            | *Optional[int]*                                                                        | :heavy_minus_sign:                                                                     | Number of results per page. Use this to control pagination size in list views. (1-200) |                                                                                        |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |                                                                                        |

### Response

**[models.GetBullBearAnalysisResponse](../../models/getbullbearanalysisresponse.md)**

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