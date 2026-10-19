# InflationExpectationsResponseResult


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `date_`                                              | *Optional[str]*                                      | :heavy_minus_sign:                                   | Reference date (YYYY-MM-DD)                          |
| `forward_years5_to10`                                | *Optional[float]*                                    | :heavy_minus_sign:                                   | Forward inflation expectation covering years 5 to 10 |
| `market10_year`                                      | *Optional[float]*                                    | :heavy_minus_sign:                                   | Market-implied 10-year inflation expectation         |
| `market5_year`                                       | *Optional[float]*                                    | :heavy_minus_sign:                                   | Market-implied 5-year inflation expectation          |
| `model10_year`                                       | *Optional[float]*                                    | :heavy_minus_sign:                                   | Model-based 10-year inflation expectation            |
| `model1_year`                                        | *Optional[float]*                                    | :heavy_minus_sign:                                   | Model-based 1-year inflation expectation             |
| `model30_year`                                       | *Optional[float]*                                    | :heavy_minus_sign:                                   | Model-based 30-year inflation expectation            |
| `model5_year`                                        | *Optional[float]*                                    | :heavy_minus_sign:                                   | Model-based 5-year inflation expectation             |