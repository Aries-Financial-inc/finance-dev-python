# Holding


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `asset_type`                                                 | *Optional[str]*                                              | :heavy_minus_sign:                                           | Asset type of the holding.                                   |
| `cusip`                                                      | *Optional[str]*                                              | :heavy_minus_sign:                                           | CUSIP identifier of the holding.                             |
| `isin`                                                       | *Optional[str]*                                              | :heavy_minus_sign:                                           | ISIN identifier of the holding.                              |
| `name`                                                       | *Optional[str]*                                              | :heavy_minus_sign:                                           | Name of the holding.                                         |
| `percent`                                                    | *Optional[float]*                                            | :heavy_minus_sign:                                           | Portfolio weight of the holding as reported by the provider. |
| `share`                                                      | *Optional[int]*                                              | :heavy_minus_sign:                                           | Number of shares held.                                       |
| `symbol`                                                     | *Optional[str]*                                              | :heavy_minus_sign:                                           | Ticker symbol of the holding.                                |
| `value`                                                      | *Optional[int]*                                              | :heavy_minus_sign:                                           | Market value of the holding as reported by the provider.     |