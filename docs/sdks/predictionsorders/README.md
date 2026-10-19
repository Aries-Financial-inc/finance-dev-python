# Predictions.Orders

## Overview

### Available Operations

* [list_prediction_orders](#list_prediction_orders) - List prediction orders
* [place_prediction_order](#place_prediction_order) - Place prediction order
* [get_prediction_order](#get_prediction_order) - Get prediction order

## list_prediction_orders

**Closed beta.** Available only to accounts enrolled in the prediction-market orders closed beta. Returns the authenticated user's prediction-market orders, newest first, one page at a time.

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

    res = fd_client.predictions.orders.list_prediction_orders(status="open", limit=50)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          | Example                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `status`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Comma-separated order states, or `open` for every state an order can still rest or execute in (`pending_new`, `new`, `partially_filled`, `unknown`). An unknown state returns `400`. | open                                                                                                                                                                                 |
| `account_id`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Only orders on this account.                                                                                                                                                         |                                                                                                                                                                                      |
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

## place_prediction_order

**Closed beta.** Available only to accounts enrolled in the prediction-market orders closed beta. Places a prediction-market order for the authenticated user. Returns `202` as soon as the order is on its way to the venue, normally in state `pending_new`. Read the venue's answer back with Get Prediction Order.

### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="placePredictionOrder" method="post" path="/v1/predictions/orders" example="flat_message" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.place_prediction_order(account_id="ACCOUNT-0001", order_type=models.OrderType.LIMIT, outcome=models.PredOrdersPlaceOrderRequestOutcome.YES, quantity="10", side=models.PredOrdersPlaceOrderRequestSide.BUY, symbol="HORC_1126_Republican", time_in_force=models.TimeInForce.DAY, idempotency_key="7d1c8e0a-4b8f-4e3a-9f43-2a6b1d0c9e11", client_order_ref="7d1c8e0a-4b8f-4e3a-9f43-2a6b1d0c9e11", price="0.54", stop_px="0.50")

    assert res.object is not None

    # Handle response
    print(res.object)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="placePredictionOrder" method="post" path="/v1/predictions/orders" example="flat_with_codes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.place_prediction_order(account_id="ACCOUNT-0001", order_type=models.OrderType.LIMIT, outcome=models.PredOrdersPlaceOrderRequestOutcome.YES, quantity="10", side=models.PredOrdersPlaceOrderRequestSide.BUY, symbol="HORC_1126_Republican", time_in_force=models.TimeInForce.DAY, idempotency_key="7d1c8e0a-4b8f-4e3a-9f43-2a6b1d0c9e11", client_order_ref="7d1c8e0a-4b8f-4e3a-9f43-2a6b1d0c9e11", price="0.54", stop_px="0.50")

    assert res.object is not None

    # Handle response
    print(res.object)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="placePredictionOrder" method="post" path="/v1/predictions/orders" example="nested_error_object" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.place_prediction_order(account_id="ACCOUNT-0001", order_type=models.OrderType.LIMIT, outcome=models.PredOrdersPlaceOrderRequestOutcome.YES, quantity="10", side=models.PredOrdersPlaceOrderRequestSide.BUY, symbol="HORC_1126_Republican", time_in_force=models.TimeInForce.DAY, idempotency_key="7d1c8e0a-4b8f-4e3a-9f43-2a6b1d0c9e11", client_order_ref="7d1c8e0a-4b8f-4e3a-9f43-2a6b1d0c9e11", price="0.54", stop_px="0.50")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                | The account to place the order on.                                                                                                                                                                                                                                | ACCOUNT-0001                                                                                                                                                                                                                                                      |
| `order_type`                                                                                                                                                                                                                                                      | [models.OrderType](../../models/ordertype.md)                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                               | limit                                                                                                                                                                                                                                                             |
| `outcome`                                                                                                                                                                                                                                                         | [models.PredOrdersPlaceOrderRequestOutcome](../../models/predordersplaceorderrequestoutcome.md)                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                | The binary outcome the order trades. It is never inferred from `side`.                                                                                                                                                                                            | YES                                                                                                                                                                                                                                                               |
| `quantity`                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                | Number of contracts as an exact decimal string. Must be greater than zero.                                                                                                                                                                                        | 10                                                                                                                                                                                                                                                                |
| `side`                                                                                                                                                                                                                                                            | [models.PredOrdersPlaceOrderRequestSide](../../models/predordersplaceorderrequestside.md)                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                               | buy                                                                                                                                                                                                                                                               |
| `symbol`                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                | Prediction-market contract symbol, as returned by search or Get Event Contracts.                                                                                                                                                                                  | HORC_1126_Republican                                                                                                                                                                                                                                              |
| `time_in_force`                                                                                                                                                                                                                                                   | [models.TimeInForce](../../models/timeinforce.md)                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                               | day                                                                                                                                                                                                                                                               |
| `idempotency_key`                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | Makes a retry safe. A placement repeating a key you already used returns the order that key placed and places nothing new. The same key with different order terms returns `400` `INVALID_ORDER`. Without it, every request is a new order. Send it at most once. | 7d1c8e0a-4b8f-4e3a-9f43-2a6b1d0c9e11                                                                                                                                                                                                                              |
| `client_order_ref`                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | Your own reference for the order, unique per account. Reusing one returns `409` `CLIENT_ORDER_REF_IN_USE`; it is not a retry key. To retry safely, use the `Idempotency-Key` header.                                                                              | 7d1c8e0a-4b8f-4e3a-9f43-2a6b1d0c9e11                                                                                                                                                                                                                              |
| `expire_time`                                                                                                                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                | Required when `timeInForce` is `gtd`.                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                   |
| `price`                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | Limit price as an exact decimal string. Required for `limit` and `stop_limit`.                                                                                                                                                                                    | 0.54                                                                                                                                                                                                                                                              |
| `stop_px`                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                | Stop price as an exact decimal string. Required for `stop` and `stop_limit`.                                                                                                                                                                                      | 0.50                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                               |                                                                                                                                                                                                                                                                   |

### Response

**[models.PlacePredictionOrderResponse](../../models/placepredictionorderresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.PredOrdersErrorEnvelope     | 400, 409, 429                      | application/json                   |
| errors.PredOrdersErrorEnvelope     | 500, 503, 504                      | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_prediction_order

**Closed beta.** Available only to accounts enrolled in the prediction-market orders closed beta. Returns one of the authenticated user's prediction-market orders together with every venue execution report against it.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPredictionOrder" method="get" path="/v1/predictions/orders/{orderId}" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.get_prediction_order(order_id="26cc5dad-e417-4e9f-acfd-09d65e80b551")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `order_id`                                                              | *str*                                                                   | :heavy_check_mark:                                                      | `orderId` returned by Place Prediction Order or List Prediction Orders. |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.GetPredictionOrderResponse](../../models/getpredictionorderresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.PredOrdersErrorEnvelope     | 404                                | application/json                   |
| errors.PredOrdersErrorEnvelope     | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |