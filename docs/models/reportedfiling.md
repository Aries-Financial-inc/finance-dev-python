# ReportedFiling

SEC filing with its reporting period and reported financial data.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `accepted_date`                                                | *Optional[str]*                                                | :heavy_minus_sign:                                             | Date and time when the SEC accepted the filing                 |
| `access_number`                                                | *Optional[str]*                                                | :heavy_minus_sign:                                             | SEC accession number uniquely identifying the filing           |
| `cik`                                                          | *Optional[str]*                                                | :heavy_minus_sign:                                             | Central Index Key assigned by the SEC to the company           |
| `end_date`                                                     | *Optional[str]*                                                | :heavy_minus_sign:                                             | End date of the reporting period in YYYY-MM-DD format          |
| `filed_date`                                                   | *Optional[str]*                                                | :heavy_minus_sign:                                             | Date when the filing was submitted to the SEC                  |
| `form`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | Type of SEC form (e.g., 10-K, 10-Q, 8-K)                       |
| `quarter`                                                      | *Optional[int]*                                                | :heavy_minus_sign:                                             | Fiscal quarter number (1-4)                                    |
| `report`                                                       | [Optional[models.ReportedReport]](../models/reportedreport.md) | :heavy_minus_sign:                                             | Financial statements reported within a filing.                 |
| `start_date`                                                   | *Optional[str]*                                                | :heavy_minus_sign:                                             | Start date of the reporting period in YYYY-MM-DD format        |
| `symbol`                                                       | *Optional[str]*                                                | :heavy_minus_sign:                                             | Stock ticker symbol                                            |
| `year`                                                         | *Optional[int]*                                                | :heavy_minus_sign:                                             | Fiscal year of the report                                      |