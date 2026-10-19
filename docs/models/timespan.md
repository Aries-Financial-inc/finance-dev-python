# Timespan

Time span unit for each aggregate bar, such as minute, hour, day, week, month, quarter, or year when supported.

## Example Usage

```python
from finance_dev.models import Timespan

value = Timespan.SECOND

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `SECOND`  | second    |
| `MINUTE`  | minute    |
| `HOUR`    | hour      |
| `DAY`     | day       |
| `WEEK`    | week      |
| `MONTH`   | month     |
| `QUARTER` | quarter   |
| `YEAR`    | year      |