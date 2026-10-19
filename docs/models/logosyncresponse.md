# LogoSyncResponse

Paginated response containing logo records for bulk sync.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `data`                                                                 | List[[models.LogoSyncResponseData](../models/logosyncresponsedata.md)] | :heavy_minus_sign:                                                     | Array of logo records                                                  |
| `has_more`                                                             | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Whether more pages are available                                       |
| `ok`                                                                   | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Request success status                                                 |
| `page`                                                                 | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Current page number                                                    |
| `page_size`                                                            | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Number of records per page                                             |