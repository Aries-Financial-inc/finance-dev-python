# Ownership

## Overview

### Available Operations

* [get_institutional](#get_institutional) - Get Institutional Ownership
* [get_portfolio](#get_portfolio) - Get Institutional Portfolio
* [get_data](#get_data) - Get Company Ownership Data
* [get_fund_data](#get_fund_data) - Get Fund Ownership Data
* [get_insider_transactions](#get_insider_transactions) - Get Insider Transactions

## get_institutional

Retrieve institutional ownership data showing the percentage of shares held by institutional investors and changes over time.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInstitutionalOwnership" method="get" path="/v1/institutional/ownership" example="default" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.ownership.get_institutional(cusip="023135106", from_=date.fromisoformat("2024-01-01"), to=date.fromisoformat("2024-12-31"), symbol="TSLA")

    assert res.institutional_ownership_response is not None

    # Handle response
    print(res.institutional_ownership_response)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `cusip`                                                                                     | *str*                                                                                       | :heavy_check_mark:                                                                          | CUSIP security identifier for the security you want institutional ownership for.            | 023135106                                                                                   |
| `from_`                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                | :heavy_check_mark:                                                                          | Start date in YYYY-MM-DD format. Enter the first date to include in the research window.    | 2024-01-01                                                                                  |
| `to`                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                | :heavy_check_mark:                                                                          | End date in YYYY-MM-DD format. Enter the last date to include in the research window.       | 2024-12-31                                                                                  |
| `symbol`                                                                                    | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Optional stock ticker symbol filter, such as AAPL. Use it to narrow results to one company. | TSLA                                                                                        |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.GetInstitutionalOwnershipResponse](../../models/getinstitutionalownershipresponse.md)**

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

## get_portfolio

Retrieve portfolio holdings for institutional investors including hedge funds, mutual funds, and pension funds based on SEC Form 13F filings.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInstitutionalPortfolio" method="get" path="/v1/institutional/portfolio" example="default" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.ownership.get_portfolio(cik="0001067983", from_=date.fromisoformat("2024-01-01"), to=date.fromisoformat("2024-12-31"))

    assert res.institutional_portfolio_response is not None

    # Handle response
    print(res.institutional_portfolio_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `cik`                                                                                    | *str*                                                                                    | :heavy_check_mark:                                                                       | Central Index Key (CIK) of the institution.                                              | 0001067983                                                                               |
| `from_`                                                                                  | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)             | :heavy_check_mark:                                                                       | Start date in YYYY-MM-DD format. Enter the first date to include in the research window. | 2024-01-01                                                                               |
| `to`                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)             | :heavy_check_mark:                                                                       | End date in YYYY-MM-DD format. Enter the last date to include in the research window.    | 2024-12-31                                                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |                                                                                          |

### Response

**[models.GetInstitutionalPortfolioResponse](../../models/getinstitutionalportfolioresponse.md)**

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

## get_data

Retrieve detailed ownership structure showing percentage stakes held by institutional investors, insiders, and retail shareholders.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOwnershipData" method="get" path="/v1/ownership/data" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.ownership.get_data(symbol="<value>")

    assert res.ownership_data_response is not None

    # Handle response
    print(res.ownership_data_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `symbol`                                                                                         | *str*                                                                                            | :heavy_check_mark:                                                                               | Stock symbol, such as AAPL. Use it to narrow results to one company.                             |
| `limit`                                                                                          | *Optional[int]*                                                                                  | :heavy_minus_sign:                                                                               | Optional maximum number of results to return. Use it to keep ownership lists small for UI views. |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[models.GetOwnershipDataResponse](../../models/getownershipdataresponse.md)**

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

## get_fund_data

Retrieve mutual fund and ETF ownership data showing which funds hold positions in a specific security and their holding amounts.

### Example Usage

<!-- UsageSnippet language="python" operationID="getFundOwnership" method="get" path="/v1/ownership/fund" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.ownership.get_fund_data(symbol="<value>")

    assert res.ownership_data_response is not None

    # Handle response
    print(res.ownership_data_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `symbol`                                                                                         | *str*                                                                                            | :heavy_check_mark:                                                                               | Stock symbol, such as AAPL. Use it to narrow results to one company.                             |
| `limit`                                                                                          | *Optional[int]*                                                                                  | :heavy_minus_sign:                                                                               | Optional maximum number of results to return. Use it to keep ownership lists small for UI views. |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[models.GetFundOwnershipResponse](../../models/getfundownershipresponse.md)**

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

## get_insider_transactions

Retrieve insider trading activity including purchases, sales, and option exercises by company executives, directors, and major shareholders.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInsiderTransactions" method="get" path="/v1/ownership/insider-transactions" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.ownership.get_insider_transactions(symbol="<value>")

    assert res.insider_transactions_response is not None

    # Handle response
    print(res.insider_transactions_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `symbol`                                                                       | *str*                                                                          | :heavy_check_mark:                                                             | Stock symbol, such as AAPL. Use it to narrow results to one company.           |
| `from_`                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)   | :heavy_minus_sign:                                                             | Optional start date in YYYY-MM-DD format. Use it to begin the research window. |
| `to`                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)   | :heavy_minus_sign:                                                             | Optional end date in YYYY-MM-DD format. Use it to end the research window.     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[models.GetInsiderTransactionsResponse](../../models/getinsidertransactionsresponse.md)**

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