"""Errors raised by Aries WebSocket clients."""

import re

_SECRET_PATTERN = re.compile(
    r"(?i)(token|client[_-]?secret|authorization)(\s*[=:]\s*)([^\s,}\]]+)"
)
_BEARER_PATTERN = re.compile(r"(?i)(authorization\s*:\s*bearer\s+)[^\s,}\]]+")


def _redact(message: str) -> str:
    message = _BEARER_PATTERN.sub(r"\1[REDACTED]", message)
    return _SECRET_PATTERN.sub(r"\1\2[REDACTED]", message)


class AriesWebSocketError(Exception):
    """Base class for websocket SDK failures."""

    def __init__(self, message=""):
        super().__init__(_redact(str(message)))


class WebSocketConfigurationError(AriesWebSocketError):
    pass


class WebSocketConnectionError(AriesWebSocketError):
    pass


class WebSocketConnectionStateError(WebSocketConnectionError):
    pass


class WebSocketReconnectExhaustedError(WebSocketConnectionError):
    pass


class WebSocketAuthenticationError(AriesWebSocketError):
    pass


class WebSocketRequestError(AriesWebSocketError):
    def __init__(self, message: str, *, status=None, code=None, request_id=None):
        super().__init__(message)
        self.status, self.code, self.request_id = status, code, request_id


class WebSocketProtocolError(AriesWebSocketError):
    pass


class WebSocketBackpressureError(AriesWebSocketError):
    pass
