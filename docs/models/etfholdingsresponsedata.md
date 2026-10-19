# EtfHoldingsResponseData

ETF holdings payload.


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `holdings`                                   | List[[models.Holding](../models/holding.md)] | :heavy_minus_sign:                           | List of holdings in the ETF.                 |
| `number_of_holdings`                         | *Optional[int]*                              | :heavy_minus_sign:                           | Total number of holdings in the ETF.         |
| `symbol`                                     | *Optional[str]*                              | :heavy_minus_sign:                           | ETF ticker symbol.                           |