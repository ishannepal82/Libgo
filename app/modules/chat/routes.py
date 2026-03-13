from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request
from app.dependencies.auth import require_auth
from app.modules.chat.services import ws_service

chat_router = APIRouter()


@chat_router.websocket("/ws/{room_id}")
@require_auth
async def join_room(
    user, websocket: WebSocket, room_id: str = None, request: Request = None
):
    await ws_service.connect(websocket, room_id)

    try:
        while True:
            message = await websocket.receive_text()

            await ws_service.broadcast(room_id, f"[{room_id}] {message}")

    except WebSocketDisconnect:
        ws_service.disconnect(websocket, room_id)
