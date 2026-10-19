# Hand-maintained WebSocket tests; preserved by Speakeasy persistent edits.
import json

import pytest_asyncio
from websockets.asyncio.server import serve

@pytest_asyncio.fixture
async def local_ws_server():
    received = []

    async def handler(socket):
        async for frame in socket:
            for line in frame.splitlines():
                if not line.strip():
                    continue
                message = json.loads(line)
                received.append(message)
                ident = message.get("id")
                if message.get("type") == "request" and message.get("payload", {}).get("path") == "/auth":
                    await socket.send(json.dumps({"type":"event","payload":{"action":"authSuccess","id":ident}}))
                elif message.get("type") == "ping":
                    await socket.send(json.dumps({"type":"pong","id":ident}))
                elif message.get("type") == "subscribe" and isinstance(message.get("payload"), dict):
                    topic = message["payload"].get("topic")
                    if topic:
                        await socket.send(json.dumps({"type":"subscribed","id":ident,"payload":{"status":200,"topic":topic,"data":[]}}))
                    else:
                        await socket.send(json.dumps({"type":"event","payload":{"action":"snapshot","id":ident,"symbol":"AAPL","type":"quote","data":{"bidPrice":1}}}))
                elif message.get("type") == "subscribe" and isinstance(message.get("payload"), list):
                    await socket.send("\n".join(json.dumps({"type":"event","payload":{"sequence":n}}) for n in range(3)))
                elif message.get("type") == "request":
                    await socket.send(json.dumps({"type":"response","id":ident,"payload":{"status":200,"data":{"ok":True}}}))
                elif message.get("type") == "unsubscribe":
                    await socket.send(json.dumps({"type":"response","id":ident,"payload":{"status":200,"data":{"unsubscribed":True}}}))

    server = await serve(handler, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    try:
        yield f"ws://127.0.0.1:{port}", received
    finally:
        server.close()
        await server.wait_closed()

@pytest_asyncio.fixture
async def reconnecting_ws_server():
    received = []
    count = 0

    async def handler(socket):
        nonlocal count
        count += 1
        connection_number = count
        async for frame in socket:
            for line in frame.splitlines():
                message = json.loads(line); received.append((connection_number, message))
                ident = message.get("id")
                if message.get("type") == "request" and message.get("payload", {}).get("path") == "/auth":
                    await socket.send(json.dumps({"type":"event","payload":{"action":"authSuccess","id":ident}}))
                elif message.get("type") == "ping" and connection_number == 1:
                    await socket.send(json.dumps({"type":"event","payload":{"action":"authExpired","id":"system"}}))
                    await socket.close()
                    return
                elif message.get("type") == "ping":
                    await socket.send(json.dumps({"type":"pong","id":ident}))
                elif message.get("type") == "subscribe":
                    await socket.send(json.dumps({"type":"subscribed","id":ident,"payload":{"status":200,"topic":"watchlist","data":[]}}))

    server = await serve(handler, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    try: yield f"ws://127.0.0.1:{port}", received
    finally:
        server.close(); await server.wait_closed()
