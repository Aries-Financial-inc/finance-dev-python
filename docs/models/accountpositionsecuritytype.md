# AccountPositionSecurityType

Indicates whether the position is an equity/stock position or an option position. Use this value to decide which position details and actions should be shown in the UI.
- `EQUITY` — a stock or ETF position.
- `OPTION` — an option contract position.

## Example Usage

```python
from finance_dev.models import AccountPositionSecurityType

value = AccountPositionSecurityType.EQUITY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `EQUITY` | EQUITY   |
| `OPTION` | OPTION   |