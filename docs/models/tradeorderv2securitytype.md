# TradeOrderV2SecurityType

Instrument type for the order. EQUITY is stock or ETF; OPTION is an options contract.

## Example Usage

```python
from finance_dev.models import TradeOrderV2SecurityType

value = TradeOrderV2SecurityType.EQUITY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `EQUITY` | EQUITY   |
| `OPTION` | OPTION   |