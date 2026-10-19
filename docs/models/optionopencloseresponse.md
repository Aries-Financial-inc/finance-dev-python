# OptionOpenCloseResponse

Daily open, high, low, close and volume for an option contract on a given date, including pre-market and after-hours prices.


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `after_hours`                                       | *Optional[float]*                                   | :heavy_minus_sign:                                  | Last traded price in after-hours session            |
| `close`                                             | *Optional[float]*                                   | :heavy_minus_sign:                                  | Closing price for the trading session               |
| `date_`                                             | *Optional[str]*                                     | :heavy_minus_sign:                                  | Trade date in YYYY-MM-DD format                     |
| `high`                                              | *Optional[float]*                                   | :heavy_minus_sign:                                  | Highest price reached during the trading session    |
| `low`                                               | *Optional[float]*                                   | :heavy_minus_sign:                                  | Lowest price reached during the trading session     |
| `open`                                              | *Optional[float]*                                   | :heavy_minus_sign:                                  | Opening price for the trading session               |
| `pre_market`                                        | *Optional[float]*                                   | :heavy_minus_sign:                                  | Last traded price in pre-market session             |
| `ticker`                                            | *Optional[str]*                                     | :heavy_minus_sign:                                  | OCC option ticker symbol                            |
| `volume`                                            | *Optional[float]*                                   | :heavy_minus_sign:                                  | Total number of contracts traded during the session |