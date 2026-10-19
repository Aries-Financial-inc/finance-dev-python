# InflationResponseResult


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `cpi`                                | *Optional[float]*                    | :heavy_minus_sign:                   | Consumer Price Index                 |
| `cpi_core`                           | *Optional[float]*                    | :heavy_minus_sign:                   | Core CPI (excluding food and energy) |
| `cpi_year_over_year`                 | *Optional[float]*                    | :heavy_minus_sign:                   | CPI year-over-year change            |
| `date_`                              | *Optional[str]*                      | :heavy_minus_sign:                   | Reference date (YYYY-MM-DD)          |
| `pce`                                | *Optional[float]*                    | :heavy_minus_sign:                   | Personal Consumption Expenditures    |
| `pce_core`                           | *Optional[float]*                    | :heavy_minus_sign:                   | Core PCE                             |
| `pce_spending`                       | *Optional[float]*                    | :heavy_minus_sign:                   | PCE spending                         |