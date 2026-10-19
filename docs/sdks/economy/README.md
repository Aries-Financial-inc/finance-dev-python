# Economy

## Overview

### Available Operations

* [get_inflation](#get_inflation) - Get Latest Inflation Data
* [get_inflation_expectations](#get_inflation_expectations) - Get Latest Inflation Expectations
* [get_treasury_yields](#get_treasury_yields) - Get Latest Treasury Yields

## get_inflation

Retrieve historical Consumer Price Index (CPI) and Personal Consumption Expenditures (PCE) inflation metrics including core inflation rates and spending data with flexible date filtering.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInflation" method="get" path="/v1/economy/inflation" example="success" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.economy.get_inflation(date_=date.fromisoformat("2024-01-15"), dates="2024-01-15,2024-01-16", date_from=date.fromisoformat("2024-01-01"), date_to=date.fromisoformat("2024-01-31"), date_after=date.fromisoformat("2024-01-01"), date_before=date.fromisoformat("2024-01-31"), limit=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        | Example                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `date_`                                                                                                                                            | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                       | :heavy_minus_sign:                                                                                                                                 | Exact date in YYYY-MM-DD format. Use this when you want one specific calendar day.                                                                 | 2024-01-15                                                                                                                                         |
| `dates`                                                                                                                                            | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Comma-separated list of dates in YYYY-MM-DD format. Use this when you want several specific dates in one request.                                  | 2024-01-15,2024-01-16                                                                                                                              |
| `date_from`                                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                       | :heavy_minus_sign:                                                                                                                                 | Start-date filter. Returns records on or after this date.                                                                                          | 2024-01-01                                                                                                                                         |
| `date_to`                                                                                                                                          | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                       | :heavy_minus_sign:                                                                                                                                 | End-date filter. Returns records on or before this date.                                                                                           | 2024-01-31                                                                                                                                         |
| `date_after`                                                                                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                       | :heavy_minus_sign:                                                                                                                                 | After-date filter. Returns records after this date, excluding the date itself.                                                                     | 2024-01-01                                                                                                                                         |
| `date_before`                                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                       | :heavy_minus_sign:                                                                                                                                 | Before-date filter. Returns records before this date, excluding the date itself.                                                                   | 2024-01-31                                                                                                                                         |
| `limit`                                                                                                                                            | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits.                              | 100                                                                                                                                                |
| `sort`                                                                                                                                             | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | A comma-separated list of sort columns. For each column, append `.asc` or `.desc` to specify direction. Defaults to `date.asc` when not specified. |                                                                                                                                                    |
| `next`                                                                                                                                             | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Pagination cursor from the previous response. Omit it on the first request, then send the returned cursor to fetch the next page.                  |                                                                                                                                                    |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |                                                                                                                                                    |

### Response

**[models.GetInflationResponse](../../models/getinflationresponse.md)**

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

## get_inflation_expectations

Retrieve historical inflation expectations data from financial markets and surveys to gauge future inflation trends with flexible date filtering.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInflationExpectations" method="get" path="/v1/economy/inflation-expectations" example="success" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.economy.get_inflation_expectations(date_=date.fromisoformat("2024-01-15"), dates="2024-01-15,2024-01-16", date_from=date.fromisoformat("2024-01-01"), date_to=date.fromisoformat("2024-01-31"), date_after=date.fromisoformat("2024-01-01"), date_before=date.fromisoformat("2024-01-31"), limit=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        | Example                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `date_`                                                                                                                                            | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                       | :heavy_minus_sign:                                                                                                                                 | Exact date in YYYY-MM-DD format. Use this when you want one specific calendar day.                                                                 | 2024-01-15                                                                                                                                         |
| `dates`                                                                                                                                            | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Comma-separated list of dates in YYYY-MM-DD format. Use this when you want several specific dates in one request.                                  | 2024-01-15,2024-01-16                                                                                                                              |
| `date_from`                                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                       | :heavy_minus_sign:                                                                                                                                 | Start-date filter. Returns records on or after this date.                                                                                          | 2024-01-01                                                                                                                                         |
| `date_to`                                                                                                                                          | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                       | :heavy_minus_sign:                                                                                                                                 | End-date filter. Returns records on or before this date.                                                                                           | 2024-01-31                                                                                                                                         |
| `date_after`                                                                                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                       | :heavy_minus_sign:                                                                                                                                 | After-date filter. Returns records after this date, excluding the date itself.                                                                     | 2024-01-01                                                                                                                                         |
| `date_before`                                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                       | :heavy_minus_sign:                                                                                                                                 | Before-date filter. Returns records before this date, excluding the date itself.                                                                   | 2024-01-31                                                                                                                                         |
| `limit`                                                                                                                                            | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits.                              | 100                                                                                                                                                |
| `sort`                                                                                                                                             | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | A comma-separated list of sort columns. For each column, append `.asc` or `.desc` to specify direction. Defaults to `date.asc` when not specified. |                                                                                                                                                    |
| `next`                                                                                                                                             | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Pagination cursor from the previous response. Omit it on the first request, then send the returned cursor to fetch the next page.                  |                                                                                                                                                    |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |                                                                                                                                                    |

### Response

**[models.GetInflationExpectationsResponse](../../models/getinflationexpectationsresponse.md)**

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

## get_treasury_yields

Retrieve historical U.S. Treasury yields across different maturities including short-term bills and long-term bonds with flexible date filtering.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTreasuryYields" method="get" path="/v1/economy/treasury-yields" example="success" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.economy.get_treasury_yields(date_=date.fromisoformat("2024-01-15"), dates="2024-01-15,2024-01-16", date_from=date.fromisoformat("2024-01-01"), date_to=date.fromisoformat("2024-01-31"), date_after=date.fromisoformat("2024-01-01"), date_before=date.fromisoformat("2024-01-31"), limit=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                           | Type                                                                                                                                                                                                                | Required                                                                                                                                                                                                            | Description                                                                                                                                                                                                         | Example                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `date_`                                                                                                                                                                                                             | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                  | Exact date in YYYY-MM-DD format. Use this when you want one specific calendar day.                                                                                                                                  | 2024-01-15                                                                                                                                                                                                          |
| `dates`                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                  | Comma-separated list of dates in YYYY-MM-DD format. Use this when you want several specific dates in one request.                                                                                                   | 2024-01-15,2024-01-16                                                                                                                                                                                               |
| `date_from`                                                                                                                                                                                                         | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                  | Start-date filter. Returns records on or after this date.                                                                                                                                                           | 2024-01-01                                                                                                                                                                                                          |
| `date_to`                                                                                                                                                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                  | End-date filter. Returns records on or before this date.                                                                                                                                                            | 2024-01-31                                                                                                                                                                                                          |
| `date_after`                                                                                                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                  | After-date filter. Returns records after this date, excluding the date itself.                                                                                                                                      | 2024-01-01                                                                                                                                                                                                          |
| `date_before`                                                                                                                                                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                  | Before-date filter. Returns records before this date, excluding the date itself.                                                                                                                                    | 2024-01-31                                                                                                                                                                                                          |
| `limit`                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                  | Maximum number of results to return. Use smaller values for UI pages and larger values for exports within API limits.                                                                                               | 100                                                                                                                                                                                                                 |
| `sort`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                  | A comma-separated list of sort columns. For each column, append `.asc` or `.desc` to specify direction. Massive documents this family with date-based sorting; use provider-supported column names in the text box. |                                                                                                                                                                                                                     |
| `next`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                  | Pagination cursor from the previous response. Omit it on the first request, then send the returned cursor to fetch the next page.                                                                                   |                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                 |                                                                                                                                                                                                                     |

### Response

**[models.GetTreasuryYieldsResponse](../../models/gettreasuryyieldsresponse.md)**

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