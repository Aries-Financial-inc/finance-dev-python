# RevenueBreakdownDataPoint

Revenue for a single segment along a breakdown axis.


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `label`                                       | *Optional[str]*                               | :heavy_minus_sign:                            | Label for the revenue segment                 |
| `member`                                      | *Optional[str]*                               | :heavy_minus_sign:                            | XBRL member identifier for the segment        |
| `percentage`                                  | *Optional[float]*                             | :heavy_minus_sign:                            | Percentage of total revenue from this segment |
| `unit`                                        | *Optional[str]*                               | :heavy_minus_sign:                            | Unit of measurement (e.g., USD)               |
| `value`                                       | *Optional[float]*                             | :heavy_minus_sign:                            | Revenue value for this segment                |