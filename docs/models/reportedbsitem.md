# ReportedBSItem

Single balance sheet line item from a reported filing.


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `concept`                                               | *Optional[str]*                                         | :heavy_minus_sign:                                      | XBRL concept tag identifier for the financial line item |
| `label`                                                 | *Optional[str]*                                         | :heavy_minus_sign:                                      | Human-readable label for the financial line item        |
| `unit`                                                  | *Optional[str]*                                         | :heavy_minus_sign:                                      | Unit of measurement (e.g., USD, shares)                 |
| `value`                                                 | *Optional[float]*                                       | :heavy_minus_sign:                                      | Numerical value of the financial line item              |