import os
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from backend.models import AQIHistory

load_dotenv()
AQICN_TOKEN = os.getenv("AQICN_API_TOKEN")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_aqi_service(city: str, db: Session = None, user_id: int = None):
    
    result_data = None

    # ==========================================
    # PLAN A: Try AQICN API (Best Accuracy - Ground Sensors)
    # ==========================================
    if AQICN_TOKEN:
        try:
            waqi_url = f"https://api.waqi.info/feed/{city}/?token={AQICN_TOKEN}"
            res = requests.get(waqi_url).json()
            
            if res.get("status") == "ok":
                data = res["data"]
                aqi_val = data.get("aqi")
                
                if str(aqi_val).isdigit(): 
                    aqi_val = int(aqi_val)
                    status = "Good" if aqi_val <= 50 else "Satisfactory" if aqi_val <= 100 else "Moderate" if aqi_val <= 200 else "Poor" if aqi_val <= 300 else "Severe"
                    
                    result_data = {
                        "city": data.get("city", {}).get("name", city.capitalize()),
                        "aqi": aqi_val,
                        "status": status,
                        "pm25": data.get("iaqi", {}).get("pm25", {}).get("v", 0),
                        "pm10": data.get("iaqi", {}).get("pm10", {}).get("v", 0),
                        "co": data.get("iaqi", {}).get("co", {}).get("v", 0),
                        "no2": data.get("iaqi", {}).get("no2", {}).get("v", 0),
                        "so2": data.get("iaqi", {}).get("so2", {}).get("v", 0),
                        "lat": data.get("city", {}).get("geo", [0, 0])[0],
                        "lon": data.get("city", {}).get("geo", [0, 0])[1],
                        "source": "AQICN (Accurate Sensor)"
                    }
        except Exception as e:
            print(f"AQICN Request Failed: {e}")

    # ==========================================
    # PLAN B: Fallback to OpenWeather API (Satellite Estimate)
    # ==========================================
    if not result_data and OPENWEATHER_KEY:
        try:
            geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={OPENWEATHER_KEY}"
            geo_data = requests.get(geo_url).json()
            
            if geo_data:
                lat, lon = geo_data[0]["lat"], geo_data[0]["lon"]
                aqi_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={OPENWEATHER_KEY}"
                
                aqi_data = requests.get(aqi_url).json()
                
                pollution = aqi_data["list"][0]
                pm25 = pollution["components"]["pm2_5"]
                
                calculated_aqi = int(pm25 * 2.75) 
                status = "Good" if calculated_aqi <= 50 else "Satisfactory" if calculated_aqi <= 100 else "Moderate" if calculated_aqi <= 200 else "Poor" if calculated_aqi <= 300 else "Severe"
                
                result_data = {
                    "city": city.capitalize(),
                    "aqi": calculated_aqi,
                    "status": status,
                    "pm25": pm25,
                    "pm10": pollution["components"]["pm10"],
                    "co": pollution["components"]["co"],
                    "no2": pollution["components"]["no2"],
                    "so2": pollution["components"]["so2"],
                    "lat": lat,
                    "lon": lon,
                    "source": "OpenWeather (Satellite Estimate)"
                }
        except Exception as e:
            print(f"OpenWeather Request Failed: {e}")

    # ==========================================
    # 💾 Save to Database Logic
    # ==========================================
    if result_data and db:
        try:
            new_aqi_history = AQIHistory(
                user_id=user_id,
                city=result_data["city"],
                aqi=result_data["aqi"],
                searched_at=datetime.now(timezone.utc)
            )
            db.add(new_aqi_history)
            db.commit()
        except Exception as e:
            print(f"Failed to save AQI history: {e}")
            db.rollback()
            
        return result_data

    return {"error": "City not found anywhere on earth!"}