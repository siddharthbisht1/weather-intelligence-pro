from fastapi import WebSocket
from typing import List

# ==========================================
# Connection Manager
# ==========================================

class ConnectionManager:
    def __init__(self):
        # Keeps track of all currently connected users
        self.active_connections: List[WebSocket] = []

    # ======================================
    # Connect
    # ======================================
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    # ======================================
    # Disconnect
    # ======================================
    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    # ======================================
    # Send Personal Message
    # ======================================
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    # ======================================
    # Broadcast Message
    # ======================================
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

# ==========================================
# Create Manager Instance
# ==========================================

manager = ConnectionManager()