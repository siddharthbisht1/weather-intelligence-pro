from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.services.history_service import (
    get_weather_history,
    get_aqi_history,
    get_prediction_history
)

router = APIRouter(
    prefix="/history",
    tags=["History"]
)

# ==========================================
# Get Weather History
# ==========================================

@router.get("/weather")
def fetch_weather_history(
    db: Session = Depends(get_db)
):
    return get_weather_history(db)

# ==========================================
# Get AQI History
# ==========================================

@router.get("/aqi")
def fetch_aqi_history(
    db: Session = Depends(get_db)
):
    return get_aqi_history(db)

# ==========================================
# Get Prediction History
# ==========================================

@router.get("/prediction")
def fetch_prediction_history(
    db: Session = Depends(get_db)
):
    return get_prediction_history(db)