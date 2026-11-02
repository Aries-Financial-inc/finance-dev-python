# PredictionMarkets

## Overview

### Available Operations

* [get_base_event](#get_base_event) - Get a base event with its events and each event's contracts
* [list_categories](#list_categories) - List prediction market categories
* [get_event_contracts](#get_event_contracts) - Get an event and all contracts under it

## get_base_event

Get a base event with its events and each event's contracts

### Example Usage

<!-- UsageSnippet language="python" operationID="getBaseEvent" method="get" path="/v1/predictions/base-events/{baseEventId}" -->
```python
from finance_dev import FinanceDev


with FinanceDev() as fd_client:

    res = fd_client.prediction_markets.get_base_event(base_event_id="UNR")

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

    res = fd_client.prediction_markets.list_categories()

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

    res = fd_client.prediction_markets.get_event_contracts(event_id="HORC_1126")

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