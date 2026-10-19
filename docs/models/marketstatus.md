# MarketStatus

Current trading status of a market.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `exchange`                                                                     | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Exchange code (e.g., US, TO, L)                                                |
| `is_open`                                                                      | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | Whether the market is currently open for trading                               |
| `session`                                                                      | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Current trading session (pre-market, regular, after-hours, or empty if closed) |
| `timestamp`                                                                    | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | Unix timestamp of the status data                                              |
| `timezone`                                                                     | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Timezone of the exchange (e.g., America/New_York)                              |