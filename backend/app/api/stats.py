from fastapi import APIRouter
from app.processing.store_instance import metrics_store  # SAME INSTANCE

router = APIRouter()

@router.get("/stats")
def get_stats():
    return metrics_store.snapshot()