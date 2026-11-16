# PredOrdersMassCancelStatus

`pending` until the venue answers. `not_sent` means nothing reached the venue.

## Example Usage

```python
from finance_dev.models import PredOrdersMassCancelStatus

value = PredOrdersMassCancelStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `PENDING`  | pending    |
| `ACCEPTED` | accepted   |
| `REJECTED` | rejected   |
| `NOT_SENT` | not_sent   |