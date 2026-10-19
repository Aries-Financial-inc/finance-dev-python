# CompanyEsgResponse

Latest ESG (environmental, social, governance) scores and disclosures for a company.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `data`                                                                         | [Optional[models.CompanyEsgResponseData]](../models/companyesgresponsedata.md) | :heavy_minus_sign:                                                             | Detailed ESG disclosures and metrics.                                          |
| `environment_score`                                                            | *Optional[float]*                                                              | :heavy_minus_sign:                                                             | Environmental score.                                                           |
| `governance_score`                                                             | *Optional[float]*                                                              | :heavy_minus_sign:                                                             | Governance score.                                                              |
| `social_score`                                                                 | *Optional[float]*                                                              | :heavy_minus_sign:                                                             | Social score.                                                                  |
| `symbol`                                                                       | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Ticker symbol of the company.                                                  |
| `total_esg_score`                                                              | *Optional[float]*                                                              | :heavy_minus_sign:                                                             | Total ESG score.                                                               |