# OwnershipRecord

Ownership record of an institutional investor or fund in a security.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `change`                                           | *Optional[int]*                                    | :heavy_minus_sign:                                 | Change in share count from previous filing         |
| `filing_date`                                      | *Optional[str]*                                    | :heavy_minus_sign:                                 | Date of the regulatory filing in YYYY-MM-DD format |
| `name`                                             | *Optional[str]*                                    | :heavy_minus_sign:                                 | Name of the institutional investor or fund         |
| `percent_of_shares`                                | *Optional[float]*                                  | :heavy_minus_sign:                                 | Percentage of total outstanding shares held        |
| `share`                                            | *Optional[int]*                                    | :heavy_minus_sign:                                 | Number of shares held                              |
| `source`                                           | *Optional[str]*                                    | :heavy_minus_sign:                                 | Source of the ownership data (e.g., 13F, 13G)      |