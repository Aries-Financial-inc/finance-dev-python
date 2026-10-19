# PaidSecurity

Security paid to holders who tender


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `cik`                                                     | *Optional[str]*                                           | :heavy_minus_sign:                                        | SEC Central Index Key (CIK) of the issuer                 |
| `composite_figi`                                          | *Optional[str]*                                           | :heavy_minus_sign:                                        | Composite FIGI of the security                            |
| `cusip`                                                   | *Optional[str]*                                           | :heavy_minus_sign:                                        | CUSIP of the security                                     |
| `figi`                                                    | *Optional[str]*                                           | :heavy_minus_sign:                                        | FIGI of the security                                      |
| `industry`                                                | *Optional[str]*                                           | :heavy_minus_sign:                                        | Industry of the issuer                                    |
| `instrument_class`                                        | *Optional[str]*                                           | :heavy_minus_sign:                                        | Instrument class of the security                          |
| `isin`                                                    | *Optional[str]*                                           | :heavy_minus_sign:                                        | ISIN of the security                                      |
| `market`                                                  | *Optional[str]*                                           | :heavy_minus_sign:                                        | Market the security trades on                             |
| `market_identification_code`                              | *Optional[str]*                                           | :heavy_minus_sign:                                        | Market Identification Code (MIC) of the security's market |
| `name`                                                    | *Optional[str]*                                           | :heavy_minus_sign:                                        | Name of the security                                      |
| `sector`                                                  | *Optional[str]*                                           | :heavy_minus_sign:                                        | Sector of the issuer                                      |
| `sedol`                                                   | *Optional[str]*                                           | :heavy_minus_sign:                                        | SEDOL of the security                                     |
| `symbol`                                                  | *Optional[str]*                                           | :heavy_minus_sign:                                        | Ticker symbol of the security                             |
| `valoren`                                                 | *Optional[str]*                                           | :heavy_minus_sign:                                        | Valoren number of the security                            |