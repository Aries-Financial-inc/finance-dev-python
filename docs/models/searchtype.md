# SearchType

Level hits come back at. `contracts` (default) returns matching contracts; `events` returns one hit per event and `base-events` one per base event, each ranked by its best-matching contract and carrying only its own fields and a count of matching contracts. Echoed in the response.

## Example Usage

```python
from finance_dev.models import SearchType

value = SearchType.CONTRACTS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `CONTRACTS`   | contracts     |
| `EVENTS`      | events        |
| `BASE_EVENTS` | base-events   |