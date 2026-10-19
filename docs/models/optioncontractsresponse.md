# OptionContractsResponse

Response containing the call and put option contracts for an underlying symbol and expiration date.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `calls`                                                                      | List[[models.Call](../models/call.md)]                                       | :heavy_minus_sign:                                                           | Call option contracts for the expiration date                                |
| `expiry_date`                                                                | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | Expiration date YYYY-MM-DD                                                   |
| `puts`                                                                       | List[[models.Put](../models/put.md)]                                         | :heavy_minus_sign:                                                           | Put option contracts for the expiration date                                 |
| `symbol`                                                                     | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Underlying symbol                                                            |