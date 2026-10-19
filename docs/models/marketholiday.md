# MarketHoliday

Market holiday or special trading day.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `at_date`                                                                             | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)          | :heavy_minus_sign:                                                                    | Date of the holiday in YYYY-MM-DD format                                              |
| `event_name`                                                                          | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Name of the holiday or special market event                                           |
| `trading_hour`                                                                        | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Trading hours for the day (e.g., 09:30-13:00 for early close, empty for full closure) |