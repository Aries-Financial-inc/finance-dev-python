# TradeOrderLegV2SecurityType

Instrument type for this leg. EQUITY is stock or ETF; OPTION is an options contract.

## Example Usage

```python
from finance_dev.models import TradeOrderLegV2SecurityType

value = TradeOrderLegV2SecurityType.EQUITY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `EQUITY` | EQUITY   |
| `OPTION` | OPTION   |