# OptionSnapshotContractDetails

Static contract metadata (`OptionSnapshotDetailsDTO`).


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `contract_type`                                                   | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Contract type (for example call or put).                          |
| `exercise_style`                                                  | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Exercise style of the contract (for example american or european) |
| `expiration_date`                                                 | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Expiration date (ISO date string).                                |
| `shares_per_contract`                                             | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Number of shares of the underlying covered by one contract        |
| `strike_price`                                                    | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Strike price of the contract                                      |
| `ticker`                                                          | *Optional[str]*                                                   | :heavy_minus_sign:                                                | OCC-format options ticker.                                        |