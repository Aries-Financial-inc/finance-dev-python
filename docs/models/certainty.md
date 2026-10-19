# Certainty

How sure order entry is of `state`. Anything other than `certain` means the order's state could not be confirmed; `certaintyReason` says why.

## Example Usage

```python
from finance_dev.models import Certainty

value = Certainty.CERTAIN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `CERTAIN`            | certain              |
| `UNKNOWN_UNACKED`    | unknown_unacked      |
| `UNKNOWN_GAP`        | unknown_gap          |
| `UNKNOWN_STORE_LOST` | unknown_store_lost   |