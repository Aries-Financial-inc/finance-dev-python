# Calendar

## Overview

### Available Operations

* [get_conference_calls](#get_conference_calls) - Get Conference Calls
* [get_earnings_calendar](#get_earnings_calendar) - Get Earnings Calendar
* [get_economics_calendar](#get_economics_calendar) - Get Economics Calendar
* [get_historical_data](#get_historical_data) - Get Historical Economic Data
* [get_mergers_and_acquisitions](#get_mergers_and_acquisitions) - Get Mergers & Acquisitions

## get_conference_calls

Retrieve upcoming and past earnings conference call schedules including dates, times, and dial-in information for management discussions.

### Example Usage

<!-- UsageSnippet language="python" operationID="getConferenceCalls" method="get" path="/v1/calendars/conference-calls" example="success" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.calendar.get_conference_calls(date_from=date.fromisoformat("2024-01-15"), date_to=date.fromisoformat("2024-01-19"), tickers="AAPL,MSFT,GOOGL", page=0, page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                   | Type                                                                                                                                                        | Required                                                                                                                                                    | Description                                                                                                                                                 | Example                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `date_from`                                                                                                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                | :heavy_minus_sign:                                                                                                                                          | Start date in YYYY-MM-DD format. Enter the first date to include in the research window.                                                                    | 2024-01-15                                                                                                                                                  |
| `date_to`                                                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                | :heavy_minus_sign:                                                                                                                                          | End date in YYYY-MM-DD format. Enter the last date to include in the research window.                                                                       | 2024-01-19                                                                                                                                                  |
| `tickers`                                                                                                                                                   | *Optional[str]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                          | Comma-separated list of ticker symbols (max 50)                                                                                                             | AAPL,MSFT,GOOGL                                                                                                                                             |
| `page`                                                                                                                                                      | *Optional[int]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                          | Page number for pagination (0-indexed, max 100000)                                                                                                          | 0                                                                                                                                                           |
| `page_size`                                                                                                                                                 | *Optional[int]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                          | Number of results per page. Use this to control pagination size in list views. Enter a value from 1 to 1000 depending on how much data your UI can display. | 100                                                                                                                                                         |
| `retries`                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                            | :heavy_minus_sign:                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                         |                                                                                                                                                             |

### Response

**[models.GetConferenceCallsResponse](../../models/getconferencecallsresponse.md)**

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

## get_earnings_calendar

Retrieve upcoming earnings release dates and historical earnings announcement schedules for earnings season planning.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEarningsCalendar" method="get" path="/v1/calendars/earnings" example="success" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.calendar.get_earnings_calendar(from_=date.fromisoformat("2024-01-01"), to=date.fromisoformat("2024-01-31"), symbol="AAPL")

    assert res.get_earnings_calendar_response is not None

    # Handle response
    print(res.get_earnings_calendar_response)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `from_`                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                | :heavy_check_mark:                                                                          | Start date in YYYY-MM-DD format. Enter the first date to include in the research window.    | 2024-01-01                                                                                  |
| `to`                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                | :heavy_check_mark:                                                                          | End date in YYYY-MM-DD format. Enter the last date to include in the research window.       | 2024-01-31                                                                                  |
| `symbol`                                                                                    | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Optional stock symbol to filter results. If not provided, returns earnings for all symbols. | AAPL                                                                                        |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.GetEarningsCalendarResponse](../../models/getearningscalendarresponse.md)**

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

## get_economics_calendar

Retrieve scheduled economic data releases including employment reports, GDP announcements, inflation data, and central bank decisions. Supports two independent query modes: (1) single date, or (2) explicit date range. Use only one mode per request.

Supply date, or supply both from and to. A complete from/to range takes precedence when date is also supplied.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEconomicsCalendar" method="get" path="/v1/calendars/economics" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.calendar.get_economics_calendar(date_=date.fromisoformat("2024-01-15"), from_=date.fromisoformat("2024-01-15"), to=date.fromisoformat("2024-03-15"))

    assert res.get_economics_calendar_response is not None

    # Handle response
    print(res.get_economics_calendar_response)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  | Example                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `date_`                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                 | :heavy_minus_sign:                                                                                                           | Single date in YYYY-MM-DD format. Returns events for that date plus 1 month ahead. Either 'date' or 'from' must be provided. | 2024-01-15                                                                                                                   |
| `from_`                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                 | :heavy_minus_sign:                                                                                                           | Start date of range in YYYY-MM-DD format. Must be used with 'to'. Either 'date' or 'from' must be provided.                  | 2024-01-15                                                                                                                   |
| `to`                                                                                                                         | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                 | :heavy_minus_sign:                                                                                                           | End date of range in YYYY-MM-DD format. Required when 'from' is specified.                                                   | 2024-03-15                                                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |                                                                                                                              |

### Response

**[models.GetEconomicsCalendarResponseResponse](../../models/geteconomicscalendarresponseresponse.md)**

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

## get_historical_data

Retrieve historical time series data for an economic indicator. Returns a direct array of data points (no wrapper). Path parameter **symbol** is the economic indicator symbol (e.g. USURTOT, UNITEDSTACONJOBCLA, UNITEDSTACONCRE). No query parameters.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHistoricalData" method="get" path="/v1/calendars/historical/{symbol}" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.calendar.get_historical_data(symbol="USURTOT")

    assert res.get_historical_data_response is not None

    # Handle response
    print(res.get_historical_data_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Economic indicator code from the upstream calendar provider. These codes are not a fixed enum on our side — fetch [GET /v1/calendars/economics](/api-reference/calendars/economics) to see the codes attached to recent calendar entries, then use that code here for the historical series. Common examples:<br/>- `USURTOT` — United States Unemployment Rate (total).<br/>- `UNITEDSTACONJOBCLA` — U.S. Continuing Jobless Claims.<br/>- `UNITEDSTACONCRE` — U.S. Consumer Credit. | USURTOT                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.GetHistoricalDataResponse](../../models/gethistoricaldataresponse.md)**

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

## get_mergers_and_acquisitions

Retrieve M&A activity including announced deals, merger terms, acquisition prices, and transaction timelines.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMergersAndAcquisitions" method="get" path="/v1/calendars/mergers-acquisitions" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.calendar.get_mergers_and_acquisitions(date_from=date.fromisoformat("2024-01-01"), date_to=date.fromisoformat("2024-12-31"), tickers="AAPL,MSFT", page=0, page_size=50)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      | Example                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `date_from`                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                     | :heavy_minus_sign:                                                                                               | Start date in YYYY-MM-DD format. Enter the first date to include in the research window.                         | 2024-01-01                                                                                                       |
| `date_to`                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                     | :heavy_minus_sign:                                                                                               | End date in YYYY-MM-DD format. Enter the last date to include in the research window.                            | 2024-12-31                                                                                                       |
| `tickers`                                                                                                        | *Optional[str]*                                                                                                  | :heavy_minus_sign:                                                                                               | Comma-separated ticker symbols, such as AAPL,MSFT. Use this to request or filter multiple companies in one call. | AAPL,MSFT                                                                                                        |
| `page`                                                                                                           | *Optional[int]*                                                                                                  | :heavy_minus_sign:                                                                                               | Zero-based page offset. Enter 0 for the first page of results.                                                   | 0                                                                                                                |
| `page_size`                                                                                                      | *Optional[int]*                                                                                                  | :heavy_minus_sign:                                                                                               | Number of results per page. Use this to control pagination size in list views. (1-1000)                          | 50                                                                                                               |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |                                                                                                                  |

### Response

**[models.GetMergersAndAcquisitionsResponse](../../models/getmergersandacquisitionsresponse.md)**

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