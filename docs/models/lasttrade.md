# LastTrade

Last trade information


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `conditions`                                                          | List[*int*]                                                           | :heavy_minus_sign:                                                    | Provider-defined numeric condition codes attached to the last trade.  |
| `exchange_id`                                                         | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Numeric identifier of the exchange where the last trade occurred.     |
| `price`                                                               | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | Price of the last trade.                                              |
| `size`                                                                | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Size of the last trade.                                               |
| `timestamp`                                                           | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Timestamp of the last trade as an integer from the upstream provider. |
| `trade_id`                                                            | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Identifier of the last trade.                                         |