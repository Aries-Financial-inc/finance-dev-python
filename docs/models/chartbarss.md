# ChartBarsS

Response status. `ok` means chart arrays are usable; `no_data` means the symbol or range returned no bars; `error` means read `errmsg`.

## Example Usage

```python
from finance_dev.models import ChartBarsS

value = ChartBarsS.OK

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `OK`      | ok        |
| `NO_DATA` | no_data   |
| `ERROR`   | error     |