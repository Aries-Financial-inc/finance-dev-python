# QuotesResponseS

Overall quote response status. `ok` means quote data was returned; `error` means the request could not be fulfilled.

## Example Usage

```python
from finance_dev.models import QuotesResponseS

value = QuotesResponseS.OK

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name    | Value   |
| ------- | ------- |
| `OK`    | ok      |
| `ERROR` | error   |