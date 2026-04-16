from fastapi import APIRouter, WebSocket
import asyncio
from app.processing.store_instance import metrics_store
from app.processing.worker import get_alert_engine

router = APIRouter()

@router.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket.accept()

    engine = get_alert_engine()

    while True:
        data = metrics_store.snapshot()

        data["bandwidth_rate"] = metrics_store.get_bandwidth_rate()
        data["pps"] = metrics_store.get_packets_per_second()

        data["alerts"] = engine.get_alerts() 

        await websocket.send_json(data)
        await asyncio.sleep(1)