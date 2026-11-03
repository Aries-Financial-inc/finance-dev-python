# Predictions

## Overview

### Available Operations

* [batch_get](#batch_get) - Batch historical ticks for up to 5 symbols
* [list_orders](#list_orders) - List current prediction orders

## batch_get

Returns historical ticks for multiple symbols in one request. Each query may carry its own optional `from`/`to`/`limit`. Maximum 5 queries per call.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHistoryBatch" method="post" path="/v1/predictions/historical-data/batch" -->
```python
from finance_dev import FinanceDev
from finance_dev.utils import parse_datetime


with FinanceDev() as fd_client:

    res = fd_client.predictions.batch_get(queries=[
        {
            "from_": parse_datetime("2026-04-01T00:00:00Z"),
            "limit": 500,
            "symbol": "HORC_1126_Republican",
            "to": parse_datetime("2026-04-20T00:00:00Z"),
        },
    ])

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `queries`                                                                 | List[[models.PredMdHistoryRequest](../../models/predmdhistoryrequest.md)] | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.GetHistoryBatchResponse](../../models/gethistorybatchresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorEnvelope | 400                  | application/json     |
| errors.ErrorEnvelope | 502                  | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## list_orders

**Closed beta.** Available only to accounts enrolled in the prediction-market orders closed beta. Returns the account's current orders, newest first, one page at a time: every order still open, however old (a GTC order), plus every order created or closed since the trading day rolled over at 17:00 America/Chicago. Older orders are read with List Prediction Order History.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPredictionOrders" method="get" path="/v1/predictions/orders" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.list_orders(account_id="ACCOUNT-0001", status="open", limit=50)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          | Example                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                                                                                         | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | The account. Every order on it is covered, whoever placed it.                                                                                                                        | ACCOUNT-0001                                                                                                                                                                         |
| `status`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Comma-separated order states, or `open` for every state an order can still rest or execute in (`pending_new`, `new`, `partially_filled`, `unknown`). An unknown state returns `400`. | open                                                                                                                                                                                 |
| `placed_by`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Only orders this user placed.                                                                                                                                                        |                                                                                                                                                                                      |
| `symbol`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Only orders on this contract symbol.                                                                                                                                                 |                                                                                                                                                                                      |
| `limit`                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Orders per page. Values above 200 are clamped to 200. `0`, a negative value, or a non-integer returns `400`.                                                                         |                                                                                                                                                                                      |
| `cursor`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | `nextCursor` from the previous page.                                                                                                                                                 |                                                                                                                                                                                      |
| `retries`                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                  |                                                                                                                                                                                      |

### Response

**[models.ListPredictionOrdersResponse](../../models/listpredictionordersresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.PredOrdersErrorEnvelope     | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.PredOrdersErrorEnvelope     | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |