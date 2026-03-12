from fastapi import WebSocket
from collections import defaultdict

class WebSocketService:

    def __init__(self):
        # room_id -> list of connections
        self.rooms: dict[str, list[WebSocket]] = defaultdict(list)

    async def connect(self, websocket: WebSocket, room_id: str):
        await websocket.accept()
        self.rooms[room_id].append(websocket)

    def disconnect(self, websocket: WebSocket, room_id: str):
        if websocket in self.rooms[room_id]:
            self.rooms[room_id].remove(websocket)

        # clean empty room
        if not self.rooms[room_id]:
            del self.rooms[room_id]

    async def broadcast(self, room_id: str, message: str):
        for connection in self.rooms.get(room_id, []):
            await connection.send_text(message)


ws_service = WebSocketService()