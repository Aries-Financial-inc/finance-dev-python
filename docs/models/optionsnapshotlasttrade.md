# OptionSnapshotLastTrade

Latest trade when included (`OptionSnapshotLastTradeDTO`).


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `conditions`                                                         | List[*int*]                                                          | :heavy_minus_sign:                                                   | Trade condition codes, as supplied by the market data provider       |
| `decimal_size`                                                       | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Trade size as a decimal string, when provided                        |
| `exchange`                                                           | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Numeric exchange identifier supplied by the market data provider.    |
| `price`                                                              | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Trade price                                                          |
| `sip_timestamp`                                                      | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | SIP timestamp of the trade, as supplied by the market data provider  |
| `size`                                                               | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Trade size                                                           |
| `timeframe`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Data timeframe of the trade, as supplied by the market data provider |