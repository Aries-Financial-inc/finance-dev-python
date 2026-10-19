# Filings

## Overview

### Available Operations

* [get_sec](#get_sec) - Get SEC Filings
* [get_similarity_index](#get_similarity_index) - Get Filings Similarity Index

## get_sec

Retrieve Securities and Exchange Commission (SEC) filings including 10-K annual reports, 10-Q quarterly reports, 8-K current reports, and proxy statements.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSecFilings" method="get" path="/v1/filings/sec" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.filings.get_sec(symbol="AAPL", form="10-K")

    assert res.sec_filings_response is not None

    # Handle response
    print(res.sec_filings_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `symbol`                                                                                 | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | Stock symbol (optional if cik provided)                                                  | AAPL                                                                                     |
| `cik`                                                                                    | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | Central Index Key (optional if symbol provided)                                          |                                                                                          |
| `access_number`                                                                          | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | SEC access number to filter by specific filing                                           |                                                                                          |
| `form`                                                                                   | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | Form type (e.g. 10-K, 10-Q, 8-K, DEF 14A)                                                | 10-K                                                                                     |
| `from_`                                                                                  | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)             | :heavy_minus_sign:                                                                       | Start date in YYYY-MM-DD format. Enter the first date to include in the research window. |                                                                                          |
| `to`                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)             | :heavy_minus_sign:                                                                       | End date in YYYY-MM-DD format. Enter the last date to include in the research window.    |                                                                                          |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |                                                                                          |

### Response

**[models.GetSecFilingsResponse](../../models/getsecfilingsresponse.md)**

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

## get_similarity_index

Retrieve similarity scores comparing current SEC filings to previous filings to identify significant changes in disclosures and risk factors. Provide either `symbol` or `cik`: `symbol` is required when `cik` is omitted, and `cik` is required when `symbol` is omitted. `freq` is optional.

At least one of symbol or cik is required; both are accepted.

### Example Usage

<!-- UsageSnippet language="python" operationID="getFilingsSimilarityIndex" method="get" path="/v1/filings/similarity-index" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.filings.get_similarity_index(symbol="MSFT", freq=models.ReportingFrequency.QUARTERLY)

    assert res.filings_similarity_index_response is not None

    # Handle response
    print(res.filings_similarity_index_response)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                  | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Stock symbol, such as AAPL. Use it to narrow results to one company. Required when `cik` is not provided. | MSFT                                                                                                      |
| `cik`                                                                                                     | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Central Index Key. Required when `symbol` is not provided.                                                |                                                                                                           |
| `freq`                                                                                                    | [Optional[models.ReportingFrequency]](../../models/reportingfrequency.md)                                 | :heavy_minus_sign:                                                                                        | Reporting frequency filter. Use annual or quarterly when you want only one reporting cadence.             | quarterly                                                                                                 |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

### Response

**[models.GetFilingsSimilarityIndexResponse](../../models/getfilingssimilarityindexresponse.md)**

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