# GetAggregateTechnicalIndicatorsResolution

How long each bar covers. Supported values are minutes (`1`, `5`, `15`, `30`, `60`) or daily/weekly/monthly (`D`, `W`, `M`). Other values return 400 Bad Request with error code `VALIDATION_ERROR`.

## Example Usage

```python
from finance_dev.models import GetAggregateTechnicalIndicatorsResolution

value = GetAggregateTechnicalIndicatorsResolution.ONE

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