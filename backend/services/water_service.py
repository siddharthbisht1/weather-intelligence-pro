# backend/services/water_service.py
import os
import requests
import random
from dotenv import load_dotenv

load_dotenv()
OWM_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def fetch_water_quality_data(city: str):
    """
    Uses OpenWeather for real coordinates & weather context, 
    and generates realistic water quality metrics based on that context.
    """
    city_name = city.capitalize() if city else "Dehradun"
    
    # Defaults
    lat, lon = 30.3165, 78.0322 
    weather_condition = "Clear"

    # 1. Real API Call for Location & Context
    if OWM_API_KEY:
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OWM_API_KEY}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                lat = data['coord']['lat']
                lon = data['coord']['lon']
                weather_condition = data['weather'][0]['main'] # e.g., "Rain", "Clear", "Clouds"
        except Exception as e:
            print(f"OpenWeather API Error: {e}")

    # 2. Context-Aware Water Quality Simulation
    # If it's raining, water gets muddy (High Turbidity, lower WQI)
    if weather_condition in ["Rain", "Thunderstorm", "Drizzle"]:
        wqi = random.randint(70, 82)
        ph = round(random.uniform(6.5, 6.9), 1)
        tds = random.randint(250, 400)
        turbidity = round(random.uniform(3.5, 6.0), 1) # High
        status = "Requires Treatment (Monsoon Runoff)"
        color = "#FACC15" # Yellow/Warning
    else:
        wqi = random.randint(88, 96)
        ph = round(random.uniform(7.1, 7.5), 1)
        tds = random.randint(150, 250)
        turbidity = round(random.uniform(0.5, 2.0), 1) # Clear
        status = "Safe for Consumption"
        color = "#4ADE80" # Green/Safe

    # Trend for the line chart (Last 5 days)
    wqi_trend = [wqi + random.randint(-4, 4) for _ in range(4)] + [wqi]

    return {
        "city": city_name,
        "map_center": {"lat": lat, "lng": lon},
        "kpis": {
            "wqi": wqi,
            "ph": ph,
            "tds": tds,
            "turbidity": turbidity,
            "status": status,
            "status_color": color
        },
        "charts": {
            "wqi_trend": wqi_trend,
            # Scaling TDS down for the bar chart so it fits with pH and Turbidity visually
            "parameters": [ph, tds/100, turbidity, round(random.uniform(0.5, 1.5), 1)] 
        }
    }