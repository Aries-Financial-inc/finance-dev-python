# PriceTargetResponse

Analyst price target consensus for a stock (high, low, mean, median and analyst count), sourced from Finnhub.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `last_updated`                                              | *Optional[str]*                                             | :heavy_minus_sign:                                          | Time the consensus was last updated, as reported by Finnhub |
| `number_analysts`                                           | *Optional[int]*                                             | :heavy_minus_sign:                                          | Number of analysts contributing to the consensus            |
| `symbol`                                                    | *Optional[str]*                                             | :heavy_minus_sign:                                          | Stock ticker symbol                                         |
| `target_high`                                               | *Optional[float]*                                           | :heavy_minus_sign:                                          | Highest analyst price target                                |
| `target_low`                                                | *Optional[float]*                                           | :heavy_minus_sign:                                          | Lowest analyst price target                                 |
| `target_mean`                                               | *Optional[float]*                                           | :heavy_minus_sign:                                          | Mean analyst price target                                   |
| `target_median`                                             | *Optional[float]*                                           | :heavy_minus_sign:                                          | Median analyst price target                                 |