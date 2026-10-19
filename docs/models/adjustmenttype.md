# AdjustmentType

Type of stock split adjustment

## Example Usage

```python
from finance_dev.models import AdjustmentType

value = AdjustmentType.FORWARD_SPLIT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `FORWARD_SPLIT`  | forward_split    |
| `REVERSE_SPLIT`  | reverse_split    |
| `STOCK_DIVIDEND` | stock_dividend   |