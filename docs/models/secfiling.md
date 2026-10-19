# SecFiling

A single SEC filing with its accession number, form type, dates and document URLs.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `accepted_date`                                      | *Optional[str]*                                      | :heavy_minus_sign:                                   | Date and time when the SEC accepted the filing       |
| `access_number`                                      | *Optional[str]*                                      | :heavy_minus_sign:                                   | SEC accession number uniquely identifying the filing |
| `cik`                                                | *Optional[str]*                                      | :heavy_minus_sign:                                   | Central Index Key assigned by the SEC                |
| `filed_date`                                         | *Optional[str]*                                      | :heavy_minus_sign:                                   | Date when the filing was submitted to the SEC        |
| `filing_url`                                         | *Optional[str]*                                      | :heavy_minus_sign:                                   | URL to the complete filing on SEC EDGAR              |
| `form`                                               | *Optional[str]*                                      | :heavy_minus_sign:                                   | Type of SEC form (e.g., 10-K, 10-Q, 8-K)             |
| `report_url`                                         | *Optional[str]*                                      | :heavy_minus_sign:                                   | URL to the formatted report document                 |
| `symbol`                                             | *Optional[str]*                                      | :heavy_minus_sign:                                   | Stock ticker symbol                                  |