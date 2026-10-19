# GetAnalystInsightsSearchKeysType

Tells the API how to interpret the value you send in `searchKeys`. Allowed values:
- `firm_id` — the value is a firm/company internal ID.
- `firm` — the value is the firm/company name.

## Example Usage

```python
from finance_dev.models import GetAnalystInsightsSearchKeysType

value = GetAnalystInsightsSearchKeysType.FIRM_ID

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `FIRM_ID` | firm_id   |
| `FIRM`    | firm      |