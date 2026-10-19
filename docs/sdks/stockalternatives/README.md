# StockAlternatives

## Overview

### Available Operations

* [get_lobbying](#get_lobbying) - Get Lobbying
* [get_transcripts](#get_transcripts) - Get Transcript by ID

## get_lobbying

Retrieve lobbying data for a symbol within a date range.

### Example Usage

<!-- UsageSnippet language="python" operationID="getLobbying" method="get" path="/v1/stock/lobbying" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternatives.get_lobbying(symbol="AAPL", from_=date.fromisoformat("2024-01-01"), to=date.fromisoformat("2024-12-31"))

    assert res.lobbying_response is not None

    # Handle response
    print(res.lobbying_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `from_`                                                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_check_mark:                                                                                                          | Start of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-01-01`).                                              | 2024-01-01                                                                                                                  |
| `to`                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_check_mark:                                                                                                          | End of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-12-31`).                                                | 2024-12-31                                                                                                                  |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetLobbyingResponse](../../models/getlobbyingresponse.md)**

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

## get_transcripts

Retrieve a single earnings call transcript by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTranscript" method="get" path="/v1/stock/transcripts" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternatives.get_transcripts(id="<id>")

    assert res.transcript_response is not None

    # Handle response
    print(res.transcript_response)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                    | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | Unique identifier for an earnings-call transcript. Obtain it from `/v1/stock/transcripts/list` for the symbol you want. |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.GetTranscriptResponse](../../models/gettranscriptresponse.md)**

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