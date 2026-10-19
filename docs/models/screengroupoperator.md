# ScreenGroupOperator

How the clauses inside this group are combined:
- `AND` — every clause in the group must match (logical AND).
- `OR` — at least one clause in the group must match (logical OR).
- `NOT` — negate the clause inside the group (logical NOT).

## Example Usage

```python
from finance_dev.models import ScreenGroupOperator

value = ScreenGroupOperator.AND

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name  | Value |
| ----- | ----- |
| `AND` | AND   |
| `OR`  | OR    |
| `NOT` | NOT   |