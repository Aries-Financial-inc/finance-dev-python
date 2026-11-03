# PredMdElectionRaceStatus

`open` while it trades, `closed` once trading has ended and the result is not yet known, `resolved` once the venue has settled it.

## Example Usage

```python
from finance_dev.models import PredMdElectionRaceStatus

value = PredMdElectionRaceStatus.OPEN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `OPEN`     | open       |
| `CLOSED`   | closed     |
| `RESOLVED` | resolved   |