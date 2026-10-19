# PredMdEventSearchResult

One page of events. found, page and perPage count events.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `found`                                                                        | *int*                                                                          | :heavy_check_mark:                                                             | Every match, not just this page.                                               |
| `hits`                                                                         | List[[models.PredMdEventHit](../models/predmdeventhit.md)]                     | :heavy_check_mark:                                                             | N/A                                                                            |
| `page`                                                                         | *int*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `per_page`                                                                     | *int*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `type`                                                                         | [models.PredMdEventSearchResultType](../models/predmdeventsearchresulttype.md) | :heavy_check_mark:                                                             | N/A                                                                            |