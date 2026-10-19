# FilingSimilarityRecord

Cosine similarity scores between a filing and the prior comparable filing, by 10-K section.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `accepted_date`                                            | *Optional[str]*                                            | :heavy_minus_sign:                                         | Date when the SEC accepted the filing                      |
| `access_number`                                            | *Optional[str]*                                            | :heavy_minus_sign:                                         | SEC accession number                                       |
| `cik`                                                      | *Optional[str]*                                            | :heavy_minus_sign:                                         | Central Index Key                                          |
| `filed_date`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | Date when filed with SEC                                   |
| `filing_url`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | URL to the complete filing                                 |
| `form`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | Type of SEC form                                           |
| `item1`                                                    | *Optional[float]*                                          | :heavy_minus_sign:                                         | Cosine similarity score for Item 1 (Business) section      |
| `item1a`                                                   | *Optional[float]*                                          | :heavy_minus_sign:                                         | Cosine similarity score for Item 1A (Risk Factors) section |
| `item2`                                                    | *Optional[float]*                                          | :heavy_minus_sign:                                         | Cosine similarity score for Item 2 (Properties) section    |
| `item7`                                                    | *Optional[float]*                                          | :heavy_minus_sign:                                         | Cosine similarity score for Item 7 (MD&A) section          |
| `item7a`                                                   | *Optional[float]*                                          | :heavy_minus_sign:                                         | Cosine similarity score for Item 7A (Market Risk) section  |
| `report_url`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | URL to the formatted report                                |