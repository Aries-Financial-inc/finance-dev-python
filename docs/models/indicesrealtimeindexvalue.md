# IndicesRealtimeIndexValue

Realtime OHLC and change fields for an index quote.


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `change_from_open`                                            | *Optional[float]*                                             | :heavy_minus_sign:                                            | Change in the index value from the session open.              |
| `change_from_previous_close`                                  | *Optional[float]*                                             | :heavy_minus_sign:                                            | Change in the index value from the previous close.            |
| `close`                                                       | *Optional[float]*                                             | :heavy_minus_sign:                                            | Current / last close value                                    |
| `date_`                                                       | *Optional[str]*                                               | :heavy_minus_sign:                                            | Session date in source format (locale-specific)               |
| `high`                                                        | *Optional[float]*                                             | :heavy_minus_sign:                                            | Highest index value for the session.                          |
| `high52_weeks`                                                | *Optional[float]*                                             | :heavy_minus_sign:                                            | 52-week high                                                  |
| `last`                                                        | *Optional[float]*                                             | :heavy_minus_sign:                                            | Last traded value                                             |
| `low`                                                         | *Optional[float]*                                             | :heavy_minus_sign:                                            | Lowest index value for the session.                           |
| `low52_weeks`                                                 | *Optional[float]*                                             | :heavy_minus_sign:                                            | 52-week low                                                   |
| `open`                                                        | *Optional[float]*                                             | :heavy_minus_sign:                                            | Opening value of the index for the session.                   |
| `percent_change_from_open`                                    | *Optional[float]*                                             | :heavy_minus_sign:                                            | Percentage change in the index value from the session open.   |
| `percent_change_from_previous_close`                          | *Optional[float]*                                             | :heavy_minus_sign:                                            | Percentage change in the index value from the previous close. |
| `previous_close`                                              | *Optional[float]*                                             | :heavy_minus_sign:                                            | Closing value of the index on the previous trading day.       |
| `previous_close_date`                                         | *Optional[str]*                                               | :heavy_minus_sign:                                            | Prior close date in source format                             |
| `time`                                                        | *Optional[str]*                                               | :heavy_minus_sign:                                            | Quote time in source format                                   |
| `utc_offset`                                                  | *Optional[int]*                                               | :heavy_minus_sign:                                            | UTC offset in hours                                           |
| `volume`                                                      | *Optional[int]*                                               | :heavy_minus_sign:                                            | Volume (may be 0 for some indices)                            |