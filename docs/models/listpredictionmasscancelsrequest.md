# ListPredictionMassCancelsRequest


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   | Example                                                       |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `account_id`                                                  | *str*                                                         | :heavy_check_mark:                                            | The account. Every order on it is covered, whoever placed it. | ACCOUNT-0001                                                  |
| `limit`                                                       | *Optional[int]*                                               | :heavy_minus_sign:                                            | Mass cancels per page. Values above 200 are clamped to 200.   |                                                               |
| `cursor`                                                      | *Optional[str]*                                               | :heavy_minus_sign:                                            | `nextCursor` from the previous page.                          |                                                               |