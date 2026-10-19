# Predictions.Markets

## Overview

### Available Operations

* [get_base_event](#get_base_event) - Get a base event with its events and each event's contracts
* [list_categories](#list_categories) - List prediction market categories
* [get_event_contracts](#get_event_contracts) - Get an event and all contracts under it
* [search](#search) - Search contracts, events or base events

## get_base_event

Get a base event with its events and each event's contracts

### Example Usage

<!-- UsageSnippet language="python" operationID="getBaseEvent" method="get" path="/v1/predictions/base-events/{baseEventId}" -->
```python
from finance_dev import FinanceDev


with FinanceDev() as fd_client:

    res = fd_client.predictions.markets.get_base_event(base_event_id="UNR")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `base_event_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | UNR                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetBaseEventResponse](../../models/getbaseeventresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorEnvelope | 400, 404             | application/json     |
| errors.ErrorEnvelope | 500                  | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## list_categories

The category tree of every category with at least one ACTIVE contract, so each one finds something when passed to search as category. Each level is ordered by name. Read from the search index, which trails the catalogue by seconds.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCategories" method="get" path="/v1/predictions/categories" -->
```python
from finance_dev import FinanceDev


with FinanceDev() as fd_client:

    res = fd_client.predictions.markets.list_categories()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListCategoriesResponse](../../models/listcategoriesresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorEnvelope | 502                  | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## get_event_contracts

Get an event and all contracts under it

### Example Usage

<!-- UsageSnippet language="python" operationID="getEventContracts" method="get" path="/v1/predictions/events/{eventId}/contracts" -->
```python
from finance_dev import FinanceDev


with FinanceDev() as fd_client:

    res = fd_client.predictions.markets.get_event_contracts(event_id="HORC_1126")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `event_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | HORC_1126                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetEventContractsResponse](../../models/geteventcontractsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorEnvelope | 400, 404             | application/json     |
| errors.ErrorEnvelope | 500                  | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## search

Full-text search over one index of event contracts. Filters always apply to contracts, so with type=events or type=base-events an event or base event is found through its matching contracts: one with none (for example, only DELETED contracts under the default state) is not returned. The index trails the catalogue by seconds.

### Example Usage

<!-- UsageSnippet language="python" operationID="search" method="get" path="/v1/predictions/search" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev() as fd_client:

    res = fd_client.predictions.markets.search(type_=models.SearchType.CONTRACTS, q="unemployment june", state="ACTIVE", base_event_id="UNR", event_id="UNR_0822", category="Elections > United States House", page=1, per_page=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                               | Example                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                                                                                                                                                                                                    | [Optional[models.SearchType]](../../models/searchtype.md)                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                        | Level hits come back at. `contracts` (default) returns matching contracts; `events` returns one hit per event and `base-events` one per base event, each ranked by its best-matching contract and carrying only its own fields and a count of matching contracts. Echoed in the response. |                                                                                                                                                                                                                                                                                           |
| `q`                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                        | Full-text query over symbols, questions, event names and base-event specifications. Symbols split on _, - and . so `BPM 0822` finds `BPM_0822_1750`. Omit to browse, soonest last-trade date first.                                                                                       | unemployment june                                                                                                                                                                                                                                                                         |
| `state`                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                        | Contract state. Omitted means ACTIVE; `*` matches every state, including DELETED.                                                                                                                                                                                                         | ACTIVE                                                                                                                                                                                                                                                                                    |
| `base_event_id`                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                        | Only contracts under this base event.                                                                                                                                                                                                                                                     | UNR                                                                                                                                                                                                                                                                                       |
| `event_id`                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                        | Only contracts under this event.                                                                                                                                                                                                                                                          | UNR_0822                                                                                                                                                                                                                                                                                  |
| `category`                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                        | Only contracts in this category or any category under it. Takes a `path` from List Categories, URL-encoded. A bare level name such as `United States` matches nothing, because level names repeat under different parents.                                                                | Elections > United States House                                                                                                                                                                                                                                                           |
| `tradable`                                                                                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                        | Only tradable (true) or non-tradable (false) contracts.                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                           |
| `page`                                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                        | 1-based page number; 0 or omitted means 1.                                                                                                                                                                                                                                                | 1                                                                                                                                                                                                                                                                                         |
| `per_page`                                                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                        | Hits per page, counting whatever type returns; 0 or omitted means 20, values above 100 are clamped to 100.                                                                                                                                                                                | 20                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                           |

### Response

**[models.SearchResponse](../../models/searchresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorEnvelope | 400                  | application/json     |
| errors.ErrorEnvelope | 502                  | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |