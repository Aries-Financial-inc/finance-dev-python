# Users

## Overview

Basic information about the authenticated user.

### Available Operations

* [get_user_info](#get_user_info) - Get User Info

## get_user_info

Return only the authenticated user's numeric ID and current email address from the user record. Accepts the same Bearer access tokens as GET /v1/users/me and does not load application or onboarding data. Responses are not cached.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUserInfo" method="get" path="/v1/users/info" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.users.get_user_info()

    assert res.user_info_response is not None

    # Handle response
    print(res.user_info_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserInfoResponse](../../models/getuserinforesponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ErrorResponse               | 403                                | application/json                   |
| errors.AuthenticationErrorEnvelope | 403                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |