# OptionExpiryDatesResponse

Response containing the option expiration dates for an underlying symbol.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `expiry_dates`                                                                     | List[[datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)] | :heavy_minus_sign:                                                                 | List of expiration dates in YYYY-MM-DD format                                      |
| `symbol`                                                                           | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Underlying symbol                                                                  |