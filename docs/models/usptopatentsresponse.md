# UsptoPatentsResponse

USPTO patent filings associated with a company, as provided by Finnhub.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `data`                                                                         | List[[models.UsptoPatentsResponseData](../models/usptopatentsresponsedata.md)] | :heavy_minus_sign:                                                             | Patent records for the symbol.                                                 |
| `symbol`                                                                       | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Company ticker symbol.                                                         |