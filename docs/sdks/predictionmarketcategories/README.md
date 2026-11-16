# PredictionMarketCategories

## Overview

### Available Operations

* [list](#list) - List prediction market categories

## list

The category tree of every category with at least one ACTIVE contract, so each one finds something when passed to search as category. Each level is ordered by name. Read from the search index, which trails the catalogue by seconds.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCategories" method="get" path="/v1/predictions/categories" -->
```python
from finance_dev import FinanceDev


with FinanceDev() as fd_client:

    res = fd_client.prediction_market_categories.list()

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