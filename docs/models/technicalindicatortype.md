# TechnicalIndicatorType

Technical indicator slug (e.g. `sma`, `ema`, `rsi`, `macd`, `bbands`). Pass this with the indicator endpoint to compute that indicator over the requested bars.

## Example Usage

```python
from finance_dev.models import TechnicalIndicatorType

value = TechnicalIndicatorType.SMA

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `SMA`    | sma      |
| `EMA`    | ema      |
| `RSI`    | rsi      |
| `MACD`   | macd     |
| `BBANDS` | bbands   |
| `STOCH`  | stoch    |
| `ADX`    | adx      |
| `CCI`    | cci      |
| `WILLR`  | willr    |
| `MFI`    | mfi      |