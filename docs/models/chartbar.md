# ChartBar


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `adjustment_ratio`                                   | *Optional[int]*                                      | :heavy_minus_sign:                                   | Price adjustment ratio for corporate actions         |
| `close`                                              | *Optional[float]*                                    | :heavy_minus_sign:                                   | Closing index value for the bar period               |
| `currency`                                           | *Optional[str]*                                      | :heavy_minus_sign:                                   | Currency of the bar data                             |
| `end_date`                                           | *Optional[str]*                                      | :heavy_minus_sign:                                   | Bar end date in MM/DD/YYYY format                    |
| `end_time`                                           | *Optional[str]*                                      | :heavy_minus_sign:                                   | Bar end time in HH:MM:SS AM/PM format                |
| `high`                                               | *Optional[float]*                                    | :heavy_minus_sign:                                   | Highest index value during the bar period            |
| `low`                                                | *Optional[float]*                                    | :heavy_minus_sign:                                   | Lowest index value during the bar period             |
| `open`                                               | *Optional[float]*                                    | :heavy_minus_sign:                                   | Opening index value for the bar period               |
| `session`                                            | *Optional[str]*                                      | :heavy_minus_sign:                                   | Trading session type (Market, PreMarket, PostMarket) |
| `start_date`                                         | *Optional[str]*                                      | :heavy_minus_sign:                                   | Bar start date in MM/DD/YYYY format                  |
| `start_time`                                         | *Optional[str]*                                      | :heavy_minus_sign:                                   | Bar start time in HH:MM:SS AM/PM format              |
| `trades`                                             | *Optional[int]*                                      | :heavy_minus_sign:                                   | Number of trades during the bar period               |
| `twap`                                               | *Optional[float]*                                    | :heavy_minus_sign:                                   | Time-Weighted Average Price for the bar period       |
| `utc_offset`                                         | *Optional[int]*                                      | :heavy_minus_sign:                                   | UTC time offset in hours                             |
| `volume`                                             | *Optional[int]*                                      | :heavy_minus_sign:                                   | Trading volume during the bar period                 |
| `vwap`                                               | *Optional[float]*                                    | :heavy_minus_sign:                                   | Volume-Weighted Average Price for the bar period     |