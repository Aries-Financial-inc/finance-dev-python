# Sector

Which industry sector to list tickers for. Use the exact uppercase value (including spaces) — these match the values returned by [GET /v1/equity/sector-wise-change](/api-reference/analytics/equity-sector-wise-change).
- `TECHNOLOGY` — software, hardware, semiconductors
- `HEALTHCARE` — pharma, biotech, medical devices, providers
- `FINANCIAL SERVICES` — banks, insurance, asset managers
- `CONSUMER CYCLICAL` — discretionary spending (autos, retail, travel)
- `CONSUMER DEFENSIVE` — staples (food, household goods, drugstores)
- `INDUSTRIALS` — manufacturing, transport, defense, machinery
- `ENERGY` — oil & gas, renewable energy
- `UTILITIES` — power, water, gas distribution
- `BASIC MATERIALS` — mining, chemicals, paper, metals
- `COMMUNICATION SERVICES` — telecom, media, internet platforms
- `REAL ESTATE` — REITs and real-estate operators
- `OTHER` — uncategorized
- `NONE` — no sector classification

## Example Usage

```python
from finance_dev.models import Sector

value = Sector.HEALTHCARE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                     | Value                    |
| ------------------------ | ------------------------ |
| `HEALTHCARE`             | HEALTHCARE               |
| `UTILITIES`              | UTILITIES                |
| `CONSUMER_CYCLICAL`      | CONSUMER CYCLICAL        |
| `INDUSTRIALS`            | INDUSTRIALS              |
| `CONSUMER_DEFENSIVE`     | CONSUMER DEFENSIVE       |
| `BASIC_MATERIALS`        | BASIC MATERIALS          |
| `COMMUNICATION_SERVICES` | COMMUNICATION SERVICES   |
| `FINANCIAL_SERVICES`     | FINANCIAL SERVICES       |
| `TECHNOLOGY`             | TECHNOLOGY               |
| `REAL_ESTATE`            | REAL ESTATE              |
| `NONE`                   | NONE                     |
| `OTHER`                  | OTHER                    |
| `ENERGY`                 | ENERGY                   |