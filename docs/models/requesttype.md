# RequestType

`all` when no `symbol` was given, otherwise `by_security`.

## Example Usage

```python
from finance_dev.models import RequestType

value = RequestType.ALL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `ALL`         | all           |
| `BY_SECURITY` | by_security   |