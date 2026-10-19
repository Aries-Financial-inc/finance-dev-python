# RevenueBreakdownInner

Total revenue for a reporting period with its breakdown by axis.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `concept`                                                              | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | XBRL concept tag for revenue                                           |
| `end_date`                                                             | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | End date of the reporting period in YYYY-MM-DD format                  |
| `revenue_breakdown`                                                    | List[[models.RevenueBreakdownAxis](../models/revenuebreakdownaxis.md)] | :heavy_minus_sign:                                                     | Array of revenue breakdown axes (by product, geography, etc.)          |
| `start_date`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Start date of the reporting period in YYYY-MM-DD format                |
| `unit`                                                                 | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Unit of measurement (e.g., USD)                                        |
| `value`                                                                | *Optional[float]*                                                      | :heavy_minus_sign:                                                     | Total revenue value                                                    |