# AdvancedOrderType

Kind of advanced-order list the order was placed in.
- `OCO` — One-cancels-other siblings.
- `BRACKET` — Entry with a profit target and/or stop loss.
- `OTO` — Parent whose fill releases its children.
- `OTOCO` — Parent whose fill releases a one-cancels-other group.

Omitted for ordinary orders.

## Example Usage

```python
from finance_dev.models import AdvancedOrderType

value = AdvancedOrderType.OCO

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `OCO`     | OCO       |
| `BRACKET` | BRACKET   |
| `OTO`     | OTO       |
| `OTOCO`   | OTOCO     |