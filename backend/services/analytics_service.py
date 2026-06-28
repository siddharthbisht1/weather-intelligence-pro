from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.models import (
    WeatherHistory,
    AQIHistory,
    Prediction,
    User
)

# ==========================================
# Total Users
# ==========================================

def get_total_users(db: Session):
    return db.query(User).count()


# ==========================================
# Total Weather Searches
# ==========================================

def get_total_weather_searches(db: Session):
    return db.query(WeatherHistory).count()


# ==========================================
# Total AQI Searches
# ==========================================

def get_total_aqi_searches(db: Session):
    return db.query(AQIHistory).count()


# ==========================================
# Total Predictions
# ==========================================

def get_total_predictions(db: Session):
    return db.query(Prediction).count()


# ==========================================
# Average Temperature (Optimized)
# ==========================================

def get_average_temperature(db: Session):
    # Let the database do the math!
    avg_temp = db.query(func.avg(WeatherHistory.temperature)).scalar()
    
    if avg_temp is None:
        return 0.0

    return round(avg_temp, 2)


# ==========================================
# Average AQI (Optimized)
# ==========================================

def get_average_aqi(db: Session):
    # Let the database do the math!
    avg_aqi = db.query(func.avg(AQIHistory.aqi)).scalar()
    
    if avg_aqi is None:
        return 0

    return round(avg_aqi, 2)


# ==========================================
# Dashboard Analytics
# ==========================================

def get_dashboard_analytics(db: Session):
    return {
        "total_users": get_total_users(db),
        "weather_searches": get_total_weather_searches(db),
        "aqi_searches": get_total_aqi_searches(db),
        "predictions": get_total_predictions(db),
        "average_temperature": get_average_temperature(db),
        "average_aqi": get_average_aqi(db)
    }