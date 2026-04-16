from fastapi import APIRouter
from app.processing.store_instance import metrics_store
from app.processing.worker import get_alert_engine

router = APIRouter()

@router.get("/stats")
def get_stats():
    return metrics_store.snapshot()

@router.get("/alerts")
def get_alerts():
    engine = get_alert_engine()
    return engine.get_alerts()