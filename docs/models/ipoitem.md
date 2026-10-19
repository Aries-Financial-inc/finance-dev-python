# IpoItem

A single IPO calendar entry.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `date_`                                          | *Optional[str]*                                  | :heavy_minus_sign:                               | Expected or actual IPO date in YYYY-MM-DD format |
| `exchange`                                       | *Optional[str]*                                  | :heavy_minus_sign:                               | Stock exchange where the IPO will list           |
| `name`                                           | *Optional[str]*                                  | :heavy_minus_sign:                               | Company name                                     |
| `price_from`                                     | *Optional[float]*                                | :heavy_minus_sign:                               | Minimum price per share in the IPO price range   |
| `price_to`                                       | *Optional[float]*                                | :heavy_minus_sign:                               | Maximum price per share in the IPO price range   |
| `status`                                         | *Optional[str]*                                  | :heavy_minus_sign:                               | IPO status (expected, priced, filed, withdrawn)  |
| `symbol`                                         | *Optional[str]*                                  | :heavy_minus_sign:                               | Stock ticker symbol for the IPO                  |
| `total_shares_value`                             | *Optional[float]*                                | :heavy_minus_sign:                               | Total value of shares offered in the IPO         |