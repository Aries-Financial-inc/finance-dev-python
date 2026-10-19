# TechnicalAnalysis

## Overview

### Available Operations

* [get_indicator](#get_indicator) - Get Technical Indicator Data
* [get_pattern](#get_pattern) - Get Technical Patterns
* [get_support_resistance](#get_support_resistance) - Get Support & Resistance Levels
* [get_technical_indicator](#get_technical_indicator) - Get Aggregate Technical Indicators

## get_indicator

Retrieve calculated technical indicator values including SMA, EMA, RSI, MACD, Bollinger Bands, and other charting indicators.

If `from` or `to` cannot be parsed as a signed 64-bit integer, returns 400 Bad Request with error code `INVALID_PARAMETER` and message `invalid from parameter` or `invalid to parameter`. Invalid indicator requests rejected by the data provider return 400 Bad Request with error code `BAD_REQUEST`; the message includes provider error details when suitable for public responses, otherwise `Invalid request parameters.`.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTechnicalIndicator" method="get" path="/v1/indicator" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.technical_analysis.get_indicator(symbol="<value>", resolution=models.GetTechnicalIndicatorResolution.THIRTY, indicator=models.TechnicalIndicatorType.RSI, from_=714124, to=669868)

    assert res.technical_indicator_response is not None

    # Handle response
    print(res.technical_indicator_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `symbol`                                                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                     | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`, `TSLA`.                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                        |
| `resolution`                                                                                                                                                                                                                                                                                           | [models.GetTechnicalIndicatorResolution](../../models/gettechnicalindicatorresolution.md)                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                     | How long each bar covers. Supported values are minutes (`1`, `5`, `15`, `30`, `60`) or daily/weekly/monthly (`D`, `W`, `M`). Other values return 400 Bad Request with error code `VALIDATION_ERROR`.                                                                                                   |                                                                                                                                                                                                                                                                                                        |
| `indicator`                                                                                                                                                                                                                                                                                            | [models.TechnicalIndicatorType](../../models/technicalindicatortype.md)                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                     | Which technical indicator to compute. Common picks: `sma` (simple moving average), `ema` (exponential moving average), `rsi` (relative strength index), `macd` (moving-average convergence-divergence), `bbands` (Bollinger Bands). See `TechnicalIndicatorType` for the full list of supported slugs. | rsi                                                                                                                                                                                                                                                                                                    |
| `from_`                                                                                                                                                                                                                                                                                                | *int*                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                     | Start timestamp (Unix seconds)                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                        |
| `to`                                                                                                                                                                                                                                                                                                   | *int*                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                     | End timestamp (Unix seconds)                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                        |
| `timeperiod`                                                                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | (Optional) Period for SMA/RSI/BBANDS                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                        |
| `fast_period`                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | MACD fast EMA length, in bars. The shorter of the two moving averages used to compute MACD. Standard value is 12. Only used when `indicator=macd`.                                                                                                                                                     |                                                                                                                                                                                                                                                                                                        |
| `slow_period`                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | MACD slow EMA length, in bars. The longer of the two moving averages used to compute MACD. Standard value is 26. Only used when `indicator=macd`.                                                                                                                                                      |                                                                                                                                                                                                                                                                                                        |
| `signal_period`                                                                                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | MACD signal EMA length, in bars. Used to smooth the MACD line into the signal line; crossovers between the two are the basic MACD trading cue. Standard value is 9. Only used when `indicator=macd`.                                                                                                   |                                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                        |

### Response

**[models.GetTechnicalIndicatorResponse](../../models/gettechnicalindicatorresponse.md)**

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

## get_pattern

Retrieve identified technical chart patterns including head and shoulders, double tops/bottoms, triangles, and other price formation signals.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTechnicalPatterns" method="get" path="/v1/scan/pattern" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.technical_analysis.get_pattern(symbol="AAPL", resolution=models.GetTechnicalPatternsResolution.M)

    assert res.technical_patterns_response is not None

    # Handle response
    print(res.technical_patterns_response)

```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          | Example                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                                                                             | *str*                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                   | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`, `TSLA`.                                                                  | AAPL                                                                                                                                                                                                 |
| `resolution`                                                                                                                                                                                         | [models.GetTechnicalPatternsResolution](../../models/gettechnicalpatternsresolution.md)                                                                                                              | :heavy_check_mark:                                                                                                                                                                                   | How long each bar covers. Supported values are minutes (`1`, `5`, `15`, `30`, `60`) or daily/weekly/monthly (`D`, `W`, `M`). Other values return 400 Bad Request with error code `VALIDATION_ERROR`. |                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                  |                                                                                                                                                                                                      |

### Response

**[models.GetTechnicalPatternsResponse](../../models/gettechnicalpatternsresponse.md)**

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

## get_support_resistance

Retrieve calculated support and resistance price levels based on historical price action for identifying key trading zones.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSupportResistanceLevels" method="get" path="/v1/scan/support-resistance" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.technical_analysis.get_support_resistance(symbol="AAPL", resolution=models.GetSupportResistanceLevelsResolution.FIFTEEN)

    assert res.support_resistance_levels_response is not None

    # Handle response
    print(res.support_resistance_levels_response)

```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          | Example                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                                                                             | *str*                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                   | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`, `TSLA`.                                                                  | AAPL                                                                                                                                                                                                 |
| `resolution`                                                                                                                                                                                         | [models.GetSupportResistanceLevelsResolution](../../models/getsupportresistancelevelsresolution.md)                                                                                                  | :heavy_check_mark:                                                                                                                                                                                   | How long each bar covers. Supported values are minutes (`1`, `5`, `15`, `30`, `60`) or daily/weekly/monthly (`D`, `W`, `M`). Other values return 400 Bad Request with error code `VALIDATION_ERROR`. |                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                  |                                                                                                                                                                                                      |

### Response

**[models.GetSupportResistanceLevelsResponse](../../models/getsupportresistancelevelsresponse.md)**

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

## get_technical_indicator

Retrieve aggregate technical indicator signals combining moving averages, oscillators, and momentum indicators for overall buy/sell recommendations.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAggregateTechnicalIndicators" method="get" path="/v1/scan/technical-indicator" example="default" -->
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.technical_analysis.get_technical_indicator(symbol="AAPL", resolution=models.GetAggregateTechnicalIndicatorsResolution.D)

    assert res.aggregate_technical_indicators_response is not None

    # Handle response
    print(res.aggregate_technical_indicators_response)

```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          | Example                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `symbol`                                                                                                                                                                                             | *str*                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                   | Stock ticker to query. Send the plain uppercase symbol exactly as you'd type it on a brokerage screen, e.g. `AAPL`, `MSFT`, `TSLA`.                                                                  | AAPL                                                                                                                                                                                                 |
| `resolution`                                                                                                                                                                                         | [models.GetAggregateTechnicalIndicatorsResolution](../../models/getaggregatetechnicalindicatorsresolution.md)                                                                                        | :heavy_check_mark:                                                                                                                                                                                   | How long each bar covers. Supported values are minutes (`1`, `5`, `15`, `30`, `60`) or daily/weekly/monthly (`D`, `W`, `M`). Other values return 400 Bad Request with error code `VALIDATION_ERROR`. |                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                  |                                                                                                                                                                                                      |

### Response

**[models.GetAggregateTechnicalIndicatorsResponse](../../models/getaggregatetechnicalindicatorsresponse.md)**

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