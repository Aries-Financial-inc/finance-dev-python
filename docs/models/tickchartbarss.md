# TickChartBarsS

Response status. `ok` means chart arrays are usable; `no_data` means no matching trade activity was found; `error` means read `errmsg`.

## Example Usage

```python
from finance_dev.models import TickChartBarsS

value = TickChartBarsS.OK

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `OK`      | ok        |
| `NO_DATA` | no_data   |
| `ERROR`   | error     |