# TechnicalIndicatorResponse

Technical indicator values for a symbol over a time range, as returned by Finnhub; the keys present depend on the requested indicator.


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `sma`                                                 | List[*float*]                                         | :heavy_minus_sign:                                    | Simple moving average values, one per timestamp in t. |
| `t`                                                   | List[*int*]                                           | :heavy_minus_sign:                                    | Timestamps corresponding to each indicator value.     |