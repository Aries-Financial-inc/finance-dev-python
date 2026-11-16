# MarketData

## Overview

### Available Operations

* [search_etb_symbols](#search_etb_symbols) - Search Easy-to-Borrow Symbols
* [get_option_details](#get_option_details) - Get option details
* [search_symbols](#search_symbols) - Search Symbols

## search_etb_symbols

Answers borrowability for a batch of symbols. Use this instead of fetching the whole list when you only care about a handful — for example, deciding whether to show a short-sell option on a ticker page. This is a POST rather than a GET because a symbol list has no practical URL-length limit. Symbols are uppercased and trimmed before the lookup and duplicates collapse, so `count` can be lower than the number of symbols you sent; always read answers out of `results` by uppercase key rather than matching them against your request array by index. Reads the same underlying set as GET /v1/etb, so the two endpoints can never disagree.

### Example Usage: duplicatesCollapse

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="duplicatesCollapse" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "aapl",
        " AAPL ",
        "AAPL",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```
### Example Usage: flat

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="flat" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "AAPL",
        "GME",
        "msft",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```
### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="flat_message" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "AAPL",
        "GME",
        "msft",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```
### Example Usage: flat_string

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="flat_string" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "AAPL",
        "GME",
        "msft",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="flat_with_codes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "AAPL",
        "GME",
        "msft",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```
### Example Usage: invalid_body

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="invalid_body" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "AAPL",
        "GME",
        "msft",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```
### Example Usage: missing_body

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="missing_body" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "AAPL",
        "GME",
        "msft",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```
### Example Usage: missing_symbols

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="missing_symbols" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "AAPL",
        "GME",
        "msft",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```
### Example Usage: mixedCase

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="mixedCase" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "AAPL",
        "GME",
        "msft",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```
### Example Usage: nested

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="nested" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "AAPL",
        "GME",
        "msft",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="nested_error_object" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "AAPL",
        "GME",
        "msft",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```
### Example Usage: too_many_symbols

<!-- UsageSnippet language="python" operationID="searchEtbSymbols" method="post" path="/v1/etb/search" example="too_many_symbols" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.search_etb_symbols(symbols=[
        "AAPL",
        "GME",
        "msft",
    ])

    assert res.etb_search_response is not None

    # Handle response
    print(res.etb_search_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbols`                                                                                                                                                                                                                                            | List[*str*]                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                   | Symbols to check. Case-insensitive and whitespace-trimmed, so `aapl`, ` AAPL `, and `AAPL` are the same symbol and return one entry. A request of only blank strings is rejected with 400 MISSING_SYMBOLS rather than answered with an empty result. | [<br/>"AAPL",<br/>"GME",<br/>"msft"<br/>]                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                  |                                                                                                                                                                                                                                                      |

### Response

**[models.SearchEtbSymbolsResponse](../../models/searchetbsymbolsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get_option_details

Batch option contract details for one or more OSI option symbols. Response includes `data` with per-symbol pricing fields (`lastPrice`, `bidPrice`, `askPrice`, `midPrice`, `closePrice`) and an `errors` array for symbols that cannot be returned. At least one symbol is required.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOptionDetails" method="get" path="/v1/marketdata/options/details" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market_data.get_option_details(symbols="GOOG270115C00285000")

    assert res.get_option_details_response is not None

    # Handle response
    print(res.get_option_details_response)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        | Example                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbols`                                                                                                                                          | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | One or more OSI option symbols, separated by commas (e.g. `GOOG270115C00285000`). Send at least one. The response order matches the request order. | GOOG270115C00285000                                                                                                                                |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |                                                                                                                                                    |

### Response

**[models.GetOptionDetailsResponseResponse](../../models/getoptiondetailsresponseresponse.md)**

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