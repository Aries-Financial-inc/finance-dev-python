# RejectReason

Set when `status` is `rejected`.

## Example Usage

```python
from finance_dev.models import RejectReason

value = RejectReason.NOT_SUPPORTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `NOT_SUPPORTED`    | not_supported      |
| `UNKNOWN_SECURITY` | unknown_security   |
| `OTHER`            | other              |
| `BUSINESS_REJECT`  | business_reject    |