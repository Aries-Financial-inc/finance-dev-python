# finance-dev

Developer-friendly & type-safe Python SDK specifically catered to leverage *finance-dev* API.

<!-- <div align="left">
    <a href="https://www.speakeasy.com/?utm_source=finance-dev&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div> -->


<br /><br />
<!-- > [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/aries/aries). Delete this section before > publishing to a package manager. -->

<!-- Start Summary [summary] -->
## Summary

Aries API — OpenAPI Specification: OpenAPI Specification for the Aries trading platform API.

# Authentication

Learn how to authenticate with the Aries API using OAuth2 and manage access tokens in your SDK.

## Overview

The Aries API uses **OAuth2 with Bearer tokens** (JWT format) for authentication. All API requests require a valid access token in the `Authorization` header:

```
Authorization: Bearer <access_token>
```

## Providing Client ID and Client Secret (SDK)

When using the generated SDK, provide your **Client ID** and **Client Secret** when you create the API client (e.g. in the constructor or security options). The SDK will use these to obtain and refresh the access token internally; you do not need to manage tokens yourself.

Obtain your OAuth2 credentials from the Aries platform (e.g. Client Center / Manage Account at https://app.aries.com):

- **Client ID** – Your application identifier (pass to SDK client)
- **Client Secret** – Your application secret key (pass to SDK client; use PKCE for public clients where secret cannot be stored)

## Authentication Flow

### 1. Authorization Code Flow

For server-side or confidential clients:

1. **Redirect the user** to the authorization URL to sign in and consent:
 - **URL:** `https://app.aries.com/oauth2/authorize`
 - **Query params:** `response_type=code`, `client_id`, `redirect_uri`, `scope`, `state`

2. **Exchange the code for tokens** (after user is redirected back with `?code=.`):
 - **POST** `https://api.aries.com/v1/oauth2/token`
 - **Body:** `grant_type=authorization_code`, `code`, `redirect_uri`, `client_id`, `client_secret`
 - Response includes `access_token` and `refresh_token`

3. **Call the API** with the access token: `Authorization: Bearer <access_token>`

### 2. PKCE Flow

For SPAs and mobile apps (public clients that cannot store `client_secret`):

1. Generate a **code_verifier** (random string) and **code_challenge** = BASE64URL(SHA256(code_verifier)).
2. **Redirect the user** to `https://app.aries.com/oauth2/authorize` with `code_challenge`, `code_challenge_method=S256`, plus `client_id`, `redirect_uri`, `scope`, `state`.
3. **Exchange the code** at POST `https://api.aries.com/v1/oauth2/token` with `grant_type=authorization_code`, `code`, `redirect_uri`, `client_id`, `code_verifier` (no client_secret).
4. Use the returned `access_token` as Bearer.

### 3. MFA Verification

If the user has MFA enabled, the authorize step may return `is_mfa: true` and a `next_step_auth_id`. Call **POST** `https://api.aries.com/v1/oauth2/authorize/mfa` with `next_step_auth_id` and `verification_code` (6-digit code). Then continue with **POST** `/v1/oauth2/authorize/confirm` to get the authorization code, and exchange it at `/v1/oauth2/token`.

## Token Management

- **Refresh when expired:** POST `https://api.aries.com/v1/oauth2/token` with `grant_type=refresh_token`, `client_id`, `client_secret`, `refresh_token`.
- **Using a Bearer token directly:** If you already have an access token, set the header `Authorization: Bearer <access_token>` on every request. The SDK can accept a pre-obtained token and use it until it expires.

## OAuth2 Scopes

Request only the scopes your application needs. Available scopes:

| Scope | Description |
|-------|-------------|
| `user:information` | View user profile and personal details |
| `watchlist:information` | View your watchlists and their symbols |
| `watchlist:management` | Create, update, replace, and delete your watchlists |
| `account:information` | View account balances, positions, and transaction history |
| `order:execution` | Place, modify, and cancel orders |
| `order:information` | View order history and status |
| `position:information` | View current positions and holdings |
| `market:information` | Access live and historical market data |
| `calendar:information` | Access earnings, economic, and market schedule data |
| `options:information` | Access options chains and expiration data |
| `analytics:information` | View analytics, ratings, and market insights |
| `market:supplemental` | News, company profiles, financials, filings, ETF data, technical analysis |

Specify multiple scopes as a space-separated string, e.g. `account:information order:execution market:information`.

## Security Best Practices

- **Store credentials securely** – Use environment variables or a secrets manager for `client_id` and `client_secret`. Never hardcode them.
- **Handle token expiration** – Check for 401 responses and refresh the token using the refresh_token, then retry the request.
- **Use HTTPS** – All authorization and token endpoints must be called over HTTPS.
- **Validate state** – When using the authorization code flow, validate the `state` parameter on the callback to prevent CSRF.

## Error Handling

- **400 Bad Request** – Invalid or missing parameters, validation failures, or malformed JSON. Response bodies follow the same patterns as other errors (flat `error` string, optional `codes`, nested `error` object, or rarely no body).

- **401 Unauthorized** – Invalid or expired access token; refresh the token or re-authenticate. JSON bodies are not identical on every route: you may see a flat `error` string (sometimes with `codes`), a nested `error` object (`type`, `code`, `message`), or rarely an empty body

- **403 Forbidden** – Insufficient scope or permissions for the requested resource. Error JSON may be flat or nested, like 400/401.

- **404 Not Found** – Resource does not exist or is not visible. Error JSON may be flat or nested.

- **500 / 5xx** – Server or upstream failure; retry with backoff. Do not depend on a single error JSON shape; some responses may have no body.


---

Endpoints in this spec: health, OAuth2 (authorize, confirm, mfa, token), users, accounts, orders, market data, watchlist, chart, analytics, calendars, company, economy, financials, indices, options, news, and supplemental data.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [finance-dev](#finance-dev)
* [Authentication](#authentication)
  * [Overview](#overview)
  * [Providing Client ID and Client Secret (SDK)](#providing-client-id-and-client-secret-sdk)
  * [Authentication Flow](#authentication-flow)
  * [Token Management](#token-management)
  * [OAuth2 Scopes](#oauth2-scopes)
  * [Security Best Practices](#security-best-practices)
  * [Error Handling](#error-handling)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication-1)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Pagination](#pagination)
  * [Retries](#retries)
  * [Error Handling](#error-handling-1)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [WebSocket streaming](#websocket-streaming)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add finance_dev
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install finance_dev
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add finance_dev
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from finance_dev python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "finance_dev",
# ]
# ///

from finance_dev import FinanceDev

sdk = FinanceDev(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.get_account_positions(id="TEST-ACCOUNT-001")

    assert res.get_positions_response is not None

    # Handle response
    print(res.get_positions_response)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from finance_dev import FinanceDev, models

async def main():

    async with FinanceDev(
        security=models.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as fd_client:

        res = await fd_client.accounts.get_account_positions_async(id="TEST-ACCOUNT-001")

        assert res.get_positions_response is not None

        # Handle response
        print(res.get_positions_response)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                                            | Type   | Scheme                         |
| ----------------------------------------------- | ------ | ------------------------------ |
| `client_id`<br/>`client_secret`<br/>`token_url` | oauth2 | OAuth2 Client Credentials Flow |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.get_account_positions(id="TEST-ACCOUNT-001")

    assert res.get_positions_response is not None

    # Handle response
    print(res.get_positions_response)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Accounts](docs/sdks/accounts/README.md)

* [get_account_positions](docs/sdks/accounts/README.md#get_account_positions) - Get Account Positions
* [get_account_balance](docs/sdks/accounts/README.md#get_account_balance) - Get Account Balance
* [get_user_accounts](docs/sdks/accounts/README.md#get_user_accounts) - Get User Accounts

### [Analytics](docs/sdks/analytics/README.md)

* [get_insights](docs/sdks/analytics/README.md#get_insights) - Get Analyst Insights
* [get_market_breadth](docs/sdks/analytics/README.md#get_market_breadth) - Get Market Breadth
* [get_net_inflow](docs/sdks/analytics/README.md#get_net_inflow) - Get Net Inflow
* [get](docs/sdks/analytics/README.md#get) - Get Analyst Ratings
* [get_sector_tickers](docs/sdks/analytics/README.md#get_sector_tickers) - Get Sector Tickers
* [get_sector_wise_change](docs/sdks/analytics/README.md#get_sector_wise_change) - Get Sector-wise Change
* [get_top_gainers](docs/sdks/analytics/README.md#get_top_gainers) - Get Top Gaining Stocks
* [get_top_losers](docs/sdks/analytics/README.md#get_top_losers) - Get Top Losing Stocks
* [get_top_most_active](docs/sdks/analytics/README.md#get_top_most_active) - Get Most Active Stocks
* [get_options_et_fs_top_volume](docs/sdks/analytics/README.md#get_options_et_fs_top_volume) - Get Top ETF Options by Volume
* [get_options_stocks_top_gainers](docs/sdks/analytics/README.md#get_options_stocks_top_gainers) - Get Top Stock Options by Gains
* [get_options_stocks_top_volume](docs/sdks/analytics/README.md#get_options_stocks_top_volume) - Get Top Stock Options by Volume
* [stock_screener](docs/sdks/analytics/README.md#stock_screener) - Stock Screener

### [Calendar](docs/sdks/calendar/README.md)

* [get_conference_calls](docs/sdks/calendar/README.md#get_conference_calls) - Get Conference Calls
* [get_earnings_calendar](docs/sdks/calendar/README.md#get_earnings_calendar) - Get Earnings Calendar
* [get_economics_calendar](docs/sdks/calendar/README.md#get_economics_calendar) - Get Economics Calendar
* [get_historical_data](docs/sdks/calendar/README.md#get_historical_data) - Get Historical Economic Data
* [get_mergers_and_acquisitions](docs/sdks/calendar/README.md#get_mergers_and_acquisitions) - Get Mergers & Acquisitions

### [Chart](docs/sdks/chart/README.md)

* [get_chart_config](docs/sdks/chart/README.md#get_chart_config) - Get Chart Configuration
* [get_chart_history](docs/sdks/chart/README.md#get_chart_history) - Get Historical Chart Data
* [get_quotes](docs/sdks/chart/README.md#get_quotes) - Get Real-Time Quotes
* [search_symbols](docs/sdks/chart/README.md#search_symbols) - Search Symbols
* [get_symbol_info](docs/sdks/chart/README.md#get_symbol_info) - Get Symbol Information
* [get_tick_history](docs/sdks/chart/README.md#get_tick_history) - Get Tick-Based Chart Data
* [get_chart_time](docs/sdks/chart/README.md#get_chart_time) - Get Server Time

### [Company](docs/sdks/company/README.md)

* [get_executive](docs/sdks/company/README.md#get_executive) - Get Company Executives
* [get_financial_metrics](docs/sdks/company/README.md#get_financial_metrics) - Get Company Financial Metrics
* [get_peers](docs/sdks/company/README.md#get_peers) - Get Company Peers
* [get_profile](docs/sdks/company/README.md#get_profile) - Get Company Profile

### [CorporateActions](docs/sdks/corporateactions/README.md)

* [get_dividends](docs/sdks/corporateactions/README.md#get_dividends) - Get Dividend History
* [get_ipo_calendar](docs/sdks/corporateactions/README.md#get_ipo_calendar) - Get IPO Calendar
* [get_spinoffs](docs/sdks/corporateactions/README.md#get_spinoffs) - Get Corporate Spinoffs
* [get_tender_offers](docs/sdks/corporateactions/README.md#get_tender_offers) - Get Tender Offers
* [get_stock_split](docs/sdks/corporateactions/README.md#get_stock_split) - Get Stock Split History

### [Economy](docs/sdks/economy/README.md)

* [get_inflation](docs/sdks/economy/README.md#get_inflation) - Get Latest Inflation Data
* [get_inflation_expectations](docs/sdks/economy/README.md#get_inflation_expectations) - Get Latest Inflation Expectations
* [get_treasury_yields](docs/sdks/economy/README.md#get_treasury_yields) - Get Latest Treasury Yields

### [Etf](docs/sdks/etf/README.md)

* [get_holdings](docs/sdks/etf/README.md#get_holdings) - Get ETF Holdings
* [get_profile](docs/sdks/etf/README.md#get_profile) - Get ETF Profile
* [get_sector](docs/sdks/etf/README.md#get_sector) - Get ETF Sector Allocation

### [Etfs](docs/sdks/etfs/README.md)

* [get_country_allocation](docs/sdks/etfs/README.md#get_country_allocation) - Get ETF Country Allocation

### [Filings](docs/sdks/filings/README.md)

* [get_sec](docs/sdks/filings/README.md#get_sec) - Get SEC Filings
* [get_similarity_index](docs/sdks/filings/README.md#get_similarity_index) - Get Filings Similarity Index

### [Financials](docs/sdks/financials/README.md)

* [get_cash_flow_statements](docs/sdks/financials/README.md#get_cash_flow_statements) - Get Cash Flow Statements
* [get_income_statements](docs/sdks/financials/README.md#get_income_statements) - Get Income Statements
* [get_ratios](docs/sdks/financials/README.md#get_ratios) - Get Financial Ratios
* [get_reported](docs/sdks/financials/README.md#get_reported) - Get Reported Financials
* [get_revenue_breakdown](docs/sdks/financials/README.md#get_revenue_breakdown) - Get Revenue Breakdown
* [get_short_interest](docs/sdks/financials/README.md#get_short_interest) - Get Short Interest Data
* [get_short_volume](docs/sdks/financials/README.md#get_short_volume) - Get Short Volume Data
* [get_statements](docs/sdks/financials/README.md#get_statements) - Get Financial Statements

### [Indices](docs/sdks/indices/README.md)

* [get_bar](docs/sdks/indices/README.md#get_bar) - Get Index Bar Data
* [get_bars](docs/sdks/indices/README.md#get_bars) - Get Index Bars Data
* [get_by_group](docs/sdks/indices/README.md#get_by_group) - Get Indices By Group
* [get_chart_bars](docs/sdks/indices/README.md#get_chart_bars) - Get Index Chart Data
* [get_groups](docs/sdks/indices/README.md#get_groups) - Get Index Groups
* [list](docs/sdks/indices/README.md#list) - Get Index List
* [get_realtime_values](docs/sdks/indices/README.md#get_realtime_values) - Get Realtime Indices Values
* [search](docs/sdks/indices/README.md#search) - Search Indices

### [Logos](docs/sdks/logos/README.md)

* [search](docs/sdks/logos/README.md#search) - Search Company Logos
* [sync](docs/sdks/logos/README.md#sync) - Sync Company Logos

### [Market](docs/sdks/market/README.md)

* [get_etb_list](docs/sdks/market/README.md#get_etb_list) - Get Easy-to-Borrow List
* [search_etb_symbols](docs/sdks/market/README.md#search_etb_symbols) - Search Easy-to-Borrow Symbols
* [get_holidays](docs/sdks/market/README.md#get_holidays) - Get Market Holidays
* [get_status](docs/sdks/market/README.md#get_status) - Get Market Status
* [get_equity_details](docs/sdks/market/README.md#get_equity_details) - Get equity details
* [get_option_details](docs/sdks/market/README.md#get_option_details) - Get option details

### [MarketData](docs/sdks/marketdata/README.md)

* [search_symbols](docs/sdks/marketdata/README.md#search_symbols) - Search Symbols

### [News](docs/sdks/newssdk/README.md)

* [get_news](docs/sdks/newssdk/README.md#get_news) - Get Market News
* [get_sentiment](docs/sdks/newssdk/README.md#get_sentiment) - Get News Sentiment
* [get_by_id](docs/sdks/newssdk/README.md#get_by_id) - Get News by ID

### [Options](docs/sdks/options/README.md)

* [get_activity](docs/sdks/options/README.md#get_activity) - Get Options Activity
* [get_last_trade](docs/sdks/options/README.md#get_last_trade) - Get Options Last Trade
* [get_open_close_data](docs/sdks/options/README.md#get_open_close_data) - Get Option Open/Close Data
* [get_previous_day](docs/sdks/options/README.md#get_previous_day) - Get Previous Day Option Data
* [get_quotes](docs/sdks/options/README.md#get_quotes) - Get Options Quotes
* [get_option_chain_snapshot](docs/sdks/options/README.md#get_option_chain_snapshot) - Get option chain snapshot
* [get_option_contract_snapshot](docs/sdks/options/README.md#get_option_contract_snapshot) - Get option contract snapshot
* [get_trades](docs/sdks/options/README.md#get_trades) - Get Options Trades
* [get_unusual_activity](docs/sdks/options/README.md#get_unusual_activity) - Get Options Unusual Activity by Symbol
* [get_contracts](docs/sdks/options/README.md#get_contracts) - Get Options Contract Symbols
* [get_expiry_dates](docs/sdks/options/README.md#get_expiry_dates) - Get Options Expiry Dates

### [Orders](docs/sdks/orders/README.md)

* [place_order](docs/sdks/orders/README.md#place_order) - Place an order
* [cancel](docs/sdks/orders/README.md#cancel) - Cancel an order
* [preview_order](docs/sdks/orders/README.md#preview_order) - Preview order
* [replace](docs/sdks/orders/README.md#replace) - Replace an order
* [list_active_orders](docs/sdks/orders/README.md#list_active_orders) - List active orders (v2)
* [list_order_history](docs/sdks/orders/README.md#list_order_history) - List order history (v2)

### [Ownership](docs/sdks/ownership/README.md)

* [get_institutional](docs/sdks/ownership/README.md#get_institutional) - Get Institutional Ownership
* [get_portfolio](docs/sdks/ownership/README.md#get_portfolio) - Get Institutional Portfolio
* [get_data](docs/sdks/ownership/README.md#get_data) - Get Company Ownership Data
* [get_fund_data](docs/sdks/ownership/README.md#get_fund_data) - Get Fund Ownership Data
* [get_insider_transactions](docs/sdks/ownership/README.md#get_insider_transactions) - Get Insider Transactions

### [Predictions.History](docs/sdks/history/README.md)

* [get_history](docs/sdks/history/README.md#get_history) - Get historical ticks for a single symbol
* [get_history_batch](docs/sdks/history/README.md#get_history_batch) - Batch historical ticks for up to 5 symbols

### [Predictions.Markets](docs/sdks/markets/README.md)

* [get_base_event](docs/sdks/markets/README.md#get_base_event) - Get a base event with its events and each event's contracts
* [list_categories](docs/sdks/markets/README.md#list_categories) - List prediction market categories
* [get_event_contracts](docs/sdks/markets/README.md#get_event_contracts) - Get an event and all contracts under it
* [search](docs/sdks/markets/README.md#search) - Search contracts, events or base events

### [Predictions.Orders](docs/sdks/predictionsorders/README.md)

* [list_prediction_orders](docs/sdks/predictionsorders/README.md#list_prediction_orders) - List prediction orders
* [place_prediction_order](docs/sdks/predictionsorders/README.md#place_prediction_order) - Place prediction order
* [get_prediction_order](docs/sdks/predictionsorders/README.md#get_prediction_order) - Get prediction order

### [Signals](docs/sdks/signals/README.md)

* [get_bull_bear](docs/sdks/signals/README.md#get_bull_bear) - Get Bull & Bear Analysis

### [StockAlternative](docs/sdks/stockalternative/README.md)

* [get_bank_branch](docs/sdks/stockalternative/README.md#get_bank_branch) - Get Bank Branch
* [get_congressional_trading](docs/sdks/stockalternative/README.md#get_congressional_trading) - Get Congressional Trading
* [get_covid19_us](docs/sdks/stockalternative/README.md#get_covid19_us) - Get COVID-19 US
* [get_earnings_call_live](docs/sdks/stockalternative/README.md#get_earnings_call_live) - Get Earnings Call Live
* [get_earnings_quality_score](docs/sdks/stockalternative/README.md#get_earnings_quality_score) - Get Earnings Quality Score
* [get_esg](docs/sdks/stockalternative/README.md#get_esg) - Get Company ESG
* [get_fda_advisory_committee_calendar](docs/sdks/stockalternative/README.md#get_fda_advisory_committee_calendar) - Get FDA Advisory Committee Calendar
* [get_historical_esg](docs/sdks/stockalternative/README.md#get_historical_esg) - Get Historical ESG
* [get_investment_theme](docs/sdks/stockalternative/README.md#get_investment_theme) - Get Investment Theme
* [get_presentation](docs/sdks/stockalternative/README.md#get_presentation) - Get Company Presentation
* [get_social_sentiment](docs/sdks/stockalternative/README.md#get_social_sentiment) - Get Social Sentiment
* [get_supply_chain](docs/sdks/stockalternative/README.md#get_supply_chain) - Get Supply Chain
* [get_transcripts_list](docs/sdks/stockalternative/README.md#get_transcripts_list) - Get Transcripts List
* [get_usa_spending](docs/sdks/stockalternative/README.md#get_usa_spending) - Get USA Spending
* [get_uspto_patent](docs/sdks/stockalternative/README.md#get_uspto_patent) - Get USPTO Patent
* [get_visa_application](docs/sdks/stockalternative/README.md#get_visa_application) - Get Visa Application (H1-B)

### [StockAlternatives](docs/sdks/stockalternatives/README.md)

* [get_lobbying](docs/sdks/stockalternatives/README.md#get_lobbying) - Get Lobbying
* [get_transcripts](docs/sdks/stockalternatives/README.md#get_transcripts) - Get Transcript by ID

### [StockEstimates](docs/sdks/stockestimates/README.md)

* [get_earnings](docs/sdks/stockestimates/README.md#get_earnings) - Get Earnings Surprises
* [get_ebit_estimate](docs/sdks/stockestimates/README.md#get_ebit_estimate) - Get EBIT Estimates
* [get_ebitda_estimate](docs/sdks/stockestimates/README.md#get_ebitda_estimate) - Get EBITDA Estimates
* [get_eps_estimate](docs/sdks/stockestimates/README.md#get_eps_estimate) - Get EPS Estimates
* [get_price_target](docs/sdks/stockestimates/README.md#get_price_target) - Get Analyst Price Targets
* [get_revenue_estimate](docs/sdks/stockestimates/README.md#get_revenue_estimate) - Get Revenue Estimates
* [get_upgrade_downgrade](docs/sdks/stockestimates/README.md#get_upgrade_downgrade) - Get Analyst Upgrades & Downgrades

### [Stocks](docs/sdks/stocks/README.md)

* [get_aggregates](docs/sdks/stocks/README.md#get_aggregates) - Get Aggregate Bars
* [get_daily_summary](docs/sdks/stocks/README.md#get_daily_summary) - Get Daily Market Summary
* [get_last_quote](docs/sdks/stocks/README.md#get_last_quote) - Get Last Quote (NBBO)
* [get_last_trade](docs/sdks/stocks/README.md#get_last_trade) - Get Last Trade
* [get_open_close](docs/sdks/stocks/README.md#get_open_close) - Get Daily Ticker Summary
* [get_prev_day](docs/sdks/stocks/README.md#get_prev_day) - Get Previous Day Bar
* [get_quotes](docs/sdks/stocks/README.md#get_quotes) - Get Stock Quotes (NBBO)
* [get_snapshot](docs/sdks/stocks/README.md#get_snapshot) - Get Full Market Snapshot
* [get_trades](docs/sdks/stocks/README.md#get_trades) - Get Stock Trades
* [get_unified_snapshot](docs/sdks/stocks/README.md#get_unified_snapshot) - Get Unified Snapshot

### [TechnicalAnalysis](docs/sdks/technicalanalysissdk/README.md)

* [get_indicator](docs/sdks/technicalanalysissdk/README.md#get_indicator) - Get Technical Indicator Data
* [get_pattern](docs/sdks/technicalanalysissdk/README.md#get_pattern) - Get Technical Patterns
* [get_support_resistance](docs/sdks/technicalanalysissdk/README.md#get_support_resistance) - Get Support & Resistance Levels
* [get_technical_indicator](docs/sdks/technicalanalysissdk/README.md#get_technical_indicator) - Get Aggregate Technical Indicators

### [Watchlist](docs/sdks/watchlistsdk/README.md)

* [list](docs/sdks/watchlistsdk/README.md#list) - List Watchlists
* [create](docs/sdks/watchlistsdk/README.md#create) - Create Watchlist
* [replace_all](docs/sdks/watchlistsdk/README.md#replace_all) - Replace All Watchlists
* [delete](docs/sdks/watchlistsdk/README.md#delete) - Delete Watchlist
* [get](docs/sdks/watchlistsdk/README.md#get) - Get Watchlist
* [update](docs/sdks/watchlistsdk/README.md#update) - Update Watchlist

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.analytics.get_insights()

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from finance_dev import FinanceDev, models
from finance_dev.utils import BackoffStrategy, RetryConfig


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.get_account_positions(id="TEST-ACCOUNT-001",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.get_positions_response is not None

    # Handle response
    print(res.get_positions_response)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from finance_dev import FinanceDev, models
from finance_dev.utils import BackoffStrategy, RetryConfig


with FinanceDev(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.get_account_positions(id="TEST-ACCOUNT-001")

    assert res.get_positions_response is not None

    # Handle response
    print(res.get_positions_response)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`FinanceDevAPIError`](./src/finance_dev/errors/financedevapierror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from finance_dev import FinanceDev, errors, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:
    res = None
    try:

        res = fd_client.accounts.get_account_positions(id="TEST-ACCOUNT-001")

        assert res.get_positions_response is not None

        # Handle response
        print(res.get_positions_response)


    except errors.FinanceDevAPIError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.AuthenticationErrorEnvelope):
            print(e.data.error)  # Optional[models.AuthenticationErrorDetail]
            print(e.data.meta)  # Optional[Dict[str, Any]]
            print(e.data.http_meta)  # models.HTTPMetadata
```

### Error Classes
**Primary errors:**
* [`FinanceDevAPIError`](./src/finance_dev/errors/financedevapierror.py): The base class for HTTP error responses.
  * [`ErrorResponse`](./src/finance_dev/errors/errorresponse.py): Flat error body: an `error` string, with optional structured `codes` and additional `metadata`. *
  * [`AuthenticationErrorEnvelope`](./src/finance_dev/errors/authenticationerrorenvelope.py): JSON envelope where `error` is a nested object (`type`, `code`, `message`, …). Many services use this shape for 400, 401, 403, 404, and 5xx when using the shared HTTP error format. *

<details><summary>Less common errors (7)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`FinanceDevAPIError`](./src/finance_dev/errors/financedevapierror.py)**:
* [`ErrorEnvelope`](./src/finance_dev/errors/errorenvelope.py): Prediction-market error envelope. Returned by historical-data and prediction-market reference endpoints on 400/404/500/502. Applicable to 6 of 151 methods.*
* [`PredOrdersErrorEnvelope`](./src/finance_dev/errors/predorderserrorenvelope.py): Invalid request. `INVALID_ORDER` carries the reason in `message`; on placement this includes refusals from order entry and the venue (price, tick size, account setup). Applicable to 3 of 151 methods.*
* [`ResponseValidationError`](./src/finance_dev/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from finance_dev import FinanceDev, models


with FinanceDev(
    server_url="https://api.aries.com",
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.get_account_positions(id="TEST-ACCOUNT-001")

    assert res.get_positions_response is not None

    # Handle response
    print(res.get_positions_response)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from finance_dev import FinanceDev
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = FinanceDev(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from finance_dev import FinanceDev
from finance_dev.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = FinanceDev(async_client=CustomClient(httpx.AsyncClient()))
```
### httpx2 (Pydantic's httpx fork)

[httpx2](https://httpx2.pydantic.dev/) is Pydantic's maintained fork of `httpx`. To run this SDK on httpx2, call `alias_httpx()` at your program's entry point, before importing the SDK, so every `import httpx` — including the ones inside the SDK — resolves to `httpx2`:
```python
import httpx2

httpx2.alias_httpx()

from finance_dev import FinanceDev

s = FinanceDev()
```

An SDK can also be generated against httpx2 directly, so it depends on the fork instead of `httpx`, by setting `python.httpClientLibrary: httpx2` in `gen.yaml`.
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `FinanceDev` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from finance_dev import FinanceDev, models
def main():

    with FinanceDev(
        security=models.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as fd_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with FinanceDev(
        security=models.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as fd_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from finance_dev import FinanceDev
import logging

logging.basicConfig(level=logging.DEBUG)
s = FinanceDev(debug_logger=logging.getLogger("finance_dev"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# WebSocket streaming

`FinanceDev` exposes market, chart, and account WebSocket clients under
`sdk.websocket`. Connections authenticate on entry and support both sync and
async context managers. See the [WebSocket guide](docs/websocket/README.md)
for examples, token providers, event semantics, and reconnect behavior.

Market field selectors use `"*"` for all fields. To combine Time & Sales with
quotes and trades, set `time_and_sales=True`, `quote_fields="*"`, and
`trade_fields="*"`; Time & Sales alone selects only that stream.

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=finance-dev&utm_campaign=python)
