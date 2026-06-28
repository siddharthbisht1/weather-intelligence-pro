import requests
from backend.config import OPENWEATHER_API_KEY

# ==========================================
# Forecast URL
# ==========================================

FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


# ==========================================
# Get 5-Day Forecast
# ==========================================

def get_forecast(city: str):
    try:
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }

        response = requests.get(FORECAST_URL, params=params)

        if response.status_code != 200:
            return {
                "error": "Unable to fetch forecast"
            }

        data = response.json()
        forecast_list = []

        for item in data["list"]:
            forecast_list.append({
                "datetime": item["dt_txt"],
                "temperature": item["main"]["temp"],
                "feels_like": item["main"]["feels_like"],
                "humidity": item["main"]["humidity"],
                "pressure": item["main"]["pressure"],
                "wind_speed": item["wind"]["speed"],
                "description": item["weather"][0]["description"],
                "icon": item["weather"][0]["icon"]
            })

        return {
            "city": data["city"]["name"],
            "country": data["city"]["country"],
            "forecast": forecast_list
        }

    except Exception as e:
        return {
            "error": str(e)
        }