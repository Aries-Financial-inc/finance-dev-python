# BankBranchesResponse

List of US bank branches for a company, as provided by Finnhub.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `data`                                                                         | List[[models.BankBranchesResponseData](../models/bankbranchesresponsedata.md)] | :heavy_minus_sign:                                                             | Bank branches for the symbol.                                                  |
| `symbol`                                                                       | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Company ticker symbol.                                                         |