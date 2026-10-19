# EpsEstimatesResponseData


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `eps_avg`                                                | *Optional[float]*                                        | :heavy_minus_sign:                                       | Average analyst EPS estimate for the period              |
| `eps_high`                                               | *Optional[float]*                                        | :heavy_minus_sign:                                       | Highest analyst EPS estimate for the period              |
| `eps_low`                                                | *Optional[float]*                                        | :heavy_minus_sign:                                       | Lowest analyst EPS estimate for the period               |
| `number_analysts`                                        | *Optional[int]*                                          | :heavy_minus_sign:                                       | Number of analysts contributing to the estimate          |
| `period`                                                 | *Optional[str]*                                          | :heavy_minus_sign:                                       | End date of the reporting period the estimate applies to |
| `quarter`                                                | *Optional[int]*                                          | :heavy_minus_sign:                                       | Fiscal quarter of the period; 0 for annual estimates     |
| `year`                                                   | *Optional[int]*                                          | :heavy_minus_sign:                                       | Fiscal year of the period                                |