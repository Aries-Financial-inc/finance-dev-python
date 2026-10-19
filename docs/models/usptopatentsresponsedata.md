# UsptoPatentsResponseData


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `application_number`                                        | *Optional[str]*                                             | :heavy_minus_sign:                                          | Patent application number.                                  |
| `company_filing_name`                                       | List[*str*]                                                 | :heavy_minus_sign:                                          | Names of the companies listed on the patent.                |
| `description`                                               | *Optional[str]*                                             | :heavy_minus_sign:                                          | Description of the patent.                                  |
| `filing_date`                                               | *Optional[str]*                                             | :heavy_minus_sign:                                          | Date the patent was filed, as returned by the provider.     |
| `filing_status`                                             | *Optional[str]*                                             | :heavy_minus_sign:                                          | Filing status of the patent.                                |
| `patent_number`                                             | *Optional[str]*                                             | :heavy_minus_sign:                                          | Patent number.                                              |
| `patent_type`                                               | *Optional[str]*                                             | :heavy_minus_sign:                                          | Type of patent.                                             |
| `publication_date`                                          | *Optional[str]*                                             | :heavy_minus_sign:                                          | Date the patent was published, as returned by the provider. |
| `url`                                                       | *Optional[str]*                                             | :heavy_minus_sign:                                          | URL of the original patent document.                        |