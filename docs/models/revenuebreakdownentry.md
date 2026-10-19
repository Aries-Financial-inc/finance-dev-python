# RevenueBreakdownEntry

Revenue breakdown for a single SEC filing.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `access_number`                                                              | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | SEC accession number for the filing                                          |
| `breakdown`                                                                  | [Optional[models.RevenueBreakdownInner]](../models/revenuebreakdowninner.md) | :heavy_minus_sign:                                                           | Total revenue for a reporting period with its breakdown by axis.             |