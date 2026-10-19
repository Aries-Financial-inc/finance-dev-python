# VisaApplicationsResponse

H-1B and permanent visa applications filed by a company, as provided by Finnhub.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `data`                                                                                 | List[[models.VisaApplicationsResponseData](../models/visaapplicationsresponsedata.md)] | :heavy_minus_sign:                                                                     | Visa application records for the symbol.                                               |
| `symbol`                                                                               | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Company ticker symbol.                                                                 |