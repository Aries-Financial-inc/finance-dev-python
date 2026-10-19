# Hand-maintained WebSocket tests; preserved by Speakeasy persistent edits.
from finance_dev import FinanceDev, models
from finance_dev.websocket.config import ACCOUNT_URL, CHART_URL, MARKET_URL
from finance_dev.websocket.errors import WebSocketAuthenticationError

def test_websocket_is_lazy_root_namespace_and_uses_sdk_security():
    sdk = FinanceDev(security=models.Security(client_id="client", client_secret="secret"))
    assert sdk.websocket.market.endpoint == MARKET_URL
    assert sdk.websocket.chart.endpoint == CHART_URL
    assert sdk.websocket.account.endpoint == ACCOUNT_URL
    provider = sdk.websocket.market._provider(None, None)
    assert provider.client_id == "client"
    assert provider.token_url == "https://api.aries.com/v1/oauth2/token"

def test_token_and_provider_are_mutually_exclusive():
    sdk = FinanceDev()
    with __import__("pytest").raises(WebSocketAuthenticationError):
        sdk.websocket.market.connect(access_token="one", token_provider=object())
