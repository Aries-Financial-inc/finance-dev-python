# GetPositionsResponse

Response for GET /v1/accounts/{id}/positions. Cached positions for the account. Numeric amounts are returned as decimal strings.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `positions`                                                  | List[[models.AccountPosition](../models/accountposition.md)] | :heavy_minus_sign:                                           | Open positions for the account                               |