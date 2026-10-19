# StockAlternative

## Overview

### Available Operations

* [get_bank_branch](#get_bank_branch) - Get Bank Branch
* [get_congressional_trading](#get_congressional_trading) - Get Congressional Trading
* [get_covid19_us](#get_covid19_us) - Get COVID-19 US
* [get_earnings_call_live](#get_earnings_call_live) - Get Earnings Call Live
* [get_earnings_quality_score](#get_earnings_quality_score) - Get Earnings Quality Score
* [get_esg](#get_esg) - Get Company ESG
* [get_fda_advisory_committee_calendar](#get_fda_advisory_committee_calendar) - Get FDA Advisory Committee Calendar
* [get_historical_esg](#get_historical_esg) - Get Historical ESG
* [get_investment_theme](#get_investment_theme) - Get Investment Theme
* [get_presentation](#get_presentation) - Get Company Presentation
* [get_social_sentiment](#get_social_sentiment) - Get Social Sentiment
* [get_supply_chain](#get_supply_chain) - Get Supply Chain
* [get_transcripts_list](#get_transcripts_list) - Get Transcripts List
* [get_usa_spending](#get_usa_spending) - Get USA Spending
* [get_uspto_patent](#get_uspto_patent) - Get USPTO Patent
* [get_visa_application](#get_visa_application) - Get Visa Application (H1-B)

## get_bank_branch

Retrieve bank branch data for a symbol.

### Example Usage

<!-- UsageSnippet language="python" operationID="getBankBranches" method="get" path="/v1/stock/bank-branch" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_bank_branch(symbol="AAPL")

    assert res.bank_branches_response is not None

    # Handle response
    print(res.bank_branches_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetBankBranchesResponse](../../models/getbankbranchesresponse.md)**

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

## get_congressional_trading

Retrieve congressional trading data for a symbol within a date range.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCongressionalTrading" method="get" path="/v1/stock/congressional-trading" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_congressional_trading(symbol="AAPL", from_=date.fromisoformat("2024-01-01"), to=date.fromisoformat("2024-12-31"))

    assert res.congressional_trading_response is not None

    # Handle response
    print(res.congressional_trading_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `from_`                                                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_check_mark:                                                                                                          | Start of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-01-01`).                                              | 2024-01-01                                                                                                                  |
| `to`                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_check_mark:                                                                                                          | End of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-12-31`).                                                | 2024-12-31                                                                                                                  |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetCongressionalTradingResponse](../../models/getcongressionaltradingresponse.md)**

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

## get_covid19_us

Retrieve COVID-19 US data.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCovid19UsCases" method="get" path="/v1/stock/covid19/us" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_covid19_us()

    assert res.covid19_us_cases_response is not None

    # Handle response
    print(res.covid19_us_cases_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCovid19UsCasesResponse](../../models/getcovid19uscasesresponse.md)**

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

## get_earnings_call_live

Retrieve live or upcoming earnings call information.

### Example Usage

<!-- UsageSnippet language="python" operationID="getEarningsCallLive" method="get" path="/v1/stock/earnings-call-live" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_earnings_call_live(symbol="AAPL")

    assert res.earnings_call_live_response is not None

    # Handle response
    print(res.earnings_call_live_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `from_`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | Start of the date window, inclusive. Format: `YYYY-MM-DD`.                   |                                                                              |
| `to`                                                                         | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | End of the date window, inclusive. Format: `YYYY-MM-DD`.                     |                                                                              |
| `symbol`                                                                     | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Stock ticker to query. Send the plain uppercase symbol, e.g. `AAPL`.         | AAPL                                                                         |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[models.GetEarningsCallLiveResponse](../../models/getearningscallliveresponse.md)**

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

## get_earnings_quality_score

Retrieve earnings quality score metrics for a company (annual or quarterly).

### Example Usage

<!-- UsageSnippet language="python" operationID="getEarningsQualityScore" method="get" path="/v1/stock/earnings-quality-score" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_earnings_quality_score(symbol="AAPL", freq=models.ReportingFrequency.QUARTERLY)

    assert res.earnings_quality_score_response is not None

    # Handle response
    print(res.earnings_quality_score_response)

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 | Example                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                                                    | *str*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`.                                                 | AAPL                                                                                                                                                                        |
| `freq`                                                                                                                                                                      | [models.ReportingFrequency](../../models/reportingfrequency.md)                                                                                                             | :heavy_check_mark:                                                                                                                                                          | How often the score is computed. Allowed values:<br/>- `annual` — one score per fiscal year (broad trends).<br/>- `quarterly` — one score per quarter (closer to recent reporting). | quarterly                                                                                                                                                                   |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |                                                                                                                                                                             |

### Response

**[models.GetEarningsQualityScoreResponse](../../models/getearningsqualityscoreresponse.md)**

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

## get_esg

Retrieve environmental, social, and governance (ESG) data for a company.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCompanyEsg" method="get" path="/v1/stock/esg" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_esg(symbol="AAPL")

    assert res.company_esg_response is not None

    # Handle response
    print(res.company_esg_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetCompanyEsgResponse](../../models/getcompanyesgresponse.md)**

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

## get_fda_advisory_committee_calendar

Retrieve FDA advisory committee meeting calendar.

### Example Usage

<!-- UsageSnippet language="python" operationID="getFdaAdvisoryCommitteeCalendar" method="get" path="/v1/stock/fda-advisory-committee-calendar" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_fda_advisory_committee_calendar()

    assert res.fda_advisory_committee_calendar_response is not None

    # Handle response
    print(res.fda_advisory_committee_calendar_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetFdaAdvisoryCommitteeCalendarResponse](../../models/getfdaadvisorycommitteecalendarresponse.md)**

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

## get_historical_esg

Retrieve historical environmental, social, and governance (ESG) data for a company over time.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHistoricalEsg" method="get" path="/v1/stock/historical-esg" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_historical_esg(symbol="AAPL")

    assert res.historical_esg_response is not None

    # Handle response
    print(res.historical_esg_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetHistoricalEsgResponse](../../models/gethistoricalesgresponse.md)**

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

## get_investment_theme

Retrieve investment theme data by theme name.

### Example Usage

<!-- UsageSnippet language="python" operationID="getInvestmentTheme" method="get" path="/v1/stock/investment-theme" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_investment_theme(theme=models.InvestmentThemeID.AI)

    assert res.investment_theme_response is not None

    # Handle response
    print(res.investment_theme_response)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              | Example                                                                                                  |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `theme`                                                                                                  | [models.InvestmentThemeID](../../models/investmentthemeid.md)                                            | :heavy_check_mark:                                                                                       | investment theme identifier. Use the Try it dropdown or the supported values list on the reference page. | ai                                                                                                       |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |                                                                                                          |

### Response

**[models.GetInvestmentThemeResponse](../../models/getinvestmentthemeresponse.md)**

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

## get_presentation

Retrieve company presentation materials for a symbol.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCompanyPresentation" method="get" path="/v1/stock/presentation" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_presentation(symbol="AAPL")

    assert res.company_presentation_response is not None

    # Handle response
    print(res.company_presentation_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetCompanyPresentationResponse](../../models/getcompanypresentationresponse.md)**

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

## get_social_sentiment

Retrieve social media sentiment metrics for a symbol.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSocialSentiment" method="get" path="/v1/stock/social-sentiment" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_social_sentiment(symbol="AAPL")

    assert res.social_sentiment_response is not None

    # Handle response
    print(res.social_sentiment_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `from_`                                                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_minus_sign:                                                                                                          | Start of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-01-01`).                                              |                                                                                                                             |
| `to`                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_minus_sign:                                                                                                          | End of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-12-31`).                                                |                                                                                                                             |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetSocialSentimentResponse](../../models/getsocialsentimentresponse.md)**

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

## get_supply_chain

Retrieve supply chain data for a symbol.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSupplyChain" method="get" path="/v1/stock/supply-chain" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_supply_chain(symbol="AAPL")

    assert res.supply_chain_response is not None

    # Handle response
    print(res.supply_chain_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetSupplyChainResponse](../../models/getsupplychainresponse.md)**

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

## get_transcripts_list

Retrieve a list of available earnings call transcripts for a symbol.

### Example Usage

<!-- UsageSnippet language="python" operationID="listTranscripts" method="get" path="/v1/stock/transcripts/list" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_transcripts_list(symbol="AAPL")

    assert res.transcripts_response is not None

    # Handle response
    print(res.transcripts_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.ListTranscriptsResponse](../../models/listtranscriptsresponse.md)**

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

## get_usa_spending

Retrieve USA spending data for a symbol within a date range.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUsaSpending" method="get" path="/v1/stock/usa-spending" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_usa_spending(symbol="AAPL", from_=date.fromisoformat("2024-01-01"), to=date.fromisoformat("2024-12-31"))

    assert res.usa_spending_response is not None

    # Handle response
    print(res.usa_spending_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `from_`                                                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_check_mark:                                                                                                          | Start of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-01-01`).                                              | 2024-01-01                                                                                                                  |
| `to`                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_check_mark:                                                                                                          | End of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-12-31`).                                                | 2024-12-31                                                                                                                  |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetUsaSpendingResponse](../../models/getusaspendingresponse.md)**

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

## get_uspto_patent

Retrieve USPTO patent data for a symbol within a date range.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUsptoPatents" method="get" path="/v1/stock/uspto-patent" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_uspto_patent(symbol="AAPL", from_=date.fromisoformat("2024-01-01"), to=date.fromisoformat("2024-12-31"))

    assert res.uspto_patents_response is not None

    # Handle response
    print(res.uspto_patents_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `from_`                                                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_check_mark:                                                                                                          | Start of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-01-01`).                                              | 2024-01-01                                                                                                                  |
| `to`                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_check_mark:                                                                                                          | End of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-12-31`).                                                | 2024-12-31                                                                                                                  |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetUsptoPatentsResponse](../../models/getusptopatentsresponse.md)**

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

## get_visa_application

Retrieve H1-B visa application data for a symbol within a date range.

### Example Usage

<!-- UsageSnippet language="python" operationID="getVisaApplications" method="get" path="/v1/stock/visa-application" -->
```python
from datetime import date
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.stock_alternative.get_visa_application(symbol="AAPL", from_=date.fromisoformat("2024-01-01"), to=date.fromisoformat("2024-12-31"))

    assert res.visa_applications_response is not None

    # Handle response
    print(res.visa_applications_response)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                    | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`. | AAPL                                                                                                                        |
| `from_`                                                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_check_mark:                                                                                                          | Start of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-01-01`).                                              | 2024-01-01                                                                                                                  |
| `to`                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                | :heavy_check_mark:                                                                                                          | End of the date window, inclusive. Format: `YYYY-MM-DD` (e.g. `2024-12-31`).                                                | 2024-12-31                                                                                                                  |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[models.GetVisaApplicationsResponse](../../models/getvisaapplicationsresponse.md)**

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