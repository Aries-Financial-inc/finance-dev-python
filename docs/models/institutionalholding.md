# InstitutionalHolding

Single holding in an institutional investor's portfolio or in a security's institutional ownership.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `change`                                                          | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Change in share count from previous quarter                       |
| `cusip`                                                           | *Optional[str]*                                                   | :heavy_minus_sign:                                                | CUSIP identifier for the security                                 |
| `name`                                                            | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Name of the security or company                                   |
| `put_call`                                                        | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Type of option position (PUT, CALL, or empty for stock positions) |
| `share`                                                           | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Number of shares held                                             |
| `symbol`                                                          | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Stock ticker symbol                                               |
| `value`                                                           | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Market value of the holding in USD                                |