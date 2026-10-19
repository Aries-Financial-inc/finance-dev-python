# FinancialsStatementsDataWrapper

Symbol and list of standardized financial statements by period.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `financials`                                                       | List[[models.FinancialStatement](../models/financialstatement.md)] | :heavy_minus_sign:                                                 | Array of financial statements for different periods                |
| `symbol`                                                           | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Stock ticker symbol                                                |