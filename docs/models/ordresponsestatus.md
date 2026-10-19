# OrdResponseStatus

Current order lifecycle state, mirroring FIX Tag 39 (OrdStatus). Most common values you'll see:
- `PENDING_NEW` — broker has not yet acknowledged the order.
- `NEW` — order is live on the exchange (working, not yet executing).
- `PARTIALLY_FILLED` — some of `qty` has filled; check `cumQty` and `leavesQty`.
- `FILLED` — the entire order has executed.
- `PENDING_CANCEL` / `CANCELED` — cancel request in progress / completed.
- `PENDING_REPLACE` / `REPLACED` — replace request in progress / completed.
- `REJECTED` — broker refused the order; see `ordRejReason` and `text`.
- `EXPIRED` — order reached its time-in-force limit without filling.
- `STOPPED`, `SUSPENDED`, `DONE_FOR_DAY`, `CALCULATED`, `ACCEPTED_FOR_BID`, `SUPERSEDED` — additional FIX states; rare in normal flows.

## Example Usage

```python
from finance_dev.models import OrdResponseStatus

value = OrdResponseStatus.NEW

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