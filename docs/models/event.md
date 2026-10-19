# Event


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `event`                                                        | *Optional[str]*                                                | :heavy_minus_sign:                                             | Title of the earnings call event.                              |
| `live_audio`                                                   | *Optional[str]*                                                | :heavy_minus_sign:                                             | URL of the live audio stream for the call.                     |
| `quarter`                                                      | *Optional[int]*                                                | :heavy_minus_sign:                                             | Fiscal quarter of the earnings call.                           |
| `recording`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | URL of the recorded audio of the call.                         |
| `symbol`                                                       | *Optional[str]*                                                | :heavy_minus_sign:                                             | Ticker symbol of the company.                                  |
| `time`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | Timestamp of the earnings call as provided by the data vendor. |
| `year`                                                         | *Optional[int]*                                                | :heavy_minus_sign:                                             | Fiscal year of the earnings call.                              |