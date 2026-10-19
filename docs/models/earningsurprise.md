# EarningSurprise


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `actual`                                      | *Optional[float]*                             | :heavy_minus_sign:                            | Reported actual earnings per share            |
| `estimate`                                    | *Optional[float]*                             | :heavy_minus_sign:                            | Analyst consensus earnings per share estimate |
| `period`                                      | *Optional[str]*                               | :heavy_minus_sign:                            | End date of the reporting period              |
| `quarter`                                     | *Optional[int]*                               | :heavy_minus_sign:                            | Fiscal quarter number                         |
| `surprise`                                    | *Optional[float]*                             | :heavy_minus_sign:                            | Difference between actual and estimate        |
| `surprise_percent`                            | *Optional[float]*                             | :heavy_minus_sign:                            | Surprise as a percentage of the estimate      |
| `symbol`                                      | *Optional[str]*                               | :heavy_minus_sign:                            | Stock ticker symbol                           |
| `year`                                        | *Optional[int]*                               | :heavy_minus_sign:                            | Fiscal year                                   |