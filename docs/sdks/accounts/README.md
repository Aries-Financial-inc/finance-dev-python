# Accounts

## Overview

### Available Operations

* [get_account_positions](#get_account_positions) - Get Account Positions
* [get_account_balance](#get_account_balance) - Get Account Balance
* [get_user_accounts](#get_user_accounts) - Get User Accounts

## get_account_positions

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

    res = fd_client.accounts.get_account_positions(id="TEST-ACCOUNT-001")

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

## get_account_balance

Retrieve account balance, cash, equity, and buying power for a specific account (v2). Use this before showing an order ticket or checking whether the account can support a trade. Sterling and the stored balance are read concurrently. The stored read uses Dragonfly, then PostgreSQL on a full cache miss. Sterling supplies the balance when available, enriched with stored Apex fields; otherwise the stored balance is used.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountBalance" method="get" path="/v2/accounts/{id}/balance" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.get_account_balance(id="TEST-ACCOUNT-001")

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

## get_user_accounts

Retrieve all trading accounts for the currently authenticated user. Returns a list of accounts with trading account ID, broker account ID, status, simulation flag, and account type and class. Users may have multiple accounts (for example a live account and a simulation account). Requires bearer token authentication.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUserAccounts" method="get" path="/v2/users/me/accounts" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.get_user_accounts()

    assert res.get_accounts_response is not None

    # Handle response
    print(res.get_accounts_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserAccountsResponse](../../models/getuseraccountsresponse.md)**

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