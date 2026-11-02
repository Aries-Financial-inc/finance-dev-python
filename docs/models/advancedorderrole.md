# AdvancedOrderRole

The order's role within its advanced-order list.
- `SIBLING` — An OCO order.
- `ENTRY`, `PROFIT_TARGET`, `STOP_LOSS` — Bracket orders.
- `PARENT`, `CHILD` — OTO and OTOCO orders.

Omitted for ordinary orders.

## Example Usage

```python
from finance_dev.models import AdvancedOrderRole

value = AdvancedOrderRole.SIBLING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `SIBLING`       | SIBLING         |
| `ENTRY`         | ENTRY           |
| `PROFIT_TARGET` | PROFIT_TARGET   |
| `STOP_LOSS`     | STOP_LOSS       |
| `PARENT`        | PARENT          |
| `CHILD`         | CHILD           |