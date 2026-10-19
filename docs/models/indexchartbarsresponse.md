# IndexChartBarsResponse

Response containing chart bars for an index along with the index metadata.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `chart_bars`                                     | List[[models.ChartBar](../models/chartbar.md)]   | :heavy_minus_sign:                               | Array of historical chart bars                   |
| `currency`                                       | *Optional[str]*                                  | :heavy_minus_sign:                               | Currency in which the index is quoted            |
| `index_group`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | Index group classification                       |
| `index_name`                                     | *Optional[str]*                                  | :heavy_minus_sign:                               | Full name of the index                           |
| `symbol`                                         | *Optional[str]*                                  | :heavy_minus_sign:                               | Index ticker symbol                              |
| `timing`                                         | *Optional[str]*                                  | :heavy_minus_sign:                               | Data timing type (RealTime or Delayed)           |
| `valoren`                                        | *Optional[str]*                                  | :heavy_minus_sign:                               | Swiss securities identification number (Valoren) |