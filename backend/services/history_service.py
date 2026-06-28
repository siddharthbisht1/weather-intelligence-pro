from sqlalchemy.orm import Session
from backend.models import (
    WeatherHistory,
    AQIHistory,
    Prediction
)


# ==========================================
# Get Weather History
# ==========================================

def get_weather_history(db: Session, limit: int = 100):
    return (
        db.query(WeatherHistory)
        .order_by(WeatherHistory.id.desc())
        .limit(limit)
        .all()
    )


# ==========================================
# Get AQI History
# ==========================================

def get_aqi_history(db: Session, limit: int = 100):
    return (
        db.query(AQIHistory)
        .order_by(AQIHistory.id.desc())
        .limit(limit)
        .all()
    )


# ==========================================
# Get Prediction History
# ==========================================

def get_prediction_history(db: Session, limit: int = 100):
    return (
        db.query(Prediction)
        .order_by(Prediction.id.desc())
        .limit(limit)
        .all()
    )