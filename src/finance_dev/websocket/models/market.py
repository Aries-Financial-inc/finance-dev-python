"""Forward-compatible market subscription and event models."""

from typing import Any
from pydantic import Field
from .common import WireModel


class MarketSubscription(WireModel):
    """Use '*' for all fields. Time & Sales alone does not enable quotes/trades."""

    symbol: str
    symbol_type: str | None = Field(default=None, alias="symbolType")
    quote_fields: list[str] | str | None = Field(default=None, alias="quoteFields")
    trade_fields: list[str] | str | None = Field(default=None, alias="tradeFields")
    level2: bool | None = None
    time_and_sales: bool | None = Field(default=None, alias="timeAndSales")
    time_and_sales_fields: list[str] | str | None = Field(
        default=None, alias="timeAndSalesFields"
    )
    greeks_fields: list[str] | str | None = Field(default=None, alias="greeksFields")


class MarketUnsubscribe(WireModel):
    symbol: str
    quote: bool | None = None
    trade: bool | None = None
    level2: bool | None = None
    time_and_sales: bool | None = Field(default=None, alias="timeAndSales")
    greeks: bool | None = None
    quote_fields: list[str] | None = Field(default=None, alias="quoteFields")
    trade_fields: list[str] | None = Field(default=None, alias="tradeFields")
    greeks_fields: list[str] | None = Field(default=None, alias="greeksFields")


class MarketEvent(WireModel):
    type: str | None = None
    action: str | None = None
    symbol: str | None = None
    data: Any = None


class QuoteData(WireModel):
    """Bid/ask data; fields may be absent in partial updates.

    Timestamps are Unix milliseconds. Unknown fields are preserved.
    """

    bid_price: float | None = Field(default=None, alias="bidPrice")
    bid_change: float | None = Field(default=None, alias="bidChange")
    bid_size: int | None = Field(default=None, alias="bidSize")
    bid_size_change: int | None = Field(default=None, alias="bidSizeChange")
    bid_timestamp: int | None = Field(default=None, alias="bidTimestamp")
    bid_exchange: str | None = Field(default=None, alias="bidExchange")
    ask_price: float | None = Field(default=None, alias="askPrice")
    ask_change: float | None = Field(default=None, alias="askChange")
    ask_size: int | None = Field(default=None, alias="askSize")
    ask_size_change: int | None = Field(default=None, alias="askSizeChange")
    ask_timestamp: int | None = Field(default=None, alias="askTimestamp")
    ask_exchange: str | None = Field(default=None, alias="askExchange")
    quote_timestamp: int | None = Field(default=None, alias="quoteTimestamp")
    mid_price: float | None = Field(default=None, alias="midPrice")
    spread: float | None = None


class TradeData(WireModel):
    """Last sale, volume, and OHLC data; fields may be absent in updates.

    Timestamps are Unix milliseconds. Unknown fields are preserved.
    """

    price: float | None = None
    size: int | None = None
    total_volume: int | None = Field(default=None, alias="totalVolume")
    tick_volume: int | None = Field(default=None, alias="tickVolume")
    open_price: float | None = Field(default=None, alias="openPrice")
    high_price: float | None = Field(default=None, alias="highPrice")
    low_price: float | None = Field(default=None, alias="lowPrice")
    last_price: float | None = Field(default=None, alias="lastPrice")
    net_change: float | None = Field(default=None, alias="netChange")
    tick: str | None = None
    trade_seq: int | None = Field(default=None, alias="tradeSeq")
    trade_timestamp: int | None = Field(default=None, alias="tradeTimestamp")
    close_price: float | None = Field(default=None, alias="closePrice")
    previous_close_price: float | None = Field(default=None, alias="previousClosePrice")


class Level2Data(WireModel):
    order_book: Any = Field(default=None, alias="orderBook")
    quotes: Any = None

    @staticmethod
    def parse_row(row: str, *, separator: str = ",") -> list[str]:
        """Safely split compact server rows without imposing a numeric schema."""
        return row.split(separator)


class TimeAndSalesData(WireModel):
    """A single execution, with string prices, sizes, and Unix millisecond times.

    Fields may be absent when selected individually. Unknown fields are preserved.
    """

    symbol: str | None = None
    price: str | None = None
    size: str | None = None
    tick: str | None = None
    trade_seq: str | None = Field(default=None, alias="tradeSeq")
    trade_exchange: str | None = Field(default=None, alias="tradeExchange")
    trade_timestamp: str | None = Field(default=None, alias="tradeTimestamp")


class GreeksData(WireModel):
    pass
