# Accounts.Orders

## Overview

### Available Operations

* [list_active](#list_active) - List active orders (v2)

## list_active

Returns active orders (open orders plus today's terminal activity) from the orders v2 cache only. There is no database fallback.

Pagination uses an opaque int64 cursor: omit cursor or send 0 for the first page, then send nextCursor while it is present. The final page omits nextCursor. Each order uses the same domain shape as WebSocket account updates.

### Example Usage

<!-- UsageSnippet language="python" operationID="listActiveOrders" method="get" path="/v2/accounts/{id}/orders" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.orders.list_active(id="TEST-ACCOUNT-001", limit=50, cursor=0)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        | Example                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                                               | *str*                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                 | Account ID whose active orders you want to read. Use the account identifier from the user's account list or trading setup.                                         | TEST-ACCOUNT-001                                                                                                                                                   |
| `limit`                                                                                                                                                            | *Optional[int]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Maximum number of orders to return in this page. Use smaller values for UI lists and larger values for back-office exports. Default is 50; maximum is 500.         | 50                                                                                                                                                                 |
| `cursor`                                                                                                                                                           | *Optional[int]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                 | Opaque pagination cursor. Send `0` (or omit) for the first page; pass the previous response's `nextCursor` for subsequent pages. Stop when `nextCursor` is absent. | 0                                                                                                                                                                  |
| `retries`                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                |                                                                                                                                                                    |

### Response

**[models.ListActiveOrdersResponse](../../models/listactiveordersresponse.md)**

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