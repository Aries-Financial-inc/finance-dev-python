# ResultOutcome

The winning outcome, when `settlementValue` is `1` or `0`. Only when `SETTLED`.

## Example Usage

```python
from finance_dev.models import ResultOutcome

value = ResultOutcome.YES

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name  | Value |
| ----- | ----- |
| `YES` | YES   |
| `NO`  | NO    |