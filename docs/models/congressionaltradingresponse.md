# CongressionalTradingResponse

Stock transactions disclosed by members of US Congress for a company, as provided by Finnhub.


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `data`                                                                                         | List[[models.CongressionalTradingResponseData](../models/congressionaltradingresponsedata.md)] | :heavy_minus_sign:                                                                             | Congressional transaction disclosures for the symbol.                                          |
| `symbol`                                                                                       | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Company ticker symbol.                                                                         |