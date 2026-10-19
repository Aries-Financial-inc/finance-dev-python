"""JSON/NDJSON wire codec."""

import json
from typing import Any
from .errors import WebSocketProtocolError
from .models.common import (
    EventMessage,
    PingMessage,
    PongMessage,
    RequestMessage,
    ResponseMessage,
    SubscribeMessage,
    SubscribedMessage,
    UnknownMessage,
    UnsubscribeMessage,
)

_MODELS = {
    "request": RequestMessage,
    "response": ResponseMessage,
    "event": EventMessage,
    "subscribe": SubscribeMessage,
    "unsubscribe": UnsubscribeMessage,
    "subscribed": SubscribedMessage,
    "ping": PingMessage,
    "pong": PongMessage,
}


def decode_frame(frame: str | bytes) -> list[Any]:
    if isinstance(frame, bytes):
        try:
            frame = frame.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise WebSocketProtocolError(
                "invalid UTF-8 websocket frame at line 1"
            ) from exc
    messages: list[Any] = []
    for line_no, line in enumerate(frame.splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except (json.JSONDecodeError, ValueError) as exc:
            raise WebSocketProtocolError(f"invalid JSON at line {line_no}") from exc
        if not isinstance(value, dict):
            raise WebSocketProtocolError(
                f"JSON value must be an object at line {line_no}"
            )
        model_type: Any = _MODELS.get(str(value.get("type")))
        if model_type is None:
            messages.append(UnknownMessage(original=value))
            continue
        try:
            messages.append(model_type.model_validate(value))
        except Exception as exc:
            raise WebSocketProtocolError(
                f"invalid {value.get('type')} message at line {line_no}"
            ) from exc
    return messages


def encode_message(message: Any) -> str:
    if hasattr(message, "model_dump"):
        message = message.model_dump(by_alias=True, exclude_none=True)
    return json.dumps(message, separators=(",", ":"), ensure_ascii=False)
