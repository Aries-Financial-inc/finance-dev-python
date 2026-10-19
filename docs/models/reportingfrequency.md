# ReportingFrequency

How often the underlying data is reported:
- `annual` — once per fiscal year (10-K, full-year statements).
- `quarterly` — once per fiscal quarter (10-Q, quarterly statements).

## Example Usage

```python
from finance_dev.models import ReportingFrequency

value = ReportingFrequency.ANNUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `ANNUAL`    | annual      |
| `QUARTERLY` | quarterly   |