# PredOrdersErrorEnvelope

Invalid request. `INVALID_ORDER` carries the reason in `message`; on placement this includes refusals from order entry and the venue (price, tick size, account setup).


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `error`                                                             | [models.PredOrdersAppError](../models/predordersapperror.md)        | :heavy_check_mark:                                                  | Structured error returned by the prediction-market order endpoints. |                                                                     |
| `success`                                                           | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | false                                                               |
| `http_meta`                                                         | [models.HTTPMetadata](../models/httpmetadata.md)                    | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |