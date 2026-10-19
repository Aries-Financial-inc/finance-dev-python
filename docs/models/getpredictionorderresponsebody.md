# GetPredictionOrderResponseBody

Standard success envelope used by all success responses. `data` is endpoint-specific.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `data`                                                                       | [Optional[models.PredOrdersOrderDetail]](../models/predordersorderdetail.md) | :heavy_minus_sign:                                                           | An order and every venue report against it, read from one snapshot.          |                                                                              |
| `success`                                                                    | *bool*                                                                       | :heavy_check_mark:                                                           | N/A                                                                          | true                                                                         |