# EbitdaEstimatesResponseData


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `ebitda_avg`                                             | *Optional[int]*                                          | :heavy_minus_sign:                                       | Average analyst EBITDA estimate for the period           |
| `ebitda_high`                                            | *Optional[int]*                                          | :heavy_minus_sign:                                       | Highest analyst EBITDA estimate for the period           |
| `ebitda_low`                                             | *Optional[int]*                                          | :heavy_minus_sign:                                       | Lowest analyst EBITDA estimate for the period            |
| `number_analysts`                                        | *Optional[int]*                                          | :heavy_minus_sign:                                       | Number of analysts contributing to the estimate          |
| `period`                                                 | *Optional[str]*                                          | :heavy_minus_sign:                                       | End date of the reporting period the estimate applies to |
| `quarter`                                                | *Optional[int]*                                          | :heavy_minus_sign:                                       | Fiscal quarter of the period; 0 for annual estimates     |
| `year`                                                   | *Optional[int]*                                          | :heavy_minus_sign:                                       | Fiscal year of the period                                |