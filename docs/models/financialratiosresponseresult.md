# FinancialRatiosResponseResult


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `average_volume`                                      | *Optional[int]*                                       | :heavy_minus_sign:                                    | Average trading volume in shares                      |
| `cash`                                                | *Optional[float]*                                     | :heavy_minus_sign:                                    | Cash ratio                                            |
| `cik`                                                 | *Optional[str]*                                       | :heavy_minus_sign:                                    | SEC Central Index Key of the company                  |
| `current`                                             | *Optional[float]*                                     | :heavy_minus_sign:                                    | Current ratio (current assets to current liabilities) |
| `date_`                                               | *Optional[str]*                                       | :heavy_minus_sign:                                    | Date the ratios were calculated for (YYYY-MM-DD)      |
| `debt_to_equity`                                      | *Optional[float]*                                     | :heavy_minus_sign:                                    | Debt-to-equity ratio                                  |
| `dividend_yield`                                      | *Optional[float]*                                     | :heavy_minus_sign:                                    | Dividend yield                                        |
| `earnings_per_share`                                  | *Optional[float]*                                     | :heavy_minus_sign:                                    | Earnings per share                                    |
| `enterprise_value`                                    | *Optional[int]*                                       | :heavy_minus_sign:                                    | Enterprise value                                      |
| `ev_to_ebitda`                                        | *Optional[float]*                                     | :heavy_minus_sign:                                    | Enterprise value to EBITDA ratio                      |
| `ev_to_sales`                                         | *Optional[float]*                                     | :heavy_minus_sign:                                    | Enterprise value to sales ratio                       |
| `free_cash_flow`                                      | *Optional[int]*                                       | :heavy_minus_sign:                                    | Free cash flow                                        |
| `market_cap`                                          | *Optional[int]*                                       | :heavy_minus_sign:                                    | Market capitalization                                 |
| `price`                                               | *Optional[float]*                                     | :heavy_minus_sign:                                    | Stock price used to compute the ratios                |
| `price_to_book`                                       | *Optional[float]*                                     | :heavy_minus_sign:                                    | Price-to-book (P/B) ratio                             |
| `price_to_cash_flow`                                  | *Optional[float]*                                     | :heavy_minus_sign:                                    | Price-to-cash-flow ratio                              |
| `price_to_earnings`                                   | *Optional[float]*                                     | :heavy_minus_sign:                                    | Price-to-earnings (P/E) ratio                         |
| `price_to_free_cash_flow`                             | *Optional[float]*                                     | :heavy_minus_sign:                                    | Price-to-free-cash-flow ratio                         |
| `price_to_sales`                                      | *Optional[float]*                                     | :heavy_minus_sign:                                    | Price-to-sales (P/S) ratio                            |
| `quick`                                               | *Optional[float]*                                     | :heavy_minus_sign:                                    | Quick ratio (liquid assets to current liabilities)    |
| `return_on_assets`                                    | *Optional[float]*                                     | :heavy_minus_sign:                                    | Return on assets                                      |
| `return_on_equity`                                    | *Optional[float]*                                     | :heavy_minus_sign:                                    | Return on equity                                      |
| `ticker`                                              | *Optional[str]*                                       | :heavy_minus_sign:                                    | Stock ticker symbol                                   |