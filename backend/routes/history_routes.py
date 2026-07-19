from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.services.history_service import (
    get_weather_history,
    get_aqi_history,
    get_prediction_history,
    fetch_user_search_history  # Nayi dashboard service yahan import ki hai
)

# Professional routing setup
router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/weather")
def fetch_weather_history(db: Session = Depends(get_db)):
    return get_weather_history(db)


@router.get("/aqi")
def fetch_aqi_history(db: Session = Depends(get_db)):
    return get_aqi_history(db)


@router.get("/prediction")
def fetch_prediction_history(db: Session = Depends(get_db)):
    return get_prediction_history(db)


# ==========================================
# 2. BFF Endpoint (Specifically for history.html Dashboard)
# ==========================================

@router.get("/dashboard/{city}")
def get_dashboard_analytics(city: str, db: Session = Depends(get_db)):
    """
    Returns structured JSON payload including KPIs, Chart arrays, 
    and formatted table rows for the History Dashboard UI.
    """
    data = fetch_user_search_history(db=db, city=city)
    return data