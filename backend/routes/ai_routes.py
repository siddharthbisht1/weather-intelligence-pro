from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.ai_service import (
    predict_weather, predict_aqi, pollution_trend, 
    heatwave_risk, rainfall_prediction, generate_ai_insights,
    get_ai_chat_response 
)

router = APIRouter(prefix="/ai", tags=["AI Forecasts"])

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
async def ai_chat_assistant(request: ChatRequest):
    ai_reply = get_ai_chat_response(request.query)
    return {"response": ai_reply}

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