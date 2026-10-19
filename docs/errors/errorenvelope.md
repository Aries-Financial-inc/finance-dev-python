# ErrorEnvelope

Prediction-market error envelope. Returned by historical-data and prediction-market reference endpoints on 400/404/500/502.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `error`                                                          | [models.AppError](../models/apperror.md)                         | :heavy_check_mark:                                               | Structured application error returned inside an `ErrorEnvelope`. |                                                                  |
| `success`                                                        | *bool*                                                           | :heavy_check_mark:                                               | N/A                                                              | false                                                            |
| `http_meta`                                                      | [models.HTTPMetadata](../models/httpmetadata.md)                 | :heavy_check_mark:                                               | N/A                                                              |                                                                  |