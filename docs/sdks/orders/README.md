# Orders

## Overview

### Available Operations

* [place_order](#place_order) - Place an order
* [cancel](#cancel) - Cancel an order
* [preview_order](#preview_order) - Preview order
* [replace](#replace) - Replace an order
* [list_active_orders](#list_active_orders) - List active orders (v2)
* [list_order_history](#list_order_history) - List order history (v2)

## place_order

Place an equity or option order. The order type is automatically determined:
- No `legs` array = Equity order
- 1 leg in `legs` array = Single-leg option order
- 2-4 legs in `legs` array = Multi-leg option order

Option and multi-leg orders only support `DAY` and `GTC` for `timeInForce`.

If you send an OSI option symbol in `symbol` and omit `legs`, the backend derives a single option leg automatically.

Price precision validation:
- `LIMIT` validates `price`
- `STOP` validates `stopPrice`
- `STOP_LIMIT` validates both
- Decimal inputs support up to 5 digits after the decimal point.

### Example Usage: equityLimit

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="equityLimit" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: equityMarket

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="equityMarket" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.MARKET,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: flat

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="flat" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="flat_message" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: flat_string

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="flat_string" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="flat_with_codes" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: nested

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="nested" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: nested_bad_request

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="nested_bad_request" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="nested_error_object" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: nested_shared_http_error

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="nested_shared_http_error" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: service_unavailable

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="service_unavailable" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: singleLegCall

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="singleLegCall" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.OPT,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
            },
        ],
        "price": "5.50",
        "qty": "1",
        "side": models.OrderSideEnum.BUY,
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```
### Example Usage: verticalSpread

<!-- UsageSnippet language="python" operationID="placeOrder" method="post" path="/v1/orders" example="verticalSpread" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.place_order(request={
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.OPT,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
            },
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.OPT,
                "side": models.OrdLegSide.SELL,
                "strike_price": "155.00",
            },
        ],
        "price": "2.50",
        "qty": "1",
        "side": models.OrderSideEnum.BUY,
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.ord_response is not None

    # Handle response
    print(res.ord_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.PlaceOrdRequestUnion](../../models/placeordrequestunion.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaceOrderResponse](../../models/placeorderresponse.md)**

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
| errors.AuthenticationErrorEnvelope | 503, 504                           | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## cancel

Cancel an existing order by original client order ID. For option cancels, you can provide the option fields directly or send an OSI option symbol in `symbol` and let the backend derive the option instrument fields.

### Example Usage: cancelEquity

<!-- UsageSnippet language="python" operationID="cancelOrder" method="post" path="/v1/orders/cancel" example="cancelEquity" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.cancel(request={
        "orig_cl_ord_id": "ORDER-123456",
        "security_type": models.SecurityTypeEnum.CS,
        "side": models.OrderSideEnum.BUY,
        "symbol": "AAPL",
        "trading_account_id": "TEST-ACCOUNT-001",
    })

    assert res.cancel_ord_response is not None

    # Handle response
    print(res.cancel_ord_response)

```
### Example Usage: cancelOption

<!-- UsageSnippet language="python" operationID="cancelOrder" method="post" path="/v1/orders/cancel" example="cancelOption" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.cancel(request={
        "maturity": date.fromisoformat("2025-01-17"),
        "orig_cl_ord_id": "ORDER-789012",
        "put_call": models.CancelOrdRequestPutCall2.CALL,
        "security_type": models.SecurityTypeEnum.OPT,
        "side": models.OrderSideEnum.BUY,
        "strike_price": "150.00",
        "symbol": "AAPL",
        "trading_account_id": "TEST-ACCOUNT-001",
    })

    assert res.cancel_ord_response is not None

    # Handle response
    print(res.cancel_ord_response)

```
### Example Usage: flat

<!-- UsageSnippet language="python" operationID="cancelOrder" method="post" path="/v1/orders/cancel" example="flat" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.cancel(request={
        "maturity": date.fromisoformat("2025-01-17"),
        "orig_cl_ord_id": "ORDER-123456",
        "put_call": models.CancelOrdRequestPutCall2.CALL,
        "security_type": models.SecurityTypeEnum.CS,
        "side": models.OrderSideEnum.BUY,
        "strike_price": "150.00",
        "symbol": "AAPL",
        "trading_account_id": "TEST-ACCOUNT-001",
    })

    assert res.cancel_ord_response is not None

    # Handle response
    print(res.cancel_ord_response)

```
### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="cancelOrder" method="post" path="/v1/orders/cancel" example="flat_message" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.cancel(request={
        "account_id": "<id>",
        "maturity": date.fromisoformat("2025-01-17"),
        "orig_cl_ord_id": "ORDER-123456",
        "put_call": models.CancelOrdRequestPutCall1.CALL,
        "security_type": models.SecurityTypeEnum.CS,
        "side": models.OrderSideEnum.BUY,
        "strike_price": "150.00",
        "symbol": "AAPL",
        "trading_account_id": "TEST-ACCOUNT-001",
    })

    assert res.cancel_ord_response is not None

    # Handle response
    print(res.cancel_ord_response)

```
### Example Usage: flat_string

<!-- UsageSnippet language="python" operationID="cancelOrder" method="post" path="/v1/orders/cancel" example="flat_string" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.cancel(request={
        "account_id": "<id>",
        "maturity": date.fromisoformat("2025-01-17"),
        "orig_cl_ord_id": "ORDER-123456",
        "put_call": models.CancelOrdRequestPutCall1.CALL,
        "security_type": models.SecurityTypeEnum.CS,
        "side": models.OrderSideEnum.BUY,
        "strike_price": "150.00",
        "symbol": "AAPL",
        "trading_account_id": "TEST-ACCOUNT-001",
    })

    assert res.cancel_ord_response is not None

    # Handle response
    print(res.cancel_ord_response)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="cancelOrder" method="post" path="/v1/orders/cancel" example="flat_with_codes" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.cancel(request={
        "maturity": date.fromisoformat("2025-01-17"),
        "orig_cl_ord_id": "ORDER-123456",
        "put_call": models.CancelOrdRequestPutCall2.CALL,
        "security_type": models.SecurityTypeEnum.CS,
        "side": models.OrderSideEnum.BUY,
        "strike_price": "150.00",
        "symbol": "AAPL",
        "trading_account_id": "TEST-ACCOUNT-001",
    })

    assert res.cancel_ord_response is not None

    # Handle response
    print(res.cancel_ord_response)

```
### Example Usage: nested

<!-- UsageSnippet language="python" operationID="cancelOrder" method="post" path="/v1/orders/cancel" example="nested" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.cancel(request={
        "maturity": date.fromisoformat("2025-01-17"),
        "orig_cl_ord_id": "ORDER-123456",
        "put_call": models.CancelOrdRequestPutCall2.CALL,
        "security_type": models.SecurityTypeEnum.CS,
        "side": models.OrderSideEnum.BUY,
        "strike_price": "150.00",
        "symbol": "AAPL",
        "trading_account_id": "TEST-ACCOUNT-001",
    })

    assert res.cancel_ord_response is not None

    # Handle response
    print(res.cancel_ord_response)

```
### Example Usage: nested_bad_request

<!-- UsageSnippet language="python" operationID="cancelOrder" method="post" path="/v1/orders/cancel" example="nested_bad_request" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.cancel(request={
        "account_id": "<id>",
        "maturity": date.fromisoformat("2025-01-17"),
        "orig_cl_ord_id": "ORDER-123456",
        "put_call": models.CancelOrdRequestPutCall1.CALL,
        "security_type": models.SecurityTypeEnum.CS,
        "side": models.OrderSideEnum.BUY,
        "strike_price": "150.00",
        "symbol": "AAPL",
        "trading_account_id": "TEST-ACCOUNT-001",
    })

    assert res.cancel_ord_response is not None

    # Handle response
    print(res.cancel_ord_response)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="cancelOrder" method="post" path="/v1/orders/cancel" example="nested_error_object" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.cancel(request={
        "maturity": date.fromisoformat("2025-01-17"),
        "orig_cl_ord_id": "ORDER-123456",
        "put_call": models.CancelOrdRequestPutCall2.CALL,
        "security_type": models.SecurityTypeEnum.CS,
        "side": models.OrderSideEnum.BUY,
        "strike_price": "150.00",
        "symbol": "AAPL",
        "trading_account_id": "TEST-ACCOUNT-001",
    })

    assert res.cancel_ord_response is not None

    # Handle response
    print(res.cancel_ord_response)

```
### Example Usage: nested_shared_http_error

<!-- UsageSnippet language="python" operationID="cancelOrder" method="post" path="/v1/orders/cancel" example="nested_shared_http_error" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.cancel(request={
        "account_id": "<id>",
        "maturity": date.fromisoformat("2025-01-17"),
        "orig_cl_ord_id": "ORDER-123456",
        "put_call": models.CancelOrdRequestPutCall1.CALL,
        "security_type": models.SecurityTypeEnum.CS,
        "side": models.OrderSideEnum.BUY,
        "strike_price": "150.00",
        "symbol": "AAPL",
        "trading_account_id": "TEST-ACCOUNT-001",
    })

    assert res.cancel_ord_response is not None

    # Handle response
    print(res.cancel_ord_response)

```
### Example Usage: service_unavailable

<!-- UsageSnippet language="python" operationID="cancelOrder" method="post" path="/v1/orders/cancel" example="service_unavailable" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.cancel(request={
        "account_id": "<id>",
        "maturity": date.fromisoformat("2025-01-17"),
        "orig_cl_ord_id": "ORDER-123456",
        "put_call": models.CancelOrdRequestPutCall1.CALL,
        "security_type": models.SecurityTypeEnum.CS,
        "side": models.OrderSideEnum.BUY,
        "strike_price": "150.00",
        "symbol": "AAPL",
        "trading_account_id": "TEST-ACCOUNT-001",
    })

    assert res.cancel_ord_response is not None

    # Handle response
    print(res.cancel_ord_response)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.CancelOrdRequestUnion](../../models/cancelordrequestunion.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CancelOrderResponse](../../models/cancelorderresponse.md)**

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
| errors.AuthenticationErrorEnvelope | 503, 504                           | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## preview_order

Preview an order to calculate estimated cost, fees, buying power impact, and option requirements before placing. Uses the same request body as Place Order (PlaceOrdRequest), including the same option `timeInForce` restrictions, OSI-symbol support, and price-precision validation.

### Example Usage: equityLimit

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="equityLimit" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: equityMarket

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="equityMarket" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.MARKET,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: equityPreview

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="equityPreview" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: flat

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="flat" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="flat_message" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: flat_string

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="flat_string" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="flat_with_codes" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: multiLegSpread

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="multiLegSpread" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.OPT,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
            },
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.OPT,
                "side": models.OrdLegSide.SELL,
                "strike_price": "155.00",
            },
        ],
        "price": "2.50",
        "qty": "1",
        "side": models.OrderSideEnum.BUY,
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: nested

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="nested" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: nested_bad_request

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="nested_bad_request" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="nested_error_object" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: nested_shared_http_error

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="nested_shared_http_error" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: optionOrder

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="optionOrder" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.OPT,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
            },
        ],
        "price": "5.50",
        "qty": "1",
        "side": models.OrderSideEnum.BUY,
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: optionPreview

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="optionPreview" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```
### Example Usage: service_unavailable

<!-- UsageSnippet language="python" operationID="previewOrder" method="post" path="/v1/orders/preview" example="service_unavailable" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.preview_order(request={
        "account_id": "<id>",
        "client_id": "CLIENT-001",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "price": "150.00",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.preview_order_response is not None

    # Handle response
    print(res.preview_order_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.PlaceOrdRequestUnion](../../models/placeordrequestunion.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PreviewOrderResponseResponse](../../models/previeworderresponseresponse.md)**

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
| errors.AuthenticationErrorEnvelope | 503, 504                           | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## replace

Replace/modify an existing order (change quantity, price, or time in force). **ID cycling:** a successful replace returns a new `clOrdId`. Use that new ID as `origClOrdId` for any further replaces of this order — the previous ID is no longer valid once replaced.

For single-leg options, you can send the option fields directly, put them inside the single leg, or send an OSI option symbol in `symbol` and let the backend derive the instrument. Multi-leg replaces must pass `legs` explicitly.

Price precision validation:
- `LIMIT` validates `price`
- `STOP` validates `stopPrice`
- `STOP_LIMIT` validates both
- Decimal inputs support up to 5 digits after the decimal point.

### Example Usage: changePrice

<!-- UsageSnippet language="python" operationID="replaceOrder" method="post" path="/v1/orders/replace" example="changePrice" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.replace(request={
        "orig_cl_ord_id": "ORDER-123456",
        "price": "148.50",
        "qty": "10",
        "side": models.OrderSideEnum.BUY,
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.replace_ord_response is not None

    # Handle response
    print(res.replace_ord_response)

```
### Example Usage: changeQuantity

<!-- UsageSnippet language="python" operationID="replaceOrder" method="post" path="/v1/orders/replace" example="changeQuantity" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.replace(request={
        "orig_cl_ord_id": "ORDER-123456",
        "price": "150.00",
        "qty": "20",
        "side": models.OrderSideEnum.BUY,
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.replace_ord_response is not None

    # Handle response
    print(res.replace_ord_response)

```
### Example Usage: flat

<!-- UsageSnippet language="python" operationID="replaceOrder" method="post" path="/v1/orders/replace" example="flat" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.replace(request={
        "account_id": "<id>",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "orig_cl_ord_id": "ORDER-123456",
        "price": "148.50",
        "qty": "20",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.replace_ord_response is not None

    # Handle response
    print(res.replace_ord_response)

```
### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="replaceOrder" method="post" path="/v1/orders/replace" example="flat_message" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.replace(request={
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "orig_cl_ord_id": "ORDER-123456",
        "price": "148.50",
        "qty": "20",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.replace_ord_response is not None

    # Handle response
    print(res.replace_ord_response)

```
### Example Usage: flat_string

<!-- UsageSnippet language="python" operationID="replaceOrder" method="post" path="/v1/orders/replace" example="flat_string" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.replace(request={
        "account_id": "<id>",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "orig_cl_ord_id": "ORDER-123456",
        "price": "148.50",
        "qty": "20",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.replace_ord_response is not None

    # Handle response
    print(res.replace_ord_response)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="replaceOrder" method="post" path="/v1/orders/replace" example="flat_with_codes" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.replace(request={
        "account_id": "<id>",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "orig_cl_ord_id": "ORDER-123456",
        "price": "148.50",
        "qty": "20",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.replace_ord_response is not None

    # Handle response
    print(res.replace_ord_response)

```
### Example Usage: nested

<!-- UsageSnippet language="python" operationID="replaceOrder" method="post" path="/v1/orders/replace" example="nested" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.replace(request={
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "orig_cl_ord_id": "ORDER-123456",
        "price": "148.50",
        "qty": "20",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.replace_ord_response is not None

    # Handle response
    print(res.replace_ord_response)

```
### Example Usage: nested_bad_request

<!-- UsageSnippet language="python" operationID="replaceOrder" method="post" path="/v1/orders/replace" example="nested_bad_request" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.replace(request={
        "account_id": "<id>",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "orig_cl_ord_id": "ORDER-123456",
        "price": "148.50",
        "qty": "20",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.replace_ord_response is not None

    # Handle response
    print(res.replace_ord_response)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="replaceOrder" method="post" path="/v1/orders/replace" example="nested_error_object" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.replace(request={
        "account_id": "<id>",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "orig_cl_ord_id": "ORDER-123456",
        "price": "148.50",
        "qty": "20",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.replace_ord_response is not None

    # Handle response
    print(res.replace_ord_response)

```
### Example Usage: nested_shared_http_error

<!-- UsageSnippet language="python" operationID="replaceOrder" method="post" path="/v1/orders/replace" example="nested_shared_http_error" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.replace(request={
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "orig_cl_ord_id": "ORDER-123456",
        "price": "148.50",
        "qty": "20",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.replace_ord_response is not None

    # Handle response
    print(res.replace_ord_response)

```
### Example Usage: service_unavailable

<!-- UsageSnippet language="python" operationID="replaceOrder" method="post" path="/v1/orders/replace" example="service_unavailable" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.replace(request={
        "account_id": "<id>",
        "currency": "USD",
        "legs": [
            {
                "maturity": date.fromisoformat("2025-01-17"),
                "position_effect": models.OrdLegPositionEffect.OPEN,
                "put_call": models.OrdLegPutCall.CALL,
                "ratio_qty": "1",
                "security_type": models.SecurityTypeEnum.CS,
                "side": models.OrdLegSide.BUY,
                "strike_price": "150.00",
                "symbol": "AAPL",
            },
        ],
        "orig_cl_ord_id": "ORDER-123456",
        "price": "148.50",
        "qty": "20",
        "side": models.OrderSideEnum.BUY,
        "stop_price": "145.00",
        "symbol": "AAPL",
        "time_in_force": models.OrderRequestTimeInForceEnum.DAY,
        "trading_account_id": "TEST-ACCOUNT-001",
        "type": models.OrderTypeEnum.LIMIT,
    })

    assert res.replace_ord_response is not None

    # Handle response
    print(res.replace_ord_response)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.ReplaceOrdRequestUnion](../../models/replaceordrequestunion.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.ReplaceOrderResponse](../../models/replaceorderresponse.md)**

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
| errors.AuthenticationErrorEnvelope | 503, 504                           | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## list_active_orders

Returns active orders (open orders plus today's terminal activity) from the orders v2 cache only. There is no database fallback.

Pagination uses an opaque int64 cursor: omit cursor or send 0 for the first page, then send nextCursor; 0 means exhausted. Each order uses the same domain shape as WebSocket account updates.

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

    res = fd_client.orders.list_active_orders(id="TEST-ACCOUNT-001", limit=50, cursor=0)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                       | Type                                                                                                                                                            | Required                                                                                                                                                        | Description                                                                                                                                                     | Example                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                            | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | Account ID whose active orders you want to read. Use the account identifier from the user's account list or trading setup.                                      | TEST-ACCOUNT-001                                                                                                                                                |
| `limit`                                                                                                                                                         | *Optional[int]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | Maximum number of orders to return in this page. Use smaller values for UI lists and larger values for back-office exports. Default is 50; maximum is 500.      | 50                                                                                                                                                              |
| `cursor`                                                                                                                                                        | *Optional[int]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | Opaque pagination cursor. Send `0` (or omit) for the first page; pass the previous response's `nextCursor` for subsequent pages. Stop when `nextCursor` is `0`. | 0                                                                                                                                                               |
| `retries`                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                | :heavy_minus_sign:                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                             |                                                                                                                                                                 |

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

## list_order_history

Date-range query against **PostgreSQL** only (no `source` parameter). `from` is required; `to` defaults to the current time truncated to the minute (UTC). The server caps the window at **90 days**.

Results are ordered and filtered by `order_created_at` (keyset pagination uses the row `id` for correctness). Rows with `SUPERSEDED` status and rows with `failed_flag = true` are excluded.

Set `exclude_today=true` to narrow `to` to just before midnight **America/New_York**, omitting today's activity (already returned by **GET /v2/accounts/{id}/orders**).

**Pagination:** Same opaque `int64` cursor contract as active orders when reading from DB — `cursor=0` first, then `nextCursor`; `0` means exhausted.

### Example Usage

<!-- UsageSnippet language="python" operationID="listOrderHistory" method="get" path="/v2/accounts/{id}/orders/history" -->
```python
from finance_dev import FinanceDev, models
from finance_dev.utils import parse_datetime


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.orders.list_order_history(id="TEST-ACCOUNT-001", from_=parse_datetime("2026-01-01T00:00:00Z"), to=parse_datetime("2026-01-31T00:00:00Z"), order_by=models.OrderBy.DESC, exclude_today=False, limit=50, cursor=0)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         | Example                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | Account ID whose historical orders you want to read.                                                                                                | TEST-ACCOUNT-001                                                                                                                                    |
| `from_`                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                | :heavy_check_mark:                                                                                                                                  | Start of the history window, inclusive. Enter an RFC 3339 timestamp with timezone, for example `2026-04-01T00:00:00Z`.                              | 2026-01-01T00:00:00Z                                                                                                                                |
| `to`                                                                                                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                | :heavy_minus_sign:                                                                                                                                  | End of the history window, inclusive. Omit it to use the current time. The total range from `from` cannot exceed 90 days.                           | 2026-01-31T00:00:00Z                                                                                                                                |
| `order_by`                                                                                                                                          | [Optional[models.OrderBy]](../../models/orderby.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                  | Sort direction by `order_created_at`. Defaults to `desc` (newest first). Use `asc` for chronological exports.                                       | desc                                                                                                                                                |
| `exclude_today`                                                                                                                                     | *Optional[bool]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                  | Set to `true` when you want historical orders only and do not want today's activity duplicated with the active-orders endpoint.                     | false                                                                                                                                               |
| `limit`                                                                                                                                             | *Optional[int]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                  | Maximum number of historical orders to return in this page. Default is 50; maximum is 500.                                                          | 50                                                                                                                                                  |
| `cursor`                                                                                                                                            | *Optional[int]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                  | Opaque pagination cursor for the database history walk. Send `0` (or omit) for the first page; pass the previous `nextCursor` until it returns `0`. | 0                                                                                                                                                   |
| `retries`                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                    | :heavy_minus_sign:                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                 |                                                                                                                                                     |

### Response

**[models.ListOrderHistoryResponse](../../models/listorderhistoryresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |