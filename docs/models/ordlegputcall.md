# OrdLegPutCall

Option contract type. Use `CALL` for call options and `PUT` for put options.

## Example Usage

```python
from finance_dev.models import OrdLegPutCall

value = OrdLegPutCall.PUT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `PUT`  | PUT    |
| `CALL` | CALL   |
| `P`    | P      |
| `C`    | C      |