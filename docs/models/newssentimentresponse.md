# NewsSentimentResponse

News sentiment and buzz metrics for a company from Finnhub.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `buzz`                                               | [Optional[models.Buzz]](../models/buzz.md)           | :heavy_minus_sign:                                   | News buzz metrics for the company.                   |
| `company_news_score`                                 | *Optional[float]*                                    | :heavy_minus_sign:                                   | News score for the company.                          |
| `sector_average_bullish_percent`                     | *Optional[float]*                                    | :heavy_minus_sign:                                   | Average bullish percent across the company's sector. |
| `sector_average_news_score`                          | *Optional[float]*                                    | :heavy_minus_sign:                                   | Average news score across the company's sector.      |
| `sentiment`                                          | [Optional[models.Sentiment]](../models/sentiment.md) | :heavy_minus_sign:                                   | News sentiment breakdown.                            |
| `symbol`                                             | *Optional[str]*                                      | :heavy_minus_sign:                                   | Ticker symbol the sentiment applies to.              |