# IndexBarResponse

Response containing a single OHLC bar for an index along with the index metadata.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `bar`                                                                        | [Optional[models.IndexBarResponseBar]](../models/indexbarresponsebar.md)     | :heavy_minus_sign:                                                           | OHLC bar data for the requested time period                                  |
| `index`                                                                      | [Optional[models.IndexBarResponseIndex]](../models/indexbarresponseindex.md) | :heavy_minus_sign:                                                           | Index metadata and identification                                            |