# OrderTypeEnum

How the order is priced. Pick one:
- `MARKET` — Execute immediately at the best available price. Fast and guaranteed to fill, but no price guarantee — the actual fill price can move during execution.
- `LIMIT` — Execute only at the limit `price` or better (lower for buys, higher for sells). Gives you price control, no execution guarantee. Requires the `price` field.
- `STOP` — Sits inactive until the market hits `stopPrice`, then converts to a market order. Common for stop-loss exits. Requires the `stopPrice` field.
- `STOP_LIMIT` — Sits inactive until the market hits `stopPrice`, then converts to a limit order at `price`. More control than `STOP`, but the limit may not fill. Requires both `stopPrice` and `price`.

## Example Usage

```python
from finance_dev.models import OrderTypeEnum

value = OrderTypeEnum.MARKET

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `MARKET`     | MARKET       |
| `LIMIT`      | LIMIT        |
| `STOP`       | STOP         |
| `STOP_LIMIT` | STOP_LIMIT   |