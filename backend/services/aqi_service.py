import os
import requests

# ==========================================
# OpenWeather API Key
# ==========================================

# Pulls the API key from your environment (.env file)
API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_OPENWEATHER_API_KEY")


# ==========================================
# Get Coordinates of City
# ==========================================

def get_coordinates(city: str):
    geo_url = (
        f"http://api.openweathermap.org/geo/1.0/direct"
        f"?q={city}"
        f"&limit=1"
        f"&appid={API_KEY}"
    )

    response = requests.get(geo_url)
    data = response.json()

    if not data:
        return None

    return {
        "lat": data[0]["lat"],
        "lon": data[0]["lon"]
    }


# ==========================================
# Get AQI Data
# ==========================================

def get_aqi(city: str):
    coords = get_coordinates(city)

    if coords is None:
        return {
            "error": "City not found"
        }

    lat = coords["lat"]
    lon = coords["lon"]

    aqi_url = (
        f"http://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}"
        f"&lon={lon}"
        f"&appid={API_KEY}"
    )

    response = requests.get(aqi_url)

    if response.status_code != 200:
        return {
            "error": "AQI data unavailable"
        }

    data = response.json()
    pollution = data["list"][0]

    return {
        "aqi": pollution["main"]["aqi"],
        "pm2_5": pollution["components"]["pm2_5"],
        "pm10": pollution["components"]["pm10"],
        "co": pollution["components"]["co"],
        "no2": pollution["components"]["no2"],
        "so2": pollution["components"]["so2"]
    }