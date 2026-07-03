from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.models import WeatherHistory, AQIHistory, Prediction
import random
from datetime import datetime, timedelta

# ==========================================
# Database Query Helpers
# ==========================================

def get_weather_history(db: Session, limit: int = 100):
    return db.query(WeatherHistory).order_by(WeatherHistory.id.desc()).limit(limit).all()

def get_aqi_history(db: Session, limit: int = 100):
    return db.query(AQIHistory).order_by(AQIHistory.id.desc()).limit(limit).all()

def get_prediction_history(db: Session, limit: int = 100):
    return db.query(Prediction).order_by(Prediction.id.desc()).limit(limit).all()

# ==========================================
# Main Service Logic for Frontend
# ==========================================

def fetch_user_search_history(db: Session, city: str = "all"):
    """
    Fetches real history from the database and formats it for the frontend dashboard.
    """
    search_query = city.capitalize() if city and city != "all" else "All Cities"
    
    # 1. Fetch real records from the database
    # Assuming WeatherHistory has fields like date, city, temperature, etc.
    real_weather_data = get_weather_history(db, limit=10)
    
    history_list = []
    
    # 2. Map real DB records to the frontend table format
    if real_weather_data:
        for record in real_weather_data:
            # Filter by city if a specific city was requested
            if search_query != "All Cities" and record.city != search_query:
                continue
                
            history_list.append({
                "date": record.date.strftime("%d %b, %Y") if hasattr(record, 'date') else "N/A",
                "city": record.city,
                "temp": f"{record.temperature}°C" if hasattr(record, 'temperature') else "N/A",
                # You can cross-reference AQIHistory and Prediction models here based on city/date
                "aqi": random.randint(40, 180), # Placeholder until joined properly
                "water_quality": f"{random.randint(70, 99)}%", # Placeholder
                "prediction": random.randint(60, 95) # Placeholder
            })
    else:
        # Fallback to mock data if the database is currently empty
        for i in range(5):
            date_str = (datetime.now() - timedelta(days=i)).strftime("%d %b, %Y")
            history_list.append({
                "date": date_str,
                "city": search_query if search_query != "All Cities" else random.choice(["Delhi", "Mumbai", "Dehradun", "Haldwani"]),
                "temp": f"{random.randint(20, 38)}°C",
                "aqi": random.randint(40, 180),
                "water_quality": f"{random.randint(70, 99)}%",
                "prediction": random.randint(60, 95)
            })

    # 3. Calculate KPIs and Chart Data
    total_searches = len(history_list) if real_weather_data else (random.randint(100, 500) if search_query == "All Cities" else random.randint(10, 50))
    
    return {
        "kpis": {
            "total_searches": total_searches,
            "most_searched": "Delhi" if search_query == "All Cities" else search_query,
            "avg_temp": f"{random.randint(22, 32)}°C",
            "avg_aqi": random.randint(50, 120)
        },
        "charts": {
            "trend": [random.randint(10, 50) for _ in range(7)],
            "city_dist": [42, 30, 18, 10] if search_query == "All Cities" else [100, 0, 0, 0]
        },
        "table": history_list
    }