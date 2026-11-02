# BarPrecision

Unit of each bar. Combine with `period` to set the exact bar size.

## Example Usage

```python
from finance_dev.models import BarPrecision

value = BarPrecision.MINUTES

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `MINUTES` | Minutes   |
| `HOURS`   | Hours     |