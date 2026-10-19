# SocialSentimentResponseData


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `at_time`                                                   | *Optional[str]*                                             | :heavy_minus_sign:                                          | Timestamp of the data point as provided by the data vendor. |
| `mention`                                                   | *Optional[int]*                                             | :heavy_minus_sign:                                          | Total number of mentions.                                   |
| `negative_mention`                                          | *Optional[int]*                                             | :heavy_minus_sign:                                          | Number of negative mentions.                                |
| `negative_score`                                            | *Optional[float]*                                           | :heavy_minus_sign:                                          | Negative sentiment score.                                   |
| `positive_mention`                                          | *Optional[int]*                                             | :heavy_minus_sign:                                          | Number of positive mentions.                                |
| `positive_score`                                            | *Optional[float]*                                           | :heavy_minus_sign:                                          | Positive sentiment score.                                   |
| `score`                                                     | *Optional[float]*                                           | :heavy_minus_sign:                                          | Overall sentiment score.                                    |