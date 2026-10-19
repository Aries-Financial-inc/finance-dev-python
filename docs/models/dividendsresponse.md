# DividendsResponse

Paginated response containing dividend events.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `next_url`                                                                      | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Opaque pagination URL for the next page of results when more data is available. |
| `request_id`                                                                    | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Provider request identifier for tracing and support.                            |
| `results`                                                                       | List[[models.DividendItem](../models/dividenditem.md)]                          | :heavy_minus_sign:                                                              | Array of dividend payment events.                                               |
| `status`                                                                        | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Provider response status.                                                       |