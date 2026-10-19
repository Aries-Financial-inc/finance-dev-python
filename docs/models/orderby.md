# OrderBy

Sort direction by `order_created_at`. Defaults to `desc` (newest first). Use `asc` for chronological exports.

## Example Usage

```python
from finance_dev.models import OrderBy

value = OrderBy.ASC

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `ASC`  | asc    |
| `DESC` | desc   |