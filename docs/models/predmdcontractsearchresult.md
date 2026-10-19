# PredMdContractSearchResult

One page of contracts.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `found`                                                                              | *int*                                                                                | :heavy_check_mark:                                                                   | Every match, not just this page.                                                     |
| `hits`                                                                               | List[[models.PredMdContractHit](../models/predmdcontracthit.md)]                     | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `page`                                                                               | *int*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `per_page`                                                                           | *int*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `type`                                                                               | [models.PredMdContractSearchResultType](../models/predmdcontractsearchresulttype.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |