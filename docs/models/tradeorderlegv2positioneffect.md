# TradeOrderLegV2PositionEffect

Whether this leg opens a new position or closes an existing one:
- `OPEN` — opens a new position (or increases an existing one).
- `CLOSE` — closes an existing position (or reduces it).

## Example Usage

```python
from finance_dev.models import TradeOrderLegV2PositionEffect

value = TradeOrderLegV2PositionEffect.OPEN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `OPEN`  | OPEN    |
| `CLOSE` | CLOSE   |