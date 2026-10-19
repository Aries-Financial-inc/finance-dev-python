# FilingsSimilarityIndexDataWrapper

Similarity index data for a company, identified by CIK and symbol.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `cik`                                                                      | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Central Index Key                                                          |
| `similarity`                                                               | List[[models.FilingSimilarityRecord](../models/filingsimilarityrecord.md)] | :heavy_minus_sign:                                                         | Array of filing similarity records with cosine similarity scores           |
| `symbol`                                                                   | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Stock ticker symbol                                                        |