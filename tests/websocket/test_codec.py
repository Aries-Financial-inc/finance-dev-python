# Hand-maintained WebSocket tests; preserved by Speakeasy persistent edits.
import pytest
from finance_dev.websocket.codec import decode_frame, encode_message
from finance_dev.websocket.errors import WebSocketProtocolError

def test_decode_ndjson_bytes_unknown_and_blank_lines():
    decoded = decode_frame(b'{"type":"event","payload":{"n":1}}\n\n{"type":"future","x":2}')
    assert decoded[0].model_dump(exclude_none=True) == {"type":"event","payload":{"n":1}}
    assert decoded[1].original == {"type":"future","x":2}

@pytest.mark.parametrize("frame", ["{", "[]", b"\xff"])
def test_decode_rejects_invalid_frames(frame):
    with pytest.raises(WebSocketProtocolError): decode_frame(frame)

def test_encoder_is_compact():
    assert encode_message({"a": 1, "b": 2}) == '{"a":1,"b":2}'
