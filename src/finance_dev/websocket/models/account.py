"""Account topic subscription models."""

from datetime import datetime
from typing import Any
from pydantic import Field, field_validator
from .common import WireModel


class AccountSubscription(WireModel):
    account_id: str = Field(alias="accountId")


class PnlSubscription(WireModel):
    account_id: str = Field(alias="accountId")
    start_time: datetime | str
    interval: str = "1m"

    @field_validator("start_time")
    @classmethod
    def aware_start(cls, value):
        if isinstance(value, datetime) and value.tzinfo is None:
            raise ValueError("start_time must be timezone-aware")
        if isinstance(value, str) and (
            "T" not in value
            or not (value.endswith("Z") or "+" in value[10:] or "-" in value[10:])
        ):
            raise ValueError("start_time must be an RFC3339 timestamp")
        return value


class WatchlistSubscription(WireModel):
    pass


class NewsSubscription(WireModel):
    symbols: list[str] | None = None
    topics: list[str] | None = None


class AccountSnapshot(WireModel):
    account: dict
    positions: list[dict]
    ordersV2: list[dict]


class AccountEvent(WireModel):
    topic: str = "account"
    name: str
    target: str | None = None
    data: dict[str, Any]


class PnlEvent(WireModel):
    topic: str = "pnl"
    data: dict[str, Any]


class TopicEvent(WireModel):
    topic: str
    data: list[dict[str, Any]]
