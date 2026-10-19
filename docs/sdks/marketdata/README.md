# MarketData

## Overview

### Available Operations

* [search_symbols](#search_symbols) - Search Symbols

## search_symbols

Search for trading symbols including stocks, indices, options, and futures. **Prefixes:** '.' searches options (e.g. '.AAPL'); '/' searches futures (e.g. '/ES'). Without a prefix, searches stocks and indices together, merges matches, ranks them, and returns at most `limit` results. The '!' character is **not** a special prefix—only '.' and '/' are. Default limit is 20 if omitted (max 100).

### Example Usage: futures

<!-- UsageSnippet language="python" operationID="searchMarketSymbols" method="get" path="/v1/marketdata/search" example="futures" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_symbols(query="/ES", limit=20)

    assert res.search_symbol_response is not None

    # Handle response
    print(res.search_symbol_response)

```
### Example Usage: option

<!-- UsageSnippet language="python" operationID="searchMarketSymbols" method="get" path="/v1/marketdata/search" example="option" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_symbols(query=".AAPL", limit=20)

    assert res.search_symbol_response is not None

    # Handle response
    print(res.search_symbol_response)

```
### Example Usage: stock

<!-- UsageSnippet language="python" operationID="searchMarketSymbols" method="get" path="/v1/marketdata/search" example="stock" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_symbols(query="AAPL", limit=20)

    assert res.search_symbol_response is not None

    # Handle response
    print(res.search_symbol_response)

```

### Parameters

| Parameter                                                                                                                                                                                                     | Type                                                                                                                                                                                                          | Required                                                                                                                                                                                                      | Description                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                            | Text the user entered in symbol search. Use `AAPL` for stocks and indices, `.AAPL` for option-chain style searches, and `/ES` for futures. Do not use `!` as a special prefix; it is treated as literal text. |
| `limit`                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                            | Maximum number of matches to return. Use a small number for autocomplete and a larger number for full search pages. Default is 20; minimum is 1; maximum is 100.                                              |
| `retries`                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                           |

### Response

**[models.SearchMarketSymbolsResponse](../../models/searchmarketsymbolsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 404                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 404                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |