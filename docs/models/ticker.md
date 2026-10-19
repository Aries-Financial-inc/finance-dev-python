# Ticker


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `day`                                                | [Optional[models.Day]](../models/day.md)             | :heavy_minus_sign:                                   | Current day aggregate                                |
| `last_quote`                                         | [Optional[models.LastQuote]](../models/lastquote.md) | :heavy_minus_sign:                                   | Last quote information                               |
| `last_trade`                                         | [Optional[models.LastTrade]](../models/lasttrade.md) | :heavy_minus_sign:                                   | Last trade information                               |
| `min`                                                | [Optional[models.Min]](../models/min.md)             | :heavy_minus_sign:                                   | Latest minute aggregate                              |
| `prev_day`                                           | [Optional[models.PrevDay]](../models/prevday.md)     | :heavy_minus_sign:                                   | Previous day aggregate                               |
| `ticker`                                             | *Optional[str]*                                      | :heavy_minus_sign:                                   | Ticker symbol                                        |
| `todays_change`                                      | *Optional[float]*                                    | :heavy_minus_sign:                                   | Today's change                                       |
| `todays_change_perc`                                 | *Optional[float]*                                    | :heavy_minus_sign:                                   | Today's change percent                               |
| `updated`                                            | *Optional[int]*                                      | :heavy_minus_sign:                                   | Last updated timestamp                               |