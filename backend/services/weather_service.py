import os
import requests
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from backend.models import WeatherHistory

API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_and_save_weather(city: str, db: Session, user_id: int = None):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": f"City '{city}' not found or API error"}

    data = response.json()

    db_weather = WeatherHistory(
        user_id=user_id,
        city=data["name"],
        temperature=data["main"]["temp"],
        humidity=data["main"]["humidity"],
        wind_speed=data["wind"]["speed"],
        searched_at=datetime.now(timezone.utc)
    )

    try:
        db.add(db_weather)
        db.commit()
        db.refresh(db_weather)
        return db_weather
        
    except Exception as e:
        db.rollback()
        return {"error": f"Database insertion failed: {str(e)}"}