# CongressionalTradingResponseData


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `amount_from`                                               | *Optional[float]*                                           | :heavy_minus_sign:                                          | Lower bound of the reported transaction amount.             |
| `amount_to`                                                 | *Optional[float]*                                           | :heavy_minus_sign:                                          | Upper bound of the reported transaction amount.             |
| `asset_name`                                                | *Optional[str]*                                             | :heavy_minus_sign:                                          | Name of the asset.                                          |
| `filing_date`                                               | *Optional[str]*                                             | :heavy_minus_sign:                                          | Date the disclosure was filed, as returned by the provider. |
| `name`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | Name of the representative.                                 |
| `owner_type`                                                | *Optional[str]*                                             | :heavy_minus_sign:                                          | Type of owner of the asset.                                 |
| `position`                                                  | *Optional[str]*                                             | :heavy_minus_sign:                                          | Position of the representative.                             |
| `symbol`                                                    | *Optional[str]*                                             | :heavy_minus_sign:                                          | Company ticker symbol.                                      |
| `transaction_date`                                          | *Optional[str]*                                             | :heavy_minus_sign:                                          | Date of the transaction, as returned by the provider.       |
| `transaction_type`                                          | *Optional[str]*                                             | :heavy_minus_sign:                                          | Type of transaction, such as Sale or Purchase.              |