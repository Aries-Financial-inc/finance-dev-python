# OrderType

ForecastEx does not support `stop` or `market_to_limit` orders.

## Example Usage

```python
from finance_dev.models import OrderType

value = OrderType.LIMIT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `LIMIT`      | limit        |
| `STOP_LIMIT` | stop_limit   |