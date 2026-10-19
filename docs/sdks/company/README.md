# Company

## Overview

### Available Operations

* [get_executive](#get_executive) - Get Company Executives
* [get_financial_metrics](#get_financial_metrics) - Get Company Financial Metrics
* [get_peers](#get_peers) - Get Company Peers
* [get_profile](#get_profile) - Get Company Profile

## get_executive

Retrieve information about company executives and key management personnel including names, titles, compensation, and tenure.

Returns 404 Not Found with error code `NOT_FOUND` when no executive data is available for the specified symbol.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCompanyExecutives" method="get" path="/v1/company/executive" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.company.get_executive(symbol="AAPL")

    assert res.company_executive_response is not None

    # Handle response
    print(res.company_executive_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `symbol`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Stock ticker symbol to research, such as AAPL.                      | AAPL                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetCompanyExecutivesResponse](../../models/getcompanyexecutivesresponse.md)**

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

## get_financial_metrics

Retrieve key financial metrics and ratios including market capitalization, P/E ratio, dividend yield, profit margins, and return on equity.

Returns 404 Not Found with error code `NOT_FOUND` when no metrics are available for the specified criteria.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCompanyMetrics" method="get" path="/v1/company/metrics" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.company.get_financial_metrics(symbol="AAPL", metric=models.GetCompanyMetricsMetric.ALL)

    assert res.basic_financials is not None

    # Handle response
    print(res.basic_financials)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         | Example                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                            | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | Stock ticker symbol to research, such as AAPL.                                                                      | AAPL                                                                                                                |
| `metric`                                                                                                            | [models.GetCompanyMetricsMetric](../../models/getcompanymetricsmetric.md)                                           | :heavy_check_mark:                                                                                                  | Which metric group to return. Currently only `all` is supported — it returns every available metric for the symbol. | all                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |                                                                                                                     |

### Response

**[models.GetCompanyMetricsResponse](../../models/getcompanymetricsresponse.md)**

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

## get_peers

Retrieve a list of peer companies within the same industry or sector that are comparable in size and business model.

Returns 404 Not Found with error code `NOT_FOUND` when no peers are available for the specified symbol.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCompanyPeers" method="get" path="/v1/company/peers" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.company.get_peers(symbol="AAPL")

    assert res.company_peers_response is not None

    # Handle response
    print(res.company_peers_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `symbol`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Stock ticker symbol to research, such as AAPL.                      | AAPL                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetCompanyPeersResponse](../../models/getcompanypeersresponse.md)**

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

## get_profile

Retrieve comprehensive company information including business description, industry classification, headquarters location, and key identifiers. At least one of symbol, ISIN, or CUSIP must be provided. If all three are omitted, the API returns 400 Bad Request. Response includes masked logo URL for privacy.

At least one of symbol, isin, or cusip is required. Multiple identifiers are accepted.

Returns 404 Not Found with error code `NOT_FOUND` when no company profile matches the supplied identifiers.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCompanyProfile" method="get" path="/v1/company/profile" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.company.get_profile(symbol="AAPL", isin="US0378331005", cusip="037833100")

    assert res.company_profile is not None

    # Handle response
    print(res.company_profile)

```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          | Example                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `symbol`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Stock ticker symbol, such as AAPL. Optional if ISIN or CUSIP is provided. If symbol, isin, and cusip are all omitted, the API returns 400 Bad Request.                               | AAPL                                                                                                                                                                                 |
| `isin`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | International Securities Identification Number. Optional if symbol or CUSIP is provided. If symbol, isin, and cusip are all omitted, the API returns 400 Bad Request.                | US0378331005                                                                                                                                                                         |
| `cusip`                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Committee on Uniform Securities Identification Procedures code. Optional if symbol or ISIN is provided. If symbol, isin, and cusip are all omitted, the API returns 400 Bad Request. | 037833100                                                                                                                                                                            |
| `retries`                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                  |                                                                                                                                                                                      |

### Response

**[models.GetCompanyProfileResponse](../../models/getcompanyprofileresponse.md)**

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