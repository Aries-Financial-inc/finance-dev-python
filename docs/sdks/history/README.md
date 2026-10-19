# Predictions.History

## Overview

### Available Operations

* [get_history](#get_history) - Get historical ticks for a single symbol
* [get_history_batch](#get_history_batch) - Batch historical ticks for up to 5 symbols

## get_history

Returns prediction-market YES/NO price history for a single symbol. Time range is optional; omit both `from` and `to` to use the service default. `from`/`to` accept RFC3339 strings (e.g. `2026-04-01T00:00:00Z`) or Unix seconds/milliseconds.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHistory" method="get" path="/v1/predictions/historical-data" -->
```python
from finance_dev import FinanceDev


with FinanceDev() as fd_client:

    res = fd_client.predictions.history.get_history(symbol="HORC_1126_Republican", from_="2026-04-01T00:00:00Z", to="2026-04-20T00:00:00Z", limit=500)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `symbol`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | HORC_1126_Republican                                                |
| `from_`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | RFC3339 timestamp or Unix seconds/milliseconds.                     | 2026-04-01T00:00:00Z                                                |
| `to`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | RFC3339 timestamp or Unix seconds/milliseconds.                     | 2026-04-20T00:00:00Z                                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | 0 or omitted means 10000; values above 10000 are clamped to it.     | 500                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetHistoryResponse](../../models/gethistoryresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorEnvelope | 400                  | application/json     |
| errors.ErrorEnvelope | 502                  | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## get_history_batch

Returns historical ticks for multiple symbols in one request. Each query may carry its own optional `from`/`to`/`limit`. Maximum 5 queries per call.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHistoryBatch" method="post" path="/v1/predictions/historical-data/batch" -->
```python
from finance_dev import FinanceDev
from finance_dev.utils import parse_datetime


with FinanceDev() as fd_client:

    res = fd_client.predictions.history.get_history_batch(queries=[
        {
            "from_": parse_datetime("2026-04-01T00:00:00Z"),
            "limit": 500,
            "symbol": "HORC_1126_Republican",
            "to": parse_datetime("2026-04-20T00:00:00Z"),
        },
    ])

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `queries`                                                                 | List[[models.PredMdHistoryRequest](../../models/predmdhistoryrequest.md)] | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.GetHistoryBatchResponse](../../models/gethistorybatchresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorEnvelope | 400                  | application/json     |
| errors.ErrorEnvelope | 502                  | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |