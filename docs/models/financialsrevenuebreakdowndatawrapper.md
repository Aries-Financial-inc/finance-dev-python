# FinancialsRevenueBreakdownDataWrapper

Company identifiers and revenue breakdown entries from SEC filings.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `cik`                                                                    | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Central Index Key assigned by the SEC.                                   |
| `data`                                                                   | List[[models.RevenueBreakdownEntry](../models/revenuebreakdownentry.md)] | :heavy_minus_sign:                                                       | Revenue breakdown entries by filing.                                     |
| `symbol`                                                                 | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Stock ticker symbol.                                                     |