# ListCategoriesResponse


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `http_meta`                                                                            | [models.HTTPMetadata](../models/httpmetadata.md)                                       | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `object`                                                                               | [Optional[models.ListCategoriesResponseBody]](../models/listcategoriesresponsebody.md) | :heavy_minus_sign:                                                                     | The category tree; empty when no contract is active                                    |