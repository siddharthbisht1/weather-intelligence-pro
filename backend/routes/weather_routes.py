from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
# Yeh line check karo apne weather_routes.py mein:
from backend.services.weather_service import get_and_save_weather  # 'get_weather' ki jagah ye likho
from backend.schemas import WeatherResponse
from backend.dependencies import get_db # Ya jahan se bhi tera get_db aa raha hai
router = APIRouter(
    prefix="/weather",
    tags=["Weather Management"]
)

@router.post("/fetch", response_model=WeatherResponse, status_code=201)
def fetch_weather_data(city: str, db: Session = Depends(get_db)):
    """
    OpenWeather API se live data fetch karega, 
    use SQLite DB mein save karega, aur response return karega.
    """
    result = get_and_save_weather(city=city, db=db)
    
    # Agar service se error dictionary aayi hai (jaise city not found ya DB failure)
    if isinstance(result, dict) and "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=result["error"]
        )
        
    return result
@router.get("/history")
def get_weather_history(db: Session = Depends(get_db)):
    # DB se purana data fetch karo
    history = db.query(WeatherHistory).order_by(WeatherHistory.searched_at.desc()).all()
    return history
