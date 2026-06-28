from fastapi import APIRouter, WebSocket, WebSocketDisconnect

# Make sure this import path matches where your manager file lives!
from backend.websocket_manager import manager

router = APIRouter(
    tags=["WebSocket"]
)

# ==========================================
# WebSocket Endpoint
# ==========================================

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    
    try:
        while True:
            # Wait for a message from the client
            data = await websocket.receive_text()
            
            # Broadcast that message to all connected clients
            await manager.broadcast(f"Client says: {data}")
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A user disconnected.")