# CancelOrdResponseStatus

Order status after the cancel request. Typical values after a successful cancel:
- `PENDING_CANCEL` — cancel request accepted by the broker but not yet final. Keep monitoring; will move to `CANCELED` once confirmed.
- `CANCELED` — order is fully cancelled; no further fills will occur.
- `REJECTED` — the cancel was refused (e.g. the order had already fully filled). The original order is unchanged.

The full FIX OrdStatus enum is supported — see the Place Order response for the complete list of possible values.

## Example Usage

```python
from finance_dev.models import CancelOrdResponseStatus

value = CancelOrdResponseStatus.NEW

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `NEW`              | NEW                |
| `PARTIALLY_FILLED` | PARTIALLY_FILLED   |
| `FILLED`           | FILLED             |
| `DONE_FOR_DAY`     | DONE_FOR_DAY       |
| `CANCELED`         | CANCELED           |
| `REPLACED`         | REPLACED           |
| `PENDING_CANCEL`   | PENDING_CANCEL     |
| `STOPPED`          | STOPPED            |
| `REJECTED`         | REJECTED           |
| `SUSPENDED`        | SUSPENDED          |
| `PENDING_NEW`      | PENDING_NEW        |
| `CALCULATED`       | CALCULATED         |
| `EXPIRED`          | EXPIRED            |
| `ACCEPTED_FOR_BID` | ACCEPTED_FOR_BID   |
| `PENDING_REPLACE`  | PENDING_REPLACE    |
| `SUPERSEDED`       | SUPERSEDED         |