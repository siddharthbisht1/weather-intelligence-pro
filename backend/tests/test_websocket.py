from fastapi.testclient import TestClient
# In every test file, change the import to:
from backend.main import app

client = TestClient(app)


# ==========================================
# WebSocket Connection Test
# ==========================================

def test_websocket_connection():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("Hello Server")
        response = websocket.receive_text()
        assert response is not None


# ==========================================
# Message Type Test
# ==========================================

def test_websocket_message():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("Weather Intelligence Pro")
        response = websocket.receive_text()
        assert isinstance(response, str)


# ==========================================
# Multiple Messages Test
# ==========================================

def test_multiple_messages():
    with client.websocket_connect("/ws") as websocket:
        messages = ["Hello", "Weather", "AQI"]
        
        for msg in messages:
            websocket.send_text(msg)
            response = websocket.receive_text()
            assert response is not None