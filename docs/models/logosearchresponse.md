# LogoSearchResponse

Response containing logo records that match a search query.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `data`                                                                     | List[[models.LogoSearchResponseData](../models/logosearchresponsedata.md)] | :heavy_minus_sign:                                                         | Array of logo data matching the search query                               |
| `ok`                                                                       | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | Request success status                                                     |