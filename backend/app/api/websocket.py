from fastapi import APIRouter, WebSocket
import asyncio
from app.processing.store_instance import metrics_store

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket client connected")

    try:
        while True:
            data = metrics_store.snapshot()
            await websocket.send_json(data)
            await asyncio.sleep(1)

    except Exception as e:
        print("WebSocket disconnected:", e)