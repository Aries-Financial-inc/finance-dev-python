# GetUnifiedSnapshotType

Asset class filter for unified snapshot.

## Example Usage

```python
from finance_dev.models import GetUnifiedSnapshotType

value = GetUnifiedSnapshotType.STOCKS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `STOCKS`  | stocks    |
| `OPTIONS` | options   |
| `FX`      | fx        |
| `CRYPTO`  | crypto    |
| `INDICES` | indices   |