# PredOrdersOrderPage


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `next_cursor`                                                     | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Pass as `cursor` to fetch the next page. Absent on the last page. |
| `orders`                                                          | List[[models.PredOrdersOrder](../models/predordersorder.md)]      | :heavy_check_mark:                                                | N/A                                                               |