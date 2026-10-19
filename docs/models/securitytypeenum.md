# SecurityTypeEnum

What kind of instrument the order is for. Pick one:
- `CS` — Common Stock (equity / ETF).
- `OPT` — Option contract (call or put).

## Example Usage

```python
from finance_dev.models import SecurityTypeEnum

value = SecurityTypeEnum.CS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name  | Value |
| ----- | ----- |
| `CS`  | CS    |
| `OPT` | OPT   |