from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.modules.auth.dependencies import get_current_user
from app.modules.chat.services import ws_service

chat_router = APIRouter()


@chat_router.websocket("/ws/{room_id}")
async def join_room(websocket: WebSocket, room_id: str = None, current_user = Depends(get_current_user)):
    await ws_service.connect(websocket, room_id)

    try:
        while True:
            message = await websocket.receive_text()

            await ws_service.broadcast(
                room_id,
                f"[{room_id}] {message}"
            )

    except WebSocketDisconnect:
        ws_service.disconnect(websocket, room_id)