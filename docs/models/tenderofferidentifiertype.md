# TenderOfferIdentifierType

Which kind of identifier you are filtering by. Provide the matching value in the identifier field:
- `Symbol` — exchange ticker (e.g. `AAPL`).
- `CUSIP` — 9-character U.S./Canadian security identifier.
- `ISIN` — 12-character international identifier.
- `SEDOL` — 7-character UK identifier.
- `Valoren` — Swiss identifier.
- `FIGI` — Bloomberg Financial Instrument Global Identifier.
- `CompositeFIGI` — country-level composite FIGI.

## Example Usage

```python
from finance_dev.models import TenderOfferIdentifierType

value = TenderOfferIdentifierType.SYMBOL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `SYMBOL`         | Symbol           |
| `CUSIP`          | CUSIP            |
| `ISIN`           | ISIN             |
| `SEDOL`          | SEDOL            |
| `VALOREN`        | Valoren          |
| `FIGI`           | FIGI             |
| `COMPOSITE_FIGI` | CompositeFIGI    |