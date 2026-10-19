# Hand-maintained WebSocket tests; preserved by Speakeasy persistent edits.
import json
from pathlib import Path

import pytest
from finance_dev.websocket.codec import decode_frame
from finance_dev.websocket.models import (
    MarketSubscription, PnlSubscription, TradingViewQuote,
    QuoteData, TradeData, TimeAndSalesData,
)

FIXTURES = Path(__file__).parent / "fixtures"

@pytest.mark.parametrize("filename, count", [("market.json", 3), ("chart.json", 1), ("account.json", 3)])
def test_official_examples_decode(filename, count):
    frame = (FIXTURES / filename).read_text()
    assert len(decode_frame(frame)) == count

def test_subscription_aliases_match_wire_format():
    item = MarketSubscription(symbol="AAPL", symbol_type="equity", time_and_sales=True)
    assert item.model_dump(by_alias=True, exclude_none=True) == {
        "symbol": "AAPL", "symbolType": "equity", "timeAndSales": True
    }

def test_tradingview_short_form_fields_are_descriptive_in_python():
    quote = TradingViewQuote.model_validate({"s":"ok", "n":"AAPL", "v":{"ch":2,"lp":10,"short_name":"Apple"}})
    assert quote.values.change == 2
    assert quote.values.last_price == 10
    assert quote.values.short_name == "Apple"

def test_pnl_requires_timezone_and_documented_interval():
    with pytest.raises(ValueError): PnlSubscription(account_id="a", start_time="2026-01-01T00:00:00")
    assert PnlSubscription(account_id="a", start_time="2026-01-01T00:00:00Z").interval == "1m"


@pytest.mark.parametrize("model, data, attribute, expected", [
    (QuoteData, {"bidPrice": 189.94, "quoteTimestamp": 1701450000000}, "bid_price", 189.94),
    (TradeData, {"lastPrice": 189.95, "totalVolume": 100}, "total_volume", 100),
    (TimeAndSalesData, {"price": "189.95", "tradeSeq": "123"}, "trade_seq", "123"),
])
def test_market_data_helpers_preserve_partial_updates_and_unknown_fields(model, data, attribute, expected):
    payload = {**data, "futureField": {"value": 1}}
    parsed = model.model_validate(payload)
    assert getattr(parsed, attribute) == expected
    assert parsed.model_dump(by_alias=True, exclude_none=True) == payload
    assert model.model_validate({}).model_dump(exclude_none=True) == {}


def test_combined_market_streams_use_explicit_field_wildcards():
    item = MarketSubscription(
        symbol="AAPL", quote_fields="*", trade_fields="*", time_and_sales=True
    )
    assert item.model_dump(by_alias=True, exclude_none=True) == {
        "symbol": "AAPL", "quoteFields": "*", "tradeFields": "*", "timeAndSales": True
    }
