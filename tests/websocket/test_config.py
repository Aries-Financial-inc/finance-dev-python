# Hand-maintained WebSocket tests; preserved by Speakeasy persistent edits.
import pytest
from finance_dev.websocket.config import WebSocketConfig
from finance_dev.websocket.errors import WebSocketConfigurationError

def test_configuration_validates_bounds():
    with pytest.raises(WebSocketConfigurationError): WebSocketConfig(auth_timeout=0)
    with pytest.raises(WebSocketConfigurationError): WebSocketConfig(reconnect_jitter=2)
