# Watchlists

## Overview

### Available Operations

* [list](#list) - List Watchlists
* [create](#create) - Create Watchlist
* [delete](#delete) - Delete Watchlist

## list

List all watchlists owned by the authenticated user. Users normally always have at least one watchlist; if the user has none, this endpoint returns 500 rather than an empty list.

### Example Usage

<!-- UsageSnippet language="python" operationID="getConfigWatchlists" method="get" path="/v1/config/watchlist" example="watchlists" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.list()

    assert res.watchlist_response is not None

    # Handle response
    print(res.watchlist_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetConfigWatchlistsResponse](../../models/getconfigwatchlistsresponse.md)**

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

## create

Create a new watchlist for the authenticated user. Watchlist names must be unique per user; creating a watchlist with a name the user already has returns 400 with error code `WATCHLIST_ALREADY_EXISTS`.

**Symbol validation:** Submitted symbols are uppercased, de-duplicated, and checked against the symbol resolver. Symbols that can't be resolved are dropped from the stored list and returned in the response's `invalid_symbols` field instead of causing the request to fail.

### Example Usage: createWatchlist

<!-- UsageSnippet language="python" operationID="createConfigWatchlist" method="post" path="/v1/config/watchlist" example="createWatchlist" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.create(name="Tech Stocks", symbols=[
        "AAPL",
        "GOOGL",
        "MSFT",
    ])

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: created

<!-- UsageSnippet language="python" operationID="createConfigWatchlist" method="post" path="/v1/config/watchlist" example="created" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.create(name="<value>", symbols=[
        "AAPL",
        "GOOGL",
        "MSFT",
    ])

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: createdWithInvalidSymbols

<!-- UsageSnippet language="python" operationID="createConfigWatchlist" method="post" path="/v1/config/watchlist" example="createdWithInvalidSymbols" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.create(name="<value>", symbols=[
        "AAPL",
        "GOOGL",
        "MSFT",
    ])

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: flat

<!-- UsageSnippet language="python" operationID="createConfigWatchlist" method="post" path="/v1/config/watchlist" example="flat" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.create(name="<value>", symbols=[
        "AAPL",
        "GOOGL",
        "MSFT",
    ])

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: flat_message

<!-- UsageSnippet language="python" operationID="createConfigWatchlist" method="post" path="/v1/config/watchlist" example="flat_message" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.create(name="<value>", symbols=[
        "AAPL",
        "GOOGL",
        "MSFT",
    ])

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: flat_string

<!-- UsageSnippet language="python" operationID="createConfigWatchlist" method="post" path="/v1/config/watchlist" example="flat_string" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.create(name="<value>", symbols=[
        "AAPL",
        "GOOGL",
        "MSFT",
    ])

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: flat_with_codes

<!-- UsageSnippet language="python" operationID="createConfigWatchlist" method="post" path="/v1/config/watchlist" example="flat_with_codes" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.create(name="<value>", symbols=[
        "AAPL",
        "GOOGL",
        "MSFT",
    ])

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: nested

<!-- UsageSnippet language="python" operationID="createConfigWatchlist" method="post" path="/v1/config/watchlist" example="nested" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.create(name="<value>", symbols=[
        "AAPL",
        "GOOGL",
        "MSFT",
    ])

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: nested_bad_request

<!-- UsageSnippet language="python" operationID="createConfigWatchlist" method="post" path="/v1/config/watchlist" example="nested_bad_request" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.create(name="<value>", symbols=[
        "AAPL",
        "GOOGL",
        "MSFT",
    ])

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: nested_error_object

<!-- UsageSnippet language="python" operationID="createConfigWatchlist" method="post" path="/v1/config/watchlist" example="nested_error_object" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.create(name="<value>", symbols=[
        "AAPL",
        "GOOGL",
        "MSFT",
    ])

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: nested_shared_http_error

<!-- UsageSnippet language="python" operationID="createConfigWatchlist" method="post" path="/v1/config/watchlist" example="nested_shared_http_error" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.create(name="<value>", symbols=[
        "AAPL",
        "GOOGL",
        "MSFT",
    ])

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```

### Parameters

| Parameter                                                                                                                                                                                        | Type                                                                                                                                                                                             | Required                                                                                                                                                                                         | Description                                                                                                                                                                                      | Example                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`                                                                                                                                                                                           | *str*                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                               | User-facing name for the new watchlist, such as Tech Stocks or Dividend Ideas. Must not match the name of another watchlist the user already has (case-sensitive).                               |                                                                                                                                                                                                  |
| `symbols`                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                               | Symbols to save in the new watchlist. Use exact uppercase ticker symbols; symbols that can't be resolved are dropped from the saved list and returned in the response's `invalid_symbols` field. | [<br/>"AAPL",<br/>"GOOGL",<br/>"MSFT"<br/>]                                                                                                                                                      |
| `retries`                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                              |                                                                                                                                                                                                  |

### Response

**[models.CreateConfigWatchlistResponse](../../models/createconfigwatchlistresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.AuthenticationErrorEnvelope | 400                                | application/json                   |
| errors.ErrorResponse               | 400                                | application/json                   |
| errors.ErrorResponse               | 401                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 401                                | application/json                   |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.ErrorResponse               | 500                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 500                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## delete

Delete one of the user's watchlists by its numeric ID.

**Important — last-watchlist rule:** If this is the user's *only remaining* watchlist, the server does not actually delete it. Instead it **resets it to a default empty state** (name set to `"Default"`, `symbols` cleared) so the user always has at least one watchlist available in the UI.

**Tip:** The response body returns the affected watchlist — whether it was actually deleted or reset — so you can update your local store without making a follow-up GET request. Compare `name` and `symbols` in the response to decide whether to render the 'reset to default' state.

### Example Usage: deleted

<!-- UsageSnippet language="python" operationID="deleteConfigWatchlistById" method="delete" path="/v1/config/watchlist/{watchlist_id}" example="deleted" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.delete(watchlist_id=12345)

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```
### Example Usage: resetToDefault

<!-- UsageSnippet language="python" operationID="deleteConfigWatchlistById" method="delete" path="/v1/config/watchlist/{watchlist_id}" example="resetToDefault" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.watchlists.delete(watchlist_id=12345)

    assert res.watchlist is not None

    # Handle response
    print(res.watchlist)

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         | Example                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `watchlist_id`                                                                                                                                      | *int*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The numeric ID of the watchlist to delete. You can get this from a previous list/create/update response (the `id` field in the returned watchlist). | 12345                                                                                                                                               |
| `retries`                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                    | :heavy_minus_sign:                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                 |                                                                                                                                                     |

### Response

**[models.DeleteConfigWatchlistByIDResponse](../../models/deleteconfigwatchlistbyidresponse.md)**

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