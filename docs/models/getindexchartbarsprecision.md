# GetIndexChartBarsPrecision

How long each chart bar covers. Pair with `period` to set the exact size. Note the singular form (different from `/v1/indices/bar` and `/v1/indices/bars`). Allowed values:
- `Minute` — minute bars (intraday).
- `Hour` — hour bars.

## Example Usage

```python
from finance_dev.models import GetIndexChartBarsPrecision

value = GetIndexChartBarsPrecision.MINUTE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `MINUTE` | Minute   |
| `HOUR`   | Hour     |