# PredMdHistoryRequest

Single query within a batch historical-data request.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Inclusive lower bound. Zero/omitted means unbounded.                 | 2026-04-01T00:00:00Z                                                 |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | 0 or omitted means 10000; values above 10000 are clamped to it.      | 500                                                                  |
| `symbol`                                                             | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  | HORC_1126_Republican                                                 |
| `to`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Inclusive upper bound. Zero/omitted means unbounded.                 | 2026-04-20T00:00:00Z                                                 |