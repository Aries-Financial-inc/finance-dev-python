# GetElectionMapResponse


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `http_meta`                                                                            | [models.HTTPMetadata](../models/httpmetadata.md)                                       | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `object`                                                                               | [Optional[models.GetElectionMapResponseBody]](../models/getelectionmapresponsebody.md) | :heavy_minus_sign:                                                                     | The election map. Gzipped when the request sends `Accept-Encoding: gzip`.              |