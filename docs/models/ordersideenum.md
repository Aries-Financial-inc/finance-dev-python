# OrderSideEnum

Which direction to trade in. Pick one:
- `BUY` — buying shares or contracts (opens a long position or closes an existing short).
- `SELL` — selling shares or contracts you already hold (closes a long position).
- `SELL_SHORT` — selling shares you do not own (opens a short position). Subject to short-sale regulations.
- `BUY_TO_COVER` — buying shares to close an open short position.

## Example Usage

```python
from finance_dev.models import OrderSideEnum

value = OrderSideEnum.BUY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `BUY`          | BUY            |
| `SELL`         | SELL           |
| `SELL_SHORT`   | SELL_SHORT     |
| `BUY_TO_COVER` | BUY_TO_COVER   |