# OrdLegPositionEffect

Whether this leg opens or closes a position. Use `OPEN` for a new position and `CLOSE` when closing an existing position.

## Example Usage

```python
from finance_dev.models import OrdLegPositionEffect

value = OrdLegPositionEffect.O

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `O`     | O       |
| `C`     | C       |
| `OPEN`  | OPEN    |
| `CLOSE` | CLOSE   |