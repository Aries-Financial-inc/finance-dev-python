# Predictions.Markets

## Overview

### Available Operations

* [get_election_map](#get_election_map) - Get every race of an election cycle with its candidates' prices

## get_election_map

Every Senate, House and governor race of the cycle in all 50 states, with each candidate's latest price and 24-hour change, plus the House-control, Senate-majority and balance-of-power markets, in one response. Built for an election map: poll it with `If-None-Match`.

### Example Usage

<!-- UsageSnippet language="python" operationID="getElectionMap" method="get" path="/v1/predictions/elections/{cycle}/states" -->
```python
from finance_dev import FinanceDev


with FinanceDev() as fd_client:

    res = fd_client.predictions.markets.get_election_map(cycle=2026, state="TX", office="senate,house", race_type="general,special", include_resolved=True, include_non_front_runners=False)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              | Example                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `cycle`                                                                                                                                                                  | *int*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                       | Election year. `2026` is the only cycle served.                                                                                                                          | 2026                                                                                                                                                                     |
| `state`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | Two-letter code of one of the 50 states. Returns that state only.                                                                                                        | TX                                                                                                                                                                       |
| `office`                                                                                                                                                                 | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | Comma-separated: `senate`, `governor`, `house`. Default: all.                                                                                                            | senate,house                                                                                                                                                             |
| `race_type`                                                                                                                                                              | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | Comma-separated: `general`, `special`, `primary_d`, `primary_r`, `primary_open`, `runoff`. Default: all.                                                                 | general,special                                                                                                                                                          |
| `include_resolved`                                                                                                                                                       | *Optional[bool]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                       | `false` leaves out races the venue has settled.                                                                                                                          |                                                                                                                                                                          |
| `include_non_front_runners`                                                                                                                                              | *Optional[bool]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                       | `true` also returns candidates the venue marks as no longer in the race (`frontRunner: false`), such as primary losers. `leader` is computed from the outcomes returned. |                                                                                                                                                                          |
| `if_none_match`                                                                                                                                                          | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | The `ETag` of a previous response. Answers `304` while the map is unchanged.                                                                                             |                                                                                                                                                                          |
| `retries`                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                      |                                                                                                                                                                          |

### Response

**[models.GetElectionMapResponse](../../models/getelectionmapresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorEnvelope | 400, 404             | application/json     |
| errors.ErrorEnvelope | 500                  | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |