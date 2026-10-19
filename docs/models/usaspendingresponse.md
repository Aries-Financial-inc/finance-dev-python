# UsaSpendingResponse

US government contract awards to a company, as provided by Finnhub.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `data`                                                                       | List[[models.UsaSpendingResponseData](../models/usaspendingresponsedata.md)] | :heavy_minus_sign:                                                           | Government spending (award) records for the symbol.                          |
| `symbol`                                                                     | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Company ticker symbol.                                                       |