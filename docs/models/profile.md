# Profile

Descriptive and fundamental attributes of the ETF.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `asset_class`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | Asset class of the ETF.                                  |
| `aum`                                                    | *Optional[int]*                                          | :heavy_minus_sign:                                       | Assets under management of the ETF.                      |
| `avg_volume`                                             | *Optional[int]*                                          | :heavy_minus_sign:                                       | Average trading volume of the ETF.                       |
| `cusip`                                                  | *Optional[str]*                                          | :heavy_minus_sign:                                       | CUSIP identifier of the ETF.                             |
| `description`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | Text description of the ETF.                             |
| `domicile`                                               | *Optional[str]*                                          | :heavy_minus_sign:                                       | Domicile of the ETF.                                     |
| `etf_company`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | Company that manages or issues the ETF.                  |
| `expense_ratio`                                          | *Optional[float]*                                        | :heavy_minus_sign:                                       | Expense ratio of the ETF.                                |
| `inception_date`                                         | *Optional[str]*                                          | :heavy_minus_sign:                                       | Inception date of the ETF as a string from the provider. |
| `investment_segment`                                     | *Optional[str]*                                          | :heavy_minus_sign:                                       | Investment segment of the ETF.                           |
| `isin`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | ISIN identifier of the ETF.                              |
| `logo`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | URL of the ETF logo image.                               |
| `name`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | Name of the ETF.                                         |
| `nav`                                                    | *Optional[float]*                                        | :heavy_minus_sign:                                       | Net asset value of the ETF.                              |
| `nav_currency`                                           | *Optional[str]*                                          | :heavy_minus_sign:                                       | Currency in which the net asset value is quoted.         |
| `price_to_book`                                          | *Optional[float]*                                        | :heavy_minus_sign:                                       | Price-to-book ratio of the ETF.                          |
| `price_to_earnings`                                      | *Optional[float]*                                        | :heavy_minus_sign:                                       | Price-to-earnings ratio of the ETF.                      |
| `tracking_index`                                         | *Optional[str]*                                          | :heavy_minus_sign:                                       | Index tracked by the ETF.                                |
| `website`                                                | *Optional[str]*                                          | :heavy_minus_sign:                                       | URL of the ETF website.                                  |