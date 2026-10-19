# Category

What kind of trade this order represents.
- `EQUITY` — Plain stock or ETF order.
- `SINGLE_LEG` — One option contract (call or put).
- `MULTI_LEG` — Two-to-four-leg option strategy (spread, condor, straddle, etc.). See the `legs` array.

Omitted when the order has not been classified.

## Example Usage

```python
from finance_dev.models import Category

value = Category.SINGLE_LEG

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `SINGLE_LEG` | SINGLE_LEG   |
| `MULTI_LEG`  | MULTI_LEG    |
| `EQUITY`     | EQUITY       |