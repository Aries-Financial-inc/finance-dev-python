# TickResolution

Tick bar size: the number of trades that make up one bar. For example, `100T` closes a new bar every 100 trades, regardless of how much time that takes. Larger values (e.g. `1000T`) smooth out noise and are better suited to a wider chart view; smaller values (e.g. `1T`, one trade per bar) show every individual trade and suit a zoomed-in view.

## Example Usage

```python
from finance_dev.models import TickResolution

value = TickResolution.ONE_T

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                      | Value                     |
| ------------------------- | ------------------------- |
| `ONE_T`                   | 1T                        |
| `FIVE_T`                  | 5T                        |
| `TEN_T`                   | 10T                       |
| `TWENTY_FIVE_T`           | 25T                       |
| `FIFTY_T`                 | 50T                       |
| `ONE_HUNDRED_T`           | 100T                      |
| `TWO_HUNDRED_AND_FIFTY_T` | 250T                      |
| `FIVE_HUNDRED_T`          | 500T                      |
| `ONE_THOUSAND_T`          | 1000T                     |