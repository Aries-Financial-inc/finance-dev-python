"""WebSocket endpoint URLs and validated connection settings."""

from dataclasses import dataclass
import math
from .errors import WebSocketConfigurationError

MARKET_URL = "wss://api.aries.com/v1/market/ws"
CHART_URL = "wss://api.aries.com/v1/charts/ws"
ACCOUNT_URL = "wss://api.aries.com/v1/accounts/ws"


@dataclass(frozen=True)
class WebSocketConfig:
    connect_timeout: float = 10.0
    auth_timeout: float = 4.0
    request_timeout: float = 10.0
    ping_interval: float = 30.0
    pong_timeout: float = 10.0
    close_timeout: float = 10.0
    reconnect: bool = True
    replay_subscriptions: bool = True
    reconnect_initial_delay: float = 1.0
    reconnect_max_delay: float = 60.0
    reconnect_jitter: float = 0.2
    incoming_queue_size: int = 1000
    max_message_size: int = 1_048_576

    def __post_init__(self):
        for key in (
            "connect_timeout",
            "auth_timeout",
            "request_timeout",
            "ping_interval",
            "pong_timeout",
            "close_timeout",
            "reconnect_initial_delay",
            "reconnect_max_delay",
        ):
            if not math.isfinite(getattr(self, key)) or getattr(self, key) <= 0:
                raise WebSocketConfigurationError(f"{key} must be positive")
        if self.reconnect_max_delay < self.reconnect_initial_delay:
            raise WebSocketConfigurationError(
                "reconnect_max_delay must be at least reconnect_initial_delay"
            )
        if not 0 <= self.reconnect_jitter <= 1:
            raise WebSocketConfigurationError(
                "reconnect_jitter must be between 0 and 1"
            )
        if self.incoming_queue_size < 1 or self.max_message_size < 1:
            raise WebSocketConfigurationError(
                "queue size and max_message_size must be positive"
            )
