import os
import requests
from datetime import datetime, timezone  # <--- FIX: timezone yahan top par add kiya
from sqlalchemy.orm import Session
from backend.models import WeatherHistory
from backend.schemas import WeatherCreate

API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_and_save_weather(city: str, db: Session):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": f"City '{city}' not found or API error"}

    data = response.json()

    # Sirf wahi fields bhejo jo database table mein existing hain
    db_weather = WeatherHistory(
        city=data["name"],
        temperature=data["main"]["temp"],
        humidity=data["main"]["humidity"],
        wind_speed=data["wind"]["speed"]
        # 'recorded_at' ya 'searched_at' ko yahan mat bhejo!
    )

    try:
        db.add(db_weather)
        db.commit()
        db.refresh(db_weather)
        
        # FIX: Yahan ab direct call karenge kyunki import upar ho chuka hai
        if hasattr(db_weather, "searched_at"):
            db_weather.searched_at = datetime.now(timezone.utc)
            db.commit()
            db.refresh(db_weather)

        return db_weather
        
    except Exception as e:
        db.rollback()
        return {"error": f"Database insertion failed: {str(e)}"}