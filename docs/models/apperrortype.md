# AppErrorType

Categorical error type. Use this for branching error-handling logic; the values are stable across endpoints:
- `VALIDATION` — request body or query parameters failed validation.
- `AUTHENTICATION` — missing, invalid, or expired token.
- `AUTHORIZATION` — token is valid but lacks the required scope/permission.
- `NOT_FOUND` — the requested resource does not exist.
- `CONFLICT` — request conflicts with current state (e.g. duplicate).
- `INTERNAL` — server-side error; retry or contact support.
- `TIMEOUT` — operation took too long.
- `UNKNOWN` — uncategorized error; check `message`.
(Additional categorical values may appear in service-specific responses.)

## Example Usage

```python
from finance_dev.models import AppErrorType

value = AppErrorType.UNKNOWN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `UNKNOWN`             | UNKNOWN               |
| `VALIDATION`          | VALIDATION            |
| `AUTHENTICATION`      | AUTHENTICATION        |
| `AUTHORIZATION`       | AUTHORIZATION         |
| `NOT_FOUND`           | NOT_FOUND             |
| `CONFLICT`            | CONFLICT              |
| `INTERNAL`            | INTERNAL              |
| `TIMEOUT`             | TIMEOUT               |
| `RATE_LIMIT`          | RATE_LIMIT            |
| `BAD_REQUEST`         | BAD_REQUEST           |
| `DATABASE`            | DATABASE              |
| `EXTERNAL_SERVICE`    | EXTERNAL_SERVICE      |
| `PRECONDITION_FAILED` | PRECONDITION_FAILED   |
| `SERVICE_UNAVAILABLE` | SERVICE_UNAVAILABLE   |
| `GRPC`                | GRPC                  |
| `QUEUE`               | QUEUE                 |
| `JSON_PARSING`        | JSON_PARSING          |