# Market

## Overview

### Available Operations

* [get_etb_list](#get_etb_list) - Get Easy-to-Borrow List
* [search_etb_symbols](#search_etb_symbols) - Search Easy-to-Borrow Symbols
* [get_holidays](#get_holidays) - Get Market Holidays
* [get_status](#get_status) - Get Market Status
* [get_equity_details](#get_equity_details) - Get equity details
* [get_option_details](#get_option_details) - Get option details

## get_etb_list

Returns every symbol on today's easy-to-borrow (ETB) list: the complete set of US equities that can be sold short without first locating shares. A symbol on the list is easy to borrow and can be shorted normally; a symbol absent from it is hard to borrow (HTB) and cannot be shorted without a locate. Absence is a positive answer, not missing data. The list is replaced once per trading day before the market opens and does not change intraday. It is not account-scoped — borrowability is a property of the symbol, so every caller gets the same answer. The response can reach a few hundred KB because the borrowable universe runs to thousands of symbols; fetch it once per trading day and check membership locally, or use POST /v1/etb/search when you only care about a handful of symbols.

### Example Usage: not_loaded

<!-- UsageSnippet language="python" operationID="getEtbList" method="get" path="/v1/etb" example="not_loaded" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market.get_etb_list()

    assert res.etb_list_response is not None

    # Handle response
    print(res.etb_list_response)

```
### Example Usage: success

<!-- UsageSnippet language="python" operationID="getEtbList" method="get" path="/v1/etb" example="success" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market.get_etb_list()

    assert res.etb_list_response is not None

    # Handle response
    print(res.etb_list_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetEtbListResponse](../../models/getetblistresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

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

    res = fd_client.market.search_etb_symbols(symbols=[
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

    res = fd_client.market.search_etb_symbols(symbols=[
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

    res = fd_client.market.search_etb_symbols(symbols=[
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

    res = fd_client.market.search_etb_symbols(symbols=[
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

    res = fd_client.market.search_etb_symbols(symbols=[
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

    res = fd_client.market.search_etb_symbols(symbols=[
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

    res = fd_client.market.search_etb_symbols(symbols=[
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

    res = fd_client.market.search_etb_symbols(symbols=[
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

    res = fd_client.market.search_etb_symbols(symbols=[
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

    res = fd_client.market.search_etb_symbols(symbols=[
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

    res = fd_client.market.search_etb_symbols(symbols=[
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

    res = fd_client.market.search_etb_symbols(symbols=[
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

## get_holidays

Retrieve market holiday schedules showing dates when exchanges are closed for official holidays and early close days.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMarketHolidays" method="get" path="/v1/market/holiday" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market.get_holidays(exchange=models.ExchangeCode.US)

    assert res.market_holiday_response is not None

    # Handle response
    print(res.market_holiday_response)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    | Example                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `exchange`                                                                                                                                     | [models.ExchangeCode](../../models/exchangecode.md)                                                                                            | :heavy_check_mark:                                                                                                                             | exchange code (case-insensitive). Select from the Try it dropdown or use any value from the supported exchange list in the API reference page. | US                                                                                                                                             |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |                                                                                                                                                |

### Response

**[models.GetMarketHolidaysResponse](../../models/getmarketholidaysresponse.md)**

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

## get_status

Retrieve current market status indicating whether exchanges are open, closed, or in pre-market/after-hours trading sessions. Returns 400 when `exchange` is not a supported Finnhub exchange code; the error message lists the supported codes.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMarketStatus" method="get" path="/v1/market/status" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market.get_status(exchange=models.ExchangeCode.US)

    assert res.market_status is not None

    # Handle response
    print(res.market_status)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    | Example                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `exchange`                                                                                                                                     | [models.ExchangeCode](../../models/exchangecode.md)                                                                                            | :heavy_check_mark:                                                                                                                             | exchange code (case-insensitive). Select from the Try it dropdown or use any value from the supported exchange list in the API reference page. | US                                                                                                                                             |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |                                                                                                                                                |

### Response

**[models.GetMarketStatusResponse](../../models/getmarketstatusresponse.md)**

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

## get_equity_details

Batch equity details from an internal cache with an automatic fallback when cached quotes are unavailable. Response includes `data` with per-symbol fields (camelCase: `bidPrice`, `openPrice`, `totalVolume`, etc.); see `EquityDetailsDTO` and `GetEquityDetailsResponse`. At least one symbol is required.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEquityDetails" method="get" path="/v1/marketdata/equities/details" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.market.get_equity_details(symbols="AAPL,MSFT")

    assert res.get_equity_details_response is not None

    # Handle response
    print(res.get_equity_details_response)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          | Example                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbols`                                                                                                                                            | *str*                                                                                                                                                | :heavy_check_mark:                                                                                                                                   | One or more uppercase ticker symbols, separated by commas (e.g. `AAPL,MSFT,GOOGL`). Send at least one. The response order matches the request order. | AAPL,MSFT                                                                                                                                            |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |                                                                                                                                                      |

### Response

**[models.GetEquityDetailsResponseResponse](../../models/getequitydetailsresponseresponse.md)**

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

    res = fd_client.market.get_option_details(symbols="GOOG270115C00285000")

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