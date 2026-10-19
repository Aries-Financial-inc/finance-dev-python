# RevenueEstimatesResponseData


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `number_analysts`                                        | *Optional[int]*                                          | :heavy_minus_sign:                                       | Number of analysts contributing to the estimate          |
| `period`                                                 | *Optional[str]*                                          | :heavy_minus_sign:                                       | End date of the reporting period the estimate applies to |
| `quarter`                                                | *Optional[int]*                                          | :heavy_minus_sign:                                       | Fiscal quarter of the period; 0 for annual estimates     |
| `revenue_avg`                                            | *Optional[int]*                                          | :heavy_minus_sign:                                       | Average analyst revenue estimate for the period          |
| `revenue_high`                                           | *Optional[int]*                                          | :heavy_minus_sign:                                       | Highest analyst revenue estimate for the period          |
| `revenue_low`                                            | *Optional[int]*                                          | :heavy_minus_sign:                                       | Lowest analyst revenue estimate for the period           |
| `year`                                                   | *Optional[int]*                                          | :heavy_minus_sign:                                       | Fiscal year of the period                                |