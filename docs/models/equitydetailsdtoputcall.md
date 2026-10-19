# EquityDetailsDTOPutCall

Option contract type. Empty for non-option instruments. Accepts long or short form:
- `CALL` or `C` — call option (right to buy at strike).
- `PUT` or `P` — put option (right to sell at strike).

## Example Usage

```python
from finance_dev.models import EquityDetailsDTOPutCall

value = EquityDetailsDTOPutCall.PUT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `PUT`  | PUT    |
| `CALL` | CALL   |
| `P`    | P      |
| `C`    | C      |