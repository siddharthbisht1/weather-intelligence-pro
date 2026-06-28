from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Updated to match your folder structure!
from backend.database import get_db

from backend.services.analytics_service import (
    get_dashboard_analytics,
    get_total_users,
    get_total_weather_searches,
    get_total_aqi_searches,
    get_total_predictions,
    get_average_temperature,
    get_average_aqi
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


# ==========================================
# Dashboard Analytics
# ==========================================

@router.get("/dashboard")
def dashboard_analytics(
    db: Session = Depends(get_db)
):
    return get_dashboard_analytics(db)


# ==========================================
# Total Users
# ==========================================

@router.get("/users")
def total_users(
    db: Session = Depends(get_db)
):
    return {
        "total_users": get_total_users(db)
    }


# ==========================================
# Weather Searches
# ==========================================

@router.get("/weather-searches")
def weather_searches(
    db: Session = Depends(get_db)
):
    return {
        "weather_searches": get_total_weather_searches(db)
    }


# ==========================================
# AQI Searches
# ==========================================

@router.get("/aqi-searches")
def aqi_searches(
    db: Session = Depends(get_db)
):
    return {
        "aqi_searches": get_total_aqi_searches(db)
    }


# ==========================================
# Predictions
# ==========================================

@router.get("/predictions")
def predictions(
    db: Session = Depends(get_db)
):
    return {
        "predictions": get_total_predictions(db)
    }


# ==========================================
# Average Temperature
# ==========================================

@router.get("/average-temperature")
def average_temperature(
    db: Session = Depends(get_db)
):
    return {
        "average_temperature": get_average_temperature(db)
    }


# ==========================================
# Average AQI
# ==========================================

@router.get("/average-aqi")
def average_aqi(
    db: Session = Depends(get_db)
):
    return {
        "average_aqi": get_average_aqi(db)
    }