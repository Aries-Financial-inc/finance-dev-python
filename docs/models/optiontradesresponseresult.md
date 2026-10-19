# OptionTradesResponseResult


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `conditions`                                                      | List[*int*]                                                       | :heavy_minus_sign:                                                | Trade conditions                                                  |
| `correction`                                                      | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Correction indicator                                              |
| `exchange`                                                        | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Numeric exchange identifier supplied by the market data provider. |
| `participant_timestamp`                                           | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Participant timestamp (nanoseconds)                               |
| `price`                                                           | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Trade price                                                       |
| `sip_timestamp`                                                   | *Optional[int]*                                                   | :heavy_minus_sign:                                                | SIP timestamp (nanoseconds)                                       |
| `size`                                                            | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Trade size (contracts)                                            |