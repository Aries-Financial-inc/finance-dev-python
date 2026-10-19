# OrdStatus

Current state of the order. Possible values:
- `PENDING_NEW` — Submitted, waiting for exchange acknowledgement.
- `NEW` — Accepted by the exchange and live in the order book; no fills yet.
- `PARTIALLY_FILLED` — Some of the quantity has executed; the rest is still working. See `cumQty` and `leavesQty`.
- `FILLED` — Fully executed. Order is complete.
- `PENDING_CANCEL` — Cancel request submitted; waiting for exchange confirmation.
- `CANCELED` — Order was cancelled and will not execute further.
- `PENDING_REPLACE` — Replace/modify request submitted; waiting for exchange confirmation.
- `REPLACED` — Order was successfully replaced/modified.
- `REJECTED` — Order was refused (bad parameters, insufficient buying power, halted symbol, etc.). Check `ordRejReason` and `text`.
- `EXPIRED` — Order reached its time-in-force limit without filling (e.g. a `DAY` order that didn't fill before close).
- `DONE_FOR_DAY` — Order is no longer active for today's session but may resume on the next trading day (rare).
- `STOPPED` — Trading was stopped on this order by an exchange action.
- `SUSPENDED` — Order is temporarily suspended by the broker or exchange.
- `CALCULATED` — End-of-day calculated status from FIX (rarely surfaced).
- `ACCEPTED_FOR_BID` — Acknowledged for a bid (auction workflows).
- `SUPERSEDED` — Replaced by a newer record; excluded from history responses server-side.

Omitted when the broker has not yet reported a status.

## Example Usage

```python
from finance_dev.models import OrdStatus

value = OrdStatus.NEW

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