# RevenueBreakdownAxis

Revenue breakdown along a single dimension such as product or geography.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `axis`                                                                           | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | XBRL axis identifier (e.g., product line, geography)                             |
| `data`                                                                           | List[[models.RevenueBreakdownDataPoint](../models/revenuebreakdowndatapoint.md)] | :heavy_minus_sign:                                                               | Array of revenue data points for this axis                                       |
| `label`                                                                          | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Human-readable label for the axis                                                |