import random
import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.schemas import ChatRequest
from backend.services.ai_service import (
    predict_weather, predict_aqi, pollution_trend, 
    heatwave_risk, rainfall_prediction, generate_ai_insights,
    get_ai_chat_response 
)

# 👇 Naya Import Service se
from backend.services.aqi_service import get_aqi_history_from_db

router = APIRouter(prefix="/ai", tags=["AI Forecasts"])

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """Frontend se user ka message leta hai aur AI response return karta hai."""
    try:
        user_query = request.user_message
        ai_reply = get_ai_chat_response(user_query)
        return {"reply": ai_reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Service Error: {str(e)}")

@router.get("/weather/{city}")
def ai_weather_prediction(city: str):
    return predict_weather(city)

@router.get("/aqi/{city}")
def ai_aqi_prediction(city: str):
    return predict_aqi(city)

@router.get("/pollution-trend")
def get_pollution_trend():
    return pollution_trend()

@router.get("/heatwave-risk")
def get_heatwave_risk():
    return heatwave_risk()

@router.get("/rainfall")
def get_rainfall_prediction():
    return rainfall_prediction()

@router.get("/insights/{city}")
def ai_insights(city: str):
    return generate_ai_insights(city)

# ==========================================
# 🛠️ FIXED: Database logic moved to service
# ==========================================
@router.get("/history/{city}")
def get_aqi_history(city: str, db: Session = Depends(get_db)):
    """Chart ke liye pichle 7 records fetch karne ka API"""
    return get_aqi_history_from_db(city, db)

# ==========================================
# Mock Data Routes
# ==========================================
@router.get("/eco-insights/{city}")
def get_eco_insights(city: str):
    return {
        "city": city.capitalize(),
        "kpi": {
            "health_score": random.randint(70, 98),
            "comfort_index": random.randint(15, 38),
            "aqi": random.randint(40, 250),
            "water_safety": random.randint(80, 99)
        },
        "charts": {
            "wellness": [random.randint(60, 95) for _ in range(7)],
            "eco_score": [random.randint(50, 100) for _ in range(5)]
        },
        "focus": {
            "activity": random.randint(50, 100),
            "hydration": round(random.uniform(1.5, 4.0), 1),
            "sleep": random.randint(6, 9)
        }
    }

@router.get("/emergency-alerts/{city}")
def get_emergency_alerts(city: str):
    city_data = {
        "mumbai": [19.0760, 72.8777], "delhi": [28.7041, 77.1025],
        "haldwani": [29.2183, 79.5130], "dehradun": [30.3165, 78.0322],
        "bengaluru": [12.9716, 77.5946], "chennai": [13.0827, 80.2707],
        "kolkata": [22.5726, 88.3639], "pune": [18.5204, 73.8567],
        "hyderabad": [17.3850, 78.4867]
    }
    
    city_lower = city.lower()
    if city_lower in city_data:
        base_lat, base_lng = city_data[city_lower]
    else:
        base_lat = random.uniform(20.0, 28.0)
        base_lng = random.uniform(72.0, 80.0)
    
    return {
        "city": city.capitalize(),
        "coords": [base_lat, base_lng],
        "kpi": {
            "active_alerts": random.randint(5, 15),
            "heatwave": random.randint(1, 5),
            "flood": random.randint(1, 4),
            "aqi": random.randint(2, 6)
        },
        "alerts_table": [
            {"location": city.capitalize(), "type": "Severe Heatwave", "severity": "Critical", "badge_class": "badge-red"},
            {"location": f"{city.capitalize()} Outskirts", "type": "Waterlogging Risk", "severity": "Severe", "badge_class": "badge-orange"},
            {"location": "Nearby Region", "type": "High AQI", "severity": "Moderate", "badge_class": "badge-yellow"}
        ],
        "charts": {
            "earthquake": [round(random.uniform(1.0, 5.0), 1) for _ in range(6)],
            "flood": [random.randint(100, 250) for _ in range(6)],
            "heatwave": [random.randint(30, 48) for _ in range(6)],
            "risk": [random.randint(10, 40), random.randint(10, 30), random.randint(20, 50), random.randint(10, 20)]
        },
        "map_markers": [
            {"lat": base_lat + random.uniform(-0.05, 0.05), "lng": base_lng + random.uniform(-0.05, 0.05), "desc": "Heatwave Spike", "color": "#FB923C"},
            {"lat": base_lat + random.uniform(-0.05, 0.05), "lng": base_lng + random.uniform(-0.05, 0.05), "desc": "Flood Risk Zone", "color": "#38BDF8"},
            {"lat": base_lat + random.uniform(-0.05, 0.05), "lng": base_lng + random.uniform(-0.05, 0.05), "desc": "Hazardous AQI", "color": "#A855F7"}
        ],
        "summary": f"Current monitoring for {city.capitalize()} indicates active environmental alerts. High temperature spikes and localized waterlogging risks are present.",
        "timeline": [
            {"time": "10 mins ago", "text": f"Alert issued for {city.capitalize()}", "color": "#FB923C", "icon": "fa-fire"},
            {"time": "1 hour ago", "text": "Flood Warning upgraded", "color": "#38BDF8", "icon": "fa-cloud-showers-heavy"},
            {"time": "3 hours ago", "text": "AQI Spike detected", "color": "#A855F7", "icon": "fa-smog"}
        ]
    }

@router.get("/export-data/{city}")
def get_export_data(city: str):
    date_today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    return {
        "city": city.capitalize(),
        "date": date_today,
        "kpi": {
            "health_score": random.randint(75, 98),
            "aqi": random.randint(40, 200),
            "temperature": random.randint(15, 45),
            "humidity": random.randint(30, 90)
        },
        "forecast": [
            {"day": "Mon", "rain_prob": random.randint(0, 100)},
            {"day": "Tue", "rain_prob": random.randint(0, 100)},
            {"day": "Wed", "rain_prob": random.randint(0, 100)}
        ]
    }

@router.get("/forecast/{city}")
def get_forecast_data(city: str):
    city_data = {
        "mumbai": [19.0760, 72.8777], "delhi": [28.7041, 77.1025], 
        "haldwani": [29.2183, 79.5130], "dehradun": [30.3165, 78.0322],
        "bengaluru": [12.9716, 77.5946]
    }
    
    city_lower = city.lower()
    base_lat, base_lng = city_data.get(city_lower, [random.uniform(20.0, 30.0), random.uniform(72.0, 85.0)])
    
    conditions = ["Sunny", "Cloudy", "Rain", "Thunderstorm", "Partly Cloudy"]
    current_condition = random.choice(conditions)
    current_temp = random.randint(15, 40)

    return {
        "city": city.capitalize(),
        "coords": [base_lat, base_lng],
        "current": {
            "temp": current_temp,
            "condition": current_condition
        },
        "details": {
            "sunrise": "05:45 AM", "sunset": "06:50 PM",
            "uv": f"{random.randint(4, 10)} (Moderate)",
            "pressure": f"{random.randint(1005, 1025)} hPa",
            "humidity": f"{random.randint(40, 90)}%",
            "wind": f"{random.randint(5, 25)} km/h",
            "visibility": f"{random.randint(5, 10)} km",
            "feels_like": f"{current_temp + random.randint(-2, 3)}°C",
            "dew_point": f"{current_temp - random.randint(5, 10)}°C",
            "moon_phase": random.choice(["Waxing", "Waning", "Full Moon", "New Moon"])
        },
        "hourly": [
            {"time": "Now", "temp": current_temp, "condition": current_condition, "rain": random.randint(0, 100)},
            {"time": "1 PM", "temp": current_temp + 1, "condition": random.choice(conditions), "rain": random.randint(0, 100)},
            {"time": "2 PM", "temp": current_temp + 2, "condition": random.choice(conditions), "rain": random.randint(0, 100)},
            {"time": "3 PM", "temp": current_temp + 1, "condition": random.choice(conditions), "rain": random.randint(0, 100)},
            {"time": "4 PM", "temp": current_temp, "condition": random.choice(conditions), "rain": random.randint(0, 100)},
            {"time": "5 PM", "temp": current_temp - 1, "condition": random.choice(conditions), "rain": random.randint(0, 100)}
        ],
        "tenday": [
            {"day": "Today", "condition": current_condition, "high": current_temp + 2, "low": current_temp - 4},
            {"day": "Tomorrow", "condition": random.choice(conditions), "high": current_temp + 3, "low": current_temp - 3},
            {"day": "Wednesday", "condition": random.choice(conditions), "high": current_temp + 1, "low": current_temp - 5},
            {"day": "Thursday", "condition": random.choice(conditions), "high": current_temp + 4, "low": current_temp - 2},
            {"day": "Friday", "condition": random.choice(conditions), "high": current_temp + 2, "low": current_temp - 3}
        ],
        "alerts": [
            "🌬 Strong winds expected in the evening",
            "⚡ Thunderstorm warning for outskirts",
            "☀️ High UV Index at noon, wear sunscreen"
        ][:random.randint(1, 3)],
        "charts": {
            "temp": [current_temp, current_temp+2, current_temp+3, current_temp+1, current_temp-1, current_temp-3],
            "rain": [random.randint(0,100) for _ in range(6)],
            "wind": [random.randint(5,30) for _ in range(6)],
            "humidity": [random.randint(40,90) for _ in range(6)]
        }
    }

@router.post("/help/query")
def get_help_response(query: dict):
    user_query = query.get("text", "").lower()
    
    responses = {
        "search": "City search karne ke liye Dashboard pe jaao aur top search bar mein naam type karo.",
        "export": "Export karne ke liye Export Center mein jaao, wahan PDF/Excel buttons par click karo.",
        "login": "Agar login mein problem hai, toh credentials check karo ya 'Forgot Password' use karo.",
        "default": "Humein feedback form ke zariye batao, hamari support team 24 ghante mein contact karegi!"
    }
    
    answer = responses.get("default")
    for key in responses:
        if key in user_query:
            answer = responses[key]
            break
            
    return {"response": answer}