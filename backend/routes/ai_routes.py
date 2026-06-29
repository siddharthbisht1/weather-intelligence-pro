from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.services.ai_service import (
    predict_weather, predict_aqi, pollution_trend, 
    heatwave_risk, rainfall_prediction, generate_ai_insights,
    get_ai_chat_response 
)
from backend.database import get_db
from backend.schemas import ChatRequest

router = APIRouter(prefix="/ai", tags=["AI Forecasts"])

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Frontend se user ka message leta hai aur AI response return karta hai.
    """
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
# backend/routes/aqi_routes.py ke andar add karo

@router.get("/history/{city}")
def get_aqi_history(city: str, db: Session = Depends(get_db)):
    """Chart ke liye pichle 7 records fetch karne ka API"""
    try:
        # Database se us city ke last 7 records nikalo
        history = db.query(AQIHistory)\
                    .filter(AQIHistory.city == city.capitalize())\
                    .order_by(AQIHistory.id.desc())\
                    .limit(7)\
                    .all()
        
        # Agar data nahi hai, toh error mat do, khali list bhej do
        if not history:
            return {"success": True, "data": []}
            
        # Data ko JSON format mein pack karo
        return {"success": True, "data": history}
        
    except Exception as e:
        print(f"History Fetch Error: {e}")
        raise HTTPException(status_code=500, detail="Database se data lane mein error")