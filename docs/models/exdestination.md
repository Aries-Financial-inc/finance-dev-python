# ExDestination

Where the order was routed for execution. Useful for support diagnostics and advanced routing displays.
- `MNGD` — Managed routing (Aries chooses the best venue automatically).
- `MNGDFTE` — Managed routing with fill-then-end (extended) handling.

## Example Usage

```python
from finance_dev.models import ExDestination

value = ExDestination.MNGD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `MNGD`    | MNGD      |
| `MNGDFTE` | MNGDFTE   |