# PredOrdersAppErrorType

Categorical error type, in lowercase.

## Example Usage

```python
from finance_dev.models import PredOrdersAppErrorType

value = PredOrdersAppErrorType.BAD_REQUEST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `BAD_REQUEST`    | bad_request      |
| `AUTHENTICATION` | authentication   |
| `NOT_FOUND`      | not_found        |
| `CONFLICT`       | conflict         |
| `RATE_LIMIT`     | rate_limit       |
| `UNAVAILABLE`    | unavailable      |
| `TIMEOUT`        | timeout          |
| `INTERNAL`       | internal         |