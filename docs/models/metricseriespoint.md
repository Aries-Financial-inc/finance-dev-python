# MetricSeriesPoint

Single data point of a company metric time series.


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `period`                                            | *Optional[str]*                                     | :heavy_minus_sign:                                  | Time period for the metric value (e.g., 2023-12-31) |
| `v`                                                 | *Optional[float]*                                   | :heavy_minus_sign:                                  | Metric value for the period                         |