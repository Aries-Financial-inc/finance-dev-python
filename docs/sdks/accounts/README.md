# Accounts

## Overview

### Available Operations

* [get_positions](#get_positions) - Get Account Positions
* [get_balance](#get_balance) - Get Account Balance

## get_positions

Retrieve all open positions for a specific account. Use this for portfolio screens and pre-trade checks before selling or closing a position. Positions come only from the position-state MemoryDB read model; there is no Sterling or database fallback. An unavailable read model returns 503. Authorization accepts either the `account:information` or the `position:information` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountPositions" method="get" path="/v1/accounts/{id}/positions" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.get_positions(id="TEST-ACCOUNT-001")

    assert res.get_positions_response is not None

    # Handle response
    print(res.get_positions_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                        | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Account whose positions you want to read. Enter the account ID from [User Accounts](/api-reference/accounts/user-accounts). | TEST-ACCOUNT-001                                                                                                            |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetAccountPositionsResponse](../../models/getaccountpositionsresponse.md)**

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
| errors.AuthenticationErrorEnvelope | 503                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_balance

Retrieve account balance, cash, equity, and buying power for a specific account (v2). Use this before showing an order ticket or checking whether the account can support a trade. Sterling and the stored balance are read concurrently. The stored read uses Dragonfly, then PostgreSQL on a full cache miss. Sterling supplies the balance when available, enriched with stored Apex fields; otherwise the stored balance is used.

Two fields depend on the account type. `cashBalance` is returned only for cash accounts and `intradayMarginBalance` only for margin accounts; the other field is omitted from the response, not returned as `null` or `"0"`. Neither is returned for any other account type. Read `account_class` from `GET /v2/users/me/accounts` to know which applies.

### Example Usage: cashAccount

<!-- UsageSnippet language="python" operationID="getAccountBalance" method="get" path="/v2/accounts/{id}/balance" example="cashAccount" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.get_balance(id="TEST-ACCOUNT-001")

    assert res.account_balance_v2 is not None

    # Handle response
    print(res.account_balance_v2)

```
### Example Usage: marginAccount

<!-- UsageSnippet language="python" operationID="getAccountBalance" method="get" path="/v2/accounts/{id}/balance" example="marginAccount" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.get_balance(id="TEST-ACCOUNT-001")

    assert res.account_balance_v2 is not None

    # Handle response
    print(res.account_balance_v2)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    | Example                                                                                        |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `id`                                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | Account whose balance you want to read. Enter the account ID from `GET /v1/users/me/accounts`. | TEST-ACCOUNT-001                                                                               |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |                                                                                                |

### Response

**[models.GetAccountBalanceResponse](../../models/getaccountbalanceresponse.md)**

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
| errors.AuthenticationErrorEnvelope | 503                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |