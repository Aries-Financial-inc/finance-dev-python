# HistoricalEsgResponse

Historical ESG (environmental, social, governance) scores and disclosures for a company by period.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `data`                                                                           | List[[models.HistoricalEsgResponseData](../models/historicalesgresponsedata.md)] | :heavy_minus_sign:                                                               | ESG records by period.                                                           |
| `symbol`                                                                         | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Ticker symbol of the company.                                                    |