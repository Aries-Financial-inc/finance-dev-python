# ReplaceOrdResponseStatus

Order status after the replace request. Typical values after a successful replace:
- `PENDING_REPLACE` — replace request accepted by the broker but not yet final. Keep monitoring; will move to `REPLACED` once confirmed.
- `REPLACED` — the modification took effect. From now on, refer to the order by the new `clOrdId`.
- `REJECTED` — the replace was refused (e.g. the order had already fully filled). The original order is unchanged.

The full FIX OrdStatus enum is supported — see the Place Order response for the complete list of possible values.

## Example Usage

```python
from finance_dev.models import ReplaceOrdResponseStatus

value = ReplaceOrdResponseStatus.NEW

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