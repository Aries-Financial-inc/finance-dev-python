# Hand-maintained WebSocket tests; preserved by Speakeasy persistent edits.
import asyncio

from finance_dev.websocket.models import MarketSubscription
from finance_dev.websocket.resources import AccountResource, ChartResource, MarketResource

class FakeStream:
    def __init__(self): self.messages=[]; self._active={}; self.counter=0
    def _id(self,prefix): self.counter+=1; return f"{prefix}-{self.counter}"
    def send_message(self,message): self.messages.append(message); return message["id"]
    def exchange(self,message): self.messages.append(message); return {"type":"subscribed","id":message["id"],"payload":{"status":200}}

def test_market_payload_is_always_an_array_and_chart_sends_one_symbol():
    stream=FakeStream()
    MarketResource(None).subscribe(stream,[MarketSubscription(symbol="AAPL",quote_fields=["bidPrice"])])
    assert stream.messages[-1]["type"]=="subscribe"
    assert stream.messages[-1]["payload"]==[{"symbol":"AAPL","quoteFields":["bidPrice"]}]
    ChartResource(None).subscribe(stream,"AAPL",data_type="bars")
    assert stream.messages[-1]["payload"]=={"type":"bars","symbol":"AAPL"}

def test_account_subscribe_waits_for_correlated_subscribed_response():
    stream=FakeStream()
    ack=AccountResource(None).subscribe_account(stream,"ACC123")
    assert ack["type"]=="subscribed"
    assert stream.messages[-1]["type"]=="subscribe"
    assert stream.messages[-1]["payload"]=={"topic":"account","params":{"accountId":"ACC123"}}

def test_chart_async_subscribe_has_wire_aliases():
    stream=FakeStream()
    async def send(message): stream.messages.append(message)
    stream.send_message=send
    async def run(): await ChartResource(None).subscribe_async(stream,"SPY",symbol_type="option")
    asyncio.run(run())
    assert stream.messages[0]["payload"]=={"type":"quotes","symbol":"SPY","symbolType":"option"}
