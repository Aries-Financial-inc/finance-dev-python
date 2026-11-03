# Predictions.Orders

## Overview

### Available Operations

* [list_prediction_order_history](#list_prediction_order_history) - List prediction order history
* [list_prediction_mass_cancels](#list_prediction_mass_cancels) - List prediction mass cancels
* [mass_cancel_prediction_orders](#mass_cancel_prediction_orders) - Mass cancel prediction orders
* [get_prediction_mass_cancel](#get_prediction_mass_cancel) - Get prediction mass cancel
* [replace_prediction_order](#replace_prediction_order) - Replace prediction order
* [cancel_prediction_order](#cancel_prediction_order) - Cancel prediction order

## list_prediction_order_history

**Closed beta.** Available only to accounts enrolled in the prediction-market orders closed beta. Returns every order on the account, newest first, one page at a time, optionally bounded by creation time.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPredictionOrderHistory" method="get" path="/v1/predictions/orders/history" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.list_prediction_order_history(account_id="ACCOUNT-0001", status="open", limit=50)

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
| `from_`                                                                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                   | Only orders created at or after this time (RFC 3339). Not RFC 3339 returns `400` `INVALID_FROM`.                                                                                     |                                                                                                                                                                                      |
| `to`                                                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                   | Only orders created before this time (RFC 3339). Not RFC 3339 returns `400` `INVALID_TO`.                                                                                            |                                                                                                                                                                                      |
| `retries`                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                  |                                                                                                                                                                                      |

### Response

**[models.ListPredictionOrderHistoryResponse](../../models/listpredictionorderhistoryresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.PredOrdersErrorEnvelope     | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.PredOrdersErrorEnvelope     | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## list_prediction_mass_cancels

**Closed beta.** Available only to accounts enrolled in the prediction-market orders closed beta. Returns the account's mass cancels, newest first, one page at a time.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPredictionMassCancels" method="get" path="/v1/predictions/orders/mass-cancels" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.list_prediction_mass_cancels(account_id="ACCOUNT-0001", limit=50)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account. Every order on it is covered, whoever placed it.       | ACCOUNT-0001                                                        |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Mass cancels per page. Values above 200 are clamped to 200.         |                                                                     |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | `nextCursor` from the previous page.                                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListPredictionMassCancelsResponse](../../models/listpredictionmasscancelsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.PredOrdersErrorEnvelope     | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.PredOrdersErrorEnvelope     | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## mass_cancel_prediction_orders

**Closed beta.** Available only to accounts enrolled in the prediction-market orders closed beta. Cancels every working order on an account, or only those in one contract, in one request to the venue. Returns `202` with the request, normally `pending`. A `202` does not mean any order is canceled: each order the venue cancels arrives as an ordinary order update.

### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="massCancelPredictionOrders" method="post" path="/v1/predictions/orders/mass-cancels" example="flat_message" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.mass_cancel_prediction_orders(account_id="ACCOUNT-0001", symbol="HORC_1126_Republican")

    assert res.object is not None

    # Handle response
    print(res.object)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="massCancelPredictionOrders" method="post" path="/v1/predictions/orders/mass-cancels" example="flat_with_codes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.mass_cancel_prediction_orders(account_id="ACCOUNT-0001", symbol="HORC_1126_Republican")

    assert res.object is not None

    # Handle response
    print(res.object)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="massCancelPredictionOrders" method="post" path="/v1/predictions/orders/mass-cancels" example="nested_error_object" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.mass_cancel_prediction_orders(account_id="ACCOUNT-0001", symbol="HORC_1126_Republican")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                              | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The account whose working orders to cancel.                                                               | ACCOUNT-0001                                                                                              |
| `outcome`                                                                                                 | [Optional[models.PredOrdersMassCancelRequestOutcome]](../../models/predordersmasscancelrequestoutcome.md) | :heavy_minus_sign:                                                                                        | Cancel only this outcome's orders. Requires `symbol`.                                                     |                                                                                                           |
| `symbol`                                                                                                  | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Cancel only orders in this contract. Omit to cancel every working order on the account.                   | HORC_1126_Republican                                                                                      |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

### Response

**[models.MassCancelPredictionOrdersResponse](../../models/masscancelpredictionordersresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.PredOrdersErrorEnvelope     | 400, 429                           | application/json                   |
| errors.PredOrdersErrorEnvelope     | 500, 503, 504                      | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_prediction_mass_cancel

**Closed beta.** Available only to accounts enrolled in the prediction-market orders closed beta. Returns one mass cancel and the venue's answer to it. The orders it canceled carry its `massCancelId` in their events.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPredictionMassCancel" method="get" path="/v1/predictions/orders/mass-cancels/{massCancelId}" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.get_prediction_mass_cancel(mass_cancel_id="97599149-c654-4879-ab4b-aaac771b2949", account_id="ACCOUNT-0001")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `mass_cancel_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The account the mass cancel was sent for.                           | ACCOUNT-0001                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetPredictionMassCancelResponse](../../models/getpredictionmasscancelresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.PredOrdersErrorEnvelope     | 400, 404                           | application/json                   |
| errors.PredOrdersErrorEnvelope     | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## replace_prediction_order

**Closed beta.** Available only to accounts enrolled in the prediction-market orders closed beta. Amends a working order's terms. Returns `202` with the order and its amend outstanding (`pendingAction` `replace`). The order keeps its working terms until the venue confirms; if the venue refuses, they stay as they were and the reason is on the order.

### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="replacePredictionOrder" method="patch" path="/v1/predictions/orders/{orderId}" example="flat_message" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.replace_prediction_order(order_id="921c6861-f62f-49f2-9f94-5cc33496c5be", account_id="ACCOUNT-0001", price="0.45", quantity="20")

    assert res.object is not None

    # Handle response
    print(res.object)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="replacePredictionOrder" method="patch" path="/v1/predictions/orders/{orderId}" example="flat_with_codes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.replace_prediction_order(order_id="47bb47c0-3414-4b7a-9d44-6ade2d5c0f4d", account_id="ACCOUNT-0001", price="0.45", quantity="20")

    assert res.object is not None

    # Handle response
    print(res.object)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="replacePredictionOrder" method="patch" path="/v1/predictions/orders/{orderId}" example="nested_error_object" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.replace_prediction_order(order_id="ac743bd7-eca0-4de3-8850-ff3e84165bec", account_id="ACCOUNT-0001", price="0.45", quantity="20")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           | Example                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `order_id`                                                                                                            | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | `orderId` returned by Place Prediction Order or List Prediction Orders.                                               |                                                                                                                       |
| `account_id`                                                                                                          | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | The account the order is on.                                                                                          | ACCOUNT-0001                                                                                                          |
| `expire_time`                                                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                  | :heavy_minus_sign:                                                                                                    | New expiry, for `gtd` orders.                                                                                         |                                                                                                                       |
| `price`                                                                                                               | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | New limit price as an exact decimal string.                                                                           | 0.45                                                                                                                  |
| `quantity`                                                                                                            | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | New total quantity as an exact decimal string. Must be greater than zero.                                             | 20                                                                                                                    |
| `stop_px`                                                                                                             | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | New stop price as an exact decimal string, for an order that has not triggered.                                       |                                                                                                                       |
| `time_in_force`                                                                                                       | [Optional[models.PredOrdersReplaceOrderRequestTimeInForce]](../../models/predordersreplaceorderrequesttimeinforce.md) | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |                                                                                                                       |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |                                                                                                                       |

### Response

**[models.ReplacePredictionOrderResponse](../../models/replacepredictionorderresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.PredOrdersErrorEnvelope     | 400, 404, 409, 429                 | application/json                   |
| errors.PredOrdersErrorEnvelope     | 500, 503, 504                      | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## cancel_prediction_order

**Closed beta.** Available only to accounts enrolled in the prediction-market orders closed beta. Cancels a working order in full; the venue has no partial cancel. Returns `202` with the order and its cancel outstanding (`pendingAction` `cancel`). Whether the venue canceled it arrives as an order update.

### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="cancelPredictionOrder" method="post" path="/v1/predictions/orders/{orderId}/cancel" example="flat_message" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.cancel_prediction_order(order_id="b96f4fb8-14e1-472d-8996-8ad676e6baed", account_id="ACCOUNT-0001")

    assert res.object is not None

    # Handle response
    print(res.object)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="cancelPredictionOrder" method="post" path="/v1/predictions/orders/{orderId}/cancel" example="flat_with_codes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.cancel_prediction_order(order_id="bbc50f07-2a0f-411a-b275-427d01e5593e", account_id="ACCOUNT-0001")

    assert res.object is not None

    # Handle response
    print(res.object)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="cancelPredictionOrder" method="post" path="/v1/predictions/orders/{orderId}/cancel" example="nested_error_object" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.predictions.orders.cancel_prediction_order(order_id="28fa94ca-8efa-47cc-b2c2-c77b0901c7c8", account_id="ACCOUNT-0001")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `order_id`                                                                               | *str*                                                                                    | :heavy_check_mark:                                                                       | `orderId` returned by Place Prediction Order or List Prediction Orders.                  |                                                                                          |
| `account_id`                                                                             | *str*                                                                                    | :heavy_check_mark:                                                                       | The account the order is on. Requests act on the account; you are recorded as who asked. | ACCOUNT-0001                                                                             |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |                                                                                          |

### Response

**[models.CancelPredictionOrderResponse](../../models/cancelpredictionorderresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.PredOrdersErrorEnvelope     | 400, 404, 409, 429                 | application/json                   |
| errors.PredOrdersErrorEnvelope     | 500, 503, 504                      | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |