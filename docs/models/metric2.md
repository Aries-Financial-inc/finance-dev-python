# Metric2

Current financial metrics and ratios (dynamic object with various metric keys)


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `ten_day_average_trading_volume`                                     | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Average daily trading volume over the last 10 days                   |
| `fifty_two_week_high`                                                | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Highest stock price in the last 52 weeks                             |
| `fifty_two_week_low`                                                 | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Lowest stock price in the last 52 weeks                              |
| `fifty_two_week_low_date`                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Date when the 52-week low was reached                                |
| `fifty_two_week_price_return_daily`                                  | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Price return over the last 52 weeks (daily calculation)              |
| `beta`                                                               | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Stock's beta coefficient measuring volatility relative to the market |
| `fifty_two_week_high_date`                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Date when the 52-week high was reached                               |
| `__pydantic_extra__`                                                 | Dict[str, [Nullable[models.Metric1]](../models/metric1.md)]          | :heavy_minus_sign:                                                   | N/A                                                                  |