# SearchResponse


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `http_meta`                                                            | [models.HTTPMetadata](../models/httpmetadata.md)                       | :heavy_check_mark:                                                     | N/A                                                                    |
| `object`                                                               | [Optional[models.SearchResponseBody]](../models/searchresponsebody.md) | :heavy_minus_sign:                                                     | One page of hits; data.type says which shape they are                  |