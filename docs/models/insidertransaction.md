# InsiderTransaction

Single insider trading transaction reported on SEC Form 4.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `change`                                                         | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Net change in shares held after the transaction                  |
| `filing_date`                                                    | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Date when the Form 4 was filed with the SEC in YYYY-MM-DD format |
| `name`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Name of the insider (executive, director, or beneficial owner)   |
| `share`                                                          | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Number of shares involved in the transaction                     |
| `symbol`                                                         | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Stock ticker symbol                                              |
| `transaction_code`                                               | *Optional[str]*                                                  | :heavy_minus_sign:                                               | SEC transaction code (P=Purchase, S=Sale, A=Award, etc.)         |
| `transaction_date`                                               | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Date when the transaction occurred in YYYY-MM-DD format          |
| `transaction_price`                                              | *Optional[float]*                                                | :heavy_minus_sign:                                               | Price per share at which the transaction was executed            |