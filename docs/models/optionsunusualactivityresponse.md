# OptionsUnusualActivityResponse

Response for GET /v1/options/unusual_activity/{symbol}. Contains unusual activity trades and optional pagination pointer.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `next_page`                                                                          | *OptionalNullable[str]*                                                              | :heavy_minus_sign:                                                                   | Absolute link to the next page when more results are available.                      |
| `trades`                                                                             | List[[models.OptionsUnusualActivityTrade](../models/optionsunusualactivitytrade.md)] | :heavy_minus_sign:                                                                   | List of unusual options activity trades                                              |