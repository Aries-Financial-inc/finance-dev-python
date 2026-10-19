# GetNewsByIDRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | Unique news item ID (must be numeric)                                    | 123456                                                                   |
| `news_type`                                                              | [models.NewsTypeEnum](../models/newstypeenum.md)                         | :heavy_check_mark:                                                       | Type of news item to retrieve. Must be either 'news' or 'press_release'. | news                                                                     |