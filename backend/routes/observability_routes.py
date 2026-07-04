# backend/routes/observability_routes.py
from fastapi import APIRouter
from backend.services.observability_service import fetch_system_metrics

router = APIRouter(
    prefix="/observability",
    tags=["System Observability"]
)

@router.get("/metrics")
def get_observability_metrics():
    """
    BFF Endpoint to fetch real-time server health and logs.
    """
    return fetch_system_metrics()