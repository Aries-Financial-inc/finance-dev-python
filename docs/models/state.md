# State

Order lifecycle state. `unknown` means order entry lost track of the order and says so rather than guessing; see `certainty`.

## Example Usage

```python
from finance_dev.models import State

value = State.PENDING_NEW

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `PENDING_NEW`      | pending_new        |
| `NEW`              | new                |
| `PARTIALLY_FILLED` | partially_filled   |
| `FILLED`           | filled             |
| `CANCELED`         | canceled           |
| `REJECTED`         | rejected           |
| `EXPIRED`          | expired            |
| `DONE_FOR_DAY`     | done_for_day       |
| `UNKNOWN`          | unknown            |