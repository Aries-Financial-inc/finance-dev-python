# CancelOrdRequestPutCall2

Option contract type for option cancels. Use `CALL` for calls and `PUT` for puts. Omit for equity cancels.

## Example Usage

```python
from finance_dev.models import CancelOrdRequestPutCall2

value = CancelOrdRequestPutCall2.PUT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `PUT`  | PUT    |
| `CALL` | CALL   |
| `P`    | P      |
| `C`    | C      |