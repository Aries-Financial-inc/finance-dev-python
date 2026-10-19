# IndexBarResponseBar

OHLC bar data for the requested time period


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `close`                                                     | *Optional[float]*                                           | :heavy_minus_sign:                                          | Closing index value for the bar period                      |
| `end_date`                                                  | *Optional[str]*                                             | :heavy_minus_sign:                                          | Bar end date in MM/DD/YYYY format                           |
| `end_time`                                                  | *Optional[str]*                                             | :heavy_minus_sign:                                          | Bar end time in HH:MM AM/PM format                          |
| `high`                                                      | *Optional[float]*                                           | :heavy_minus_sign:                                          | Highest index value during the bar period                   |
| `low`                                                       | *Optional[float]*                                           | :heavy_minus_sign:                                          | Lowest index value during the bar period                    |
| `open`                                                      | *Optional[float]*                                           | :heavy_minus_sign:                                          | Opening index value for the bar period                      |
| `start_date`                                                | *Optional[str]*                                             | :heavy_minus_sign:                                          | Bar start date in MM/DD/YYYY format                         |
| `start_time`                                                | *Optional[str]*                                             | :heavy_minus_sign:                                          | Bar start time in HH:MM AM/PM format                        |
| `utc_offset`                                                | *Optional[int]*                                             | :heavy_minus_sign:                                          | UTC time offset in hours (e.g., -5 for EST)                 |
| `volume`                                                    | *Optional[int]*                                             | :heavy_minus_sign:                                          | Trading volume during the bar period (may be 0 for indices) |