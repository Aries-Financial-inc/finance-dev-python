"""WebSocket namespace attached to the generated Aries SDK."""

from .market import MarketWebSocket
from .chart import ChartWebSocket
from .account import AccountWebSocket


class WebSocketSDK:
    def __init__(self, sdk_configuration, parent_ref=None):
        self.market = MarketWebSocket(sdk_configuration)
        self.chart = ChartWebSocket(sdk_configuration)
        self.account = AccountWebSocket(sdk_configuration)
        self.parent_ref = parent_ref
