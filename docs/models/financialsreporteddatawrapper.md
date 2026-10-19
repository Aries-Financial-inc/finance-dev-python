# FinancialsReportedDataWrapper

Company identifiers and the list of reported SEC filings.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `cik`                                                      | *Optional[str]*                                            | :heavy_minus_sign:                                         | Central Index Key assigned by the SEC                      |
| `data`                                                     | List[[models.ReportedFiling](../models/reportedfiling.md)] | :heavy_minus_sign:                                         | Array of reported filings with financial data              |
| `symbol`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | Stock ticker symbol                                        |