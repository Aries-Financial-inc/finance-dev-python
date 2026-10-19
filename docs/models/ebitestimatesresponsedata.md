# EbitEstimatesResponseData


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `ebit_avg`                                               | *Optional[int]*                                          | :heavy_minus_sign:                                       | Average analyst EBIT estimate for the period             |
| `ebit_high`                                              | *Optional[int]*                                          | :heavy_minus_sign:                                       | Highest analyst EBIT estimate for the period             |
| `ebit_low`                                               | *Optional[int]*                                          | :heavy_minus_sign:                                       | Lowest analyst EBIT estimate for the period              |
| `number_analysts`                                        | *Optional[int]*                                          | :heavy_minus_sign:                                       | Number of analysts contributing to the estimate          |
| `period`                                                 | *Optional[str]*                                          | :heavy_minus_sign:                                       | End date of the reporting period the estimate applies to |
| `quarter`                                                | *Optional[int]*                                          | :heavy_minus_sign:                                       | Fiscal quarter of the period; 0 for annual estimates     |
| `year`                                                   | *Optional[int]*                                          | :heavy_minus_sign:                                       | Fiscal year of the period                                |