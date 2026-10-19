# SocialSentimentResponse

Social media sentiment time series for a symbol.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `data`                                                                               | List[[models.SocialSentimentResponseData](../models/socialsentimentresponsedata.md)] | :heavy_minus_sign:                                                                   | Sentiment data points.                                                               |
| `symbol`                                                                             | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Ticker symbol of the company.                                                        |