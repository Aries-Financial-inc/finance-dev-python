"""TradingView-compatible chart models."""

from typing import Any
from pydantic import Field
from .common import WireModel


class ChartSubscription(WireModel):
    symbol: str
    type: str = "quotes"
    symbol_type: str | None = Field(default=None, alias="symbolType")


class ChartEvent(WireModel):
    symbol: str | None = None
    data: Any = None


class TradingViewQuoteValues(WireModel):
    change: float | None = Field(default=None, alias="ch")
    change_percent: float | None = Field(default=None, alias="chp")
    last_price: float | None = Field(default=None, alias="lp")
    ask: float | None = None
    bid: float | None = None
    open_price: float | None = Field(default=None, alias="open_price")
    high_price: float | None = Field(default=None, alias="high_price")
    low_price: float | None = Field(default=None, alias="low_price")
    previous_close_price: float | None = Field(default=None, alias="prev_close_price")
    volume: float | None = None
    exchange: str | None = None
    short_name: str | None = None


class TradingViewQuote(WireModel):
    status: str | None = Field(default=None, alias="s")
    name: str | None = Field(default=None, alias="n")
    values: TradingViewQuoteValues | None = Field(default=None, alias="v")


class TradingViewTrade(WireModel):
    status: str | None = Field(default=None, alias="s")
    timestamp: int | None = Field(default=None, alias="t")
    last_price: float | None = Field(default=None, alias="lp")
    volume: float | None = Field(default=None, alias="v")
