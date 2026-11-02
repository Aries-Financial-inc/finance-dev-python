# Watchlist

## Overview

### Available Operations

* [replace_all](#replace_all) - Replace All Watchlists
* [get](#get) - Get Watchlist
* [update](#update) - Update Watchlist

## replace_all

Replace the authenticated user's entire set of watchlists in a single call. Send the full desired list as an array: entries matching an existing watchlist by `name` (exact, case-sensitive) are updated in place, keeping their `id` and replacing their `symbols`; entries with a new `name` are created; and every existing watchlist whose `name` is **not** present in the array is deleted. Sending an empty array `[]` deletes all of the user's watchlists and creates a single new `"Default"` watchlist with no symbols.

Unlike Create and Update, symbols sent here are stored as-is and are **not** uppercased or checked against the symbol resolver. If `symbols` is omitted for an entry, that watchlist is stored with `symbols: null`.

### Example Usage: flat

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="flat" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[
        {
            "name": "<value>",
            "symbols": [
                "AAPL",
                "GOOGL",
                "MSFT",
            ],
        },
    ])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```
### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="flat_message" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```
### Example Usage: flat_string

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="flat_string" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="flat_with_codes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```
### Example Usage: nested

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="nested" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[
        {
            "name": "<value>",
            "symbols": [
                "AAPL",
                "GOOGL",
                "MSFT",
            ],
        },
    ])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```
### Example Usage: nested_bad_request

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="nested_bad_request" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[
        {
            "name": "<value>",
            "symbols": [
                "AAPL",
                "GOOGL",
                "MSFT",
            ],
        },
    ])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="nested_error_object" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```
### Example Usage: nested_shared_http_error

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="nested_shared_http_error" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```
### Example Usage: replaceAll

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="replaceAll" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[
        {
            "name": "Tech Stocks",
            "symbols": [
                "AAPL",
                "GOOGL",
                "MSFT",
            ],
        },
        {
            "name": "Finance",
            "symbols": [
                "JPM",
                "BAC",
                "GS",
            ],
        },
    ])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```
### Example Usage: replaced

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="replaced" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[
        {
            "name": "<value>",
            "symbols": [
                "AAPL",
                "GOOGL",
                "MSFT",
            ],
        },
    ])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```
### Example Usage: resetAll

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="resetAll" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```
### Example Usage: resetToDefault

<!-- UsageSnippet language="python" operationID="replaceConfigWatchlists" method="put" path="/v1/config/watchlist" example="resetToDefault" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.replace_all(request=[
        {
            "name": "<value>",
            "symbols": [
                "AAPL",
                "GOOGL",
                "MSFT",
            ],
        },
    ])

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[models.WatchlistRequest]](../../models/.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ReplaceConfigWatchlistsResponse](../../models/replaceconfigwatchlistsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## get

Retrieve a single watchlist owned by the authenticated user, identified by its numeric `watchlist_id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="getConfigWatchlistById" method="get" path="/v1/config/watchlist/{watchlist_id}" example="found" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.get(watchlist_id=12345)

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           | Example                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `watchlist_id`                                                                                                                                        | *int*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | The numeric ID of the watchlist to retrieve. You can get this from a previous list/create/update response (the `id` field in the returned watchlist). | 12345                                                                                                                                                 |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |                                                                                                                                                       |

### Response

**[models.GetConfigWatchlistByIDResponse](../../models/getconfigwatchlistbyidresponse.md)**

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

## update

Partially update a watchlist owned by the authenticated user: rename it, add symbols, remove symbols, or any combination of these. Include at least one of `name`, `add_symbols`, or `remove_symbols`. Renaming to a name the user already uses for another watchlist returns 400 with error code `WATCHLIST_ALREADY_EXISTS`.

**Symbol validation:** Symbols in `add_symbols` are uppercased; symbols already in the watchlist are skipped, and the rest are checked against the symbol resolver. Any that can't be resolved are dropped from the stored list and returned in the response's `invalid_symbols` field. Symbols in `remove_symbols` are uppercased for comparison and removed from the resulting symbol set after additions are applied, so a symbol present in both lists ends up removed.

### Example Usage: addAndRemoveSymbols

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="addAndRemoveSymbols" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: flat

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="flat" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "name": "<value>",
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="flat_message" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: flat_string

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="flat_string" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="flat_with_codes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: nested

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="nested" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: nested_bad_request

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="nested_bad_request" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "name": "<value>",
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="nested_error_object" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: nested_shared_http_error

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="nested_shared_http_error" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "name": "<value>",
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: renameWatchlist

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="renameWatchlist" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "name": "Growth Stocks",
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: renamed

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="renamed" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: symbolsUpdated

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="symbolsUpdated" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: symbolsUpdatedWithInvalid

<!-- UsageSnippet language="python" operationID="updateConfigWatchlistById" method="patch" path="/v1/config/watchlist/{watchlist_id}" example="symbolsUpdatedWithInvalid" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlist.update(watchlist_id=12345, update_watchlist_request={
        "add_symbols": [
            "TSLA",
        ],
        "remove_symbols": [
            "MSFT",
        ],
    })

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         | Example                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `watchlist_id`                                                                                                                                      | *int*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The numeric ID of the watchlist to update. You can get this from a previous list/create/update response (the `id` field in the returned watchlist). | 12345                                                                                                                                               |
| `update_watchlist_request`                                                                                                                          | [models.UpdateWatchlistRequestUnion](../../models/updatewatchlistrequestunion.md)                                                                   | :heavy_check_mark:                                                                                                                                  | At least one of `name`, `add_symbols`, or `remove_symbols` must be included.                                                                        |                                                                                                                                                     |
| `retries`                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                    | :heavy_minus_sign:                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                 |                                                                                                                                                     |

### Response

**[models.UpdateConfigWatchlistByIDResponse](../../models/updateconfigwatchlistbyidresponse.md)**

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