# GetInsiderTransactionsRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `symbol`                                                                       | *str*                                                                          | :heavy_check_mark:                                                             | Stock symbol, such as AAPL. Use it to narrow results to one company.           |
| `from_`                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)   | :heavy_minus_sign:                                                             | Optional start date in YYYY-MM-DD format. Use it to begin the research window. |
| `to`                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)   | :heavy_minus_sign:                                                             | Optional end date in YYYY-MM-DD format. Use it to end the research window.     |