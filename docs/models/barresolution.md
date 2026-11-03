# BarResolution

Bar size: minutes (`1`, `5`, `15`, `30`, `60`), or daily, weekly, or monthly (`D`, `W`, `M`).

## Example Usage

```python
from finance_dev.models import BarResolution

value = BarResolution.ONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ONE`     | 1         |
| `FIVE`    | 5         |
| `FIFTEEN` | 15        |
| `THIRTY`  | 30        |
| `SIXTY`   | 60        |
| `D`       | D         |
| `W`       | W         |
| `M`       | M         |