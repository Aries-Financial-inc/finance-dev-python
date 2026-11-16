# ContractState

`ACTIVE` while it trades, `CLOSED` once trading has ended and the result is not yet known, `SETTLED` once it is, and `DELETED` if the venue withdrew it. `CLOSED` and `SETTLED` are never left.

## Example Usage

```python
from finance_dev.models import ContractState

value = ContractState.ACTIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ACTIVE`  | ACTIVE    |
| `CLOSED`  | CLOSED    |
| `SETTLED` | SETTLED   |
| `DELETED` | DELETED   |