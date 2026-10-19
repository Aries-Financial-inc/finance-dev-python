# IndicesIdentifierType

Which kind of identifier you are sending in `identifier` / `identifiers`. Provide the matching value:
- `Symbol` — index ticker (e.g. `SPX.IND_CBOM`). Default.
- `CIK` — SEC Central Index Key.
- `CUSIP` — 9-character U.S./Canadian security identifier.
- `ISIN` — 12-character international identifier.
- `Valoren` — Swiss security identifier.
- `SEDOL` — 7-character UK identifier.
- `FIGI` — Bloomberg Financial Instrument Global Identifier.
- `CompositeFIGI` — country-level composite FIGI.

## Example Usage

```python
from finance_dev.models import IndicesIdentifierType

value = IndicesIdentifierType.SYMBOL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `SYMBOL`         | Symbol           |
| `CIK`            | CIK              |
| `CUSIP`          | CUSIP            |
| `ISIN`           | ISIN             |
| `VALOREN`        | Valoren          |
| `SEDOL`          | SEDOL            |
| `FIGI`           | FIGI             |
| `COMPOSITE_FIGI` | CompositeFIGI    |