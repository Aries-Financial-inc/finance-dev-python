# OptionDetailsDTO

One option contract's pricing snapshot from GET /v1/marketdata/options/details. Numeric prices are returned as JSON numbers.


## Fields

| Field                                    | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `ask_price`                              | *Optional[float]*                        | :heavy_minus_sign:                       | Current best ask price.                  | 80.9                                     |
| `bid_price`                              | *Optional[float]*                        | :heavy_minus_sign:                       | Current best bid price.                  | 78.05                                    |
| `close_price`                            | *Optional[float]*                        | :heavy_minus_sign:                       | Previous session's closing price.        | 93.5                                     |
| `last_price`                             | *Optional[float]*                        | :heavy_minus_sign:                       | Last traded price for the contract.      | 79.76                                    |
| `mid_price`                              | *Optional[float]*                        | :heavy_minus_sign:                       | Midpoint between the bid and ask prices. | 79.475                                   |
| `symbol`                                 | *Optional[str]*                          | :heavy_minus_sign:                       | OSI option symbol for the contract.      | GOOG270115C00285000                      |