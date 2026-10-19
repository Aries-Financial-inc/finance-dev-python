# OrderType

## Example Usage

```python
from finance_dev.models import OrderType

value = OrderType.LIMIT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `LIMIT`           | limit             |
| `STOP`            | stop              |
| `STOP_LIMIT`      | stop_limit        |
| `MARKET_TO_LIMIT` | market_to_limit   |