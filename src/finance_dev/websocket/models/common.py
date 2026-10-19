"""Forward-compatible common protocol models."""

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class WireModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class RequestMessage(WireModel):
    type: Literal["request"] = "request"
    id: str
    payload: dict[str, Any]


class ResponseMessage(WireModel):
    type: Literal["response"] = "response"
    id: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)


class ErrorResponse(ResponseMessage):
    pass


class AuthRequest(RequestMessage):
    pass


class AuthEvent(WireModel):
    type: str | None = None
    id: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)


class SubscribeMessage(WireModel):
    type: Literal["subscribe"] = "subscribe"
    id: str | None = None
    payload: Any


class UnsubscribeMessage(WireModel):
    type: Literal["unsubscribe"] = "unsubscribe"
    id: str | None = None
    payload: Any


class SubscribedMessage(WireModel):
    type: Literal["subscribed"] = "subscribed"
    id: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)


class EventMessage(WireModel):
    type: Literal["event"] = "event"
    id: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)


class PingMessage(WireModel):
    type: Literal["ping"] = "ping"
    id: str | None = None


class PongMessage(WireModel):
    type: Literal["pong"] = "pong"
    id: str | None = None


class UnknownMessage(WireModel):
    original: dict[str, Any]


InboundMessage = (
    RequestMessage
    | ResponseMessage
    | EventMessage
    | SubscribeMessage
    | UnsubscribeMessage
    | SubscribedMessage
    | PingMessage
    | PongMessage
    | UnknownMessage
)
