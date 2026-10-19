# TimeInForceEnum

How long the order should stay alive before automatically cancelling. Pick one:
- `DAY` — Active until the end of today's regular trading session, then cancelled if not filled. The default choice for most orders.
- `GTC` — Good 'Til Cancelled. Stays open across multiple trading days until you cancel it (the broker may cap at 60–90 days).
- `IOC` — Immediate Or Cancel. Fill whatever you can right now; cancel the rest immediately. Useful when you want partial fills but no resting order.
- `FOK` — Fill Or Kill. Fill the entire order immediately, or cancel it entirely. No partial fills allowed.
- `EXTENDED_HOURS` — Active during pre-market and after-hours trading sessions in addition to regular hours.
- `AT_THE_OPENING` — Execute at the official market open price; if it can't fill at open, it's cancelled.
- `AT_THE_CLOSE` — Execute at the official market close price; if it can't fill at close, it's cancelled.

## Example Usage

```python
from finance_dev.models import TimeInForceEnum

value = TimeInForceEnum.DAY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `DAY`            | DAY              |
| `GTC`            | GTC              |
| `IOC`            | IOC              |
| `FOK`            | FOK              |
| `EXTENDED_HOURS` | EXTENDED_HOURS   |
| `AT_THE_OPENING` | AT_THE_OPENING   |
| `AT_THE_CLOSE`   | AT_THE_CLOSE     |