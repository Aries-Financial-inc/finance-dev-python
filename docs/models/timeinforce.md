# TimeInForce

## Example Usage

```python
from finance_dev.models import TimeInForce

value = TimeInForce.DAY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name  | Value |
| ----- | ----- |
| `DAY` | day   |
| `GTC` | gtc   |
| `IOC` | ioc   |
| `FOK` | fok   |
| `GTD` | gtd   |