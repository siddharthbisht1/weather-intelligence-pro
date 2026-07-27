from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.services.weather_service import get_and_save_weather
from backend.schemas import WeatherResponse
from backend.dependencies import get_db
# 1. Current user aur Model ka import add kiya
from backend.dependencies.current_user import get_current_user
from backend.models import WeatherHistory, User

router = APIRouter(
    prefix="/weather",
    tags=["Weather Management"]
)

@router.post("/fetch", response_model=WeatherResponse, status_code=201)
def fetch_weather_data(
    city: str, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # 2. API hit karne wale user ko identify karega
):
    """
    OpenWeather API se live data fetch karega, 
    use SQLite DB mein save karega, aur response return karega.
    """
    # 3. Service mein current_user.id pass kar diya
    result = get_and_save_weather(city=city, db=db, user_id=current_user.id)
    
    if isinstance(result, dict) and "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=result["error"]
        )
        
    return result

@router.get("/history")
def get_weather_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) # 4. History bhi user-specific kardi
):
    # 5. DB se sirf usi user ka purana data fetch karo
    history = db.query(WeatherHistory)\
                .filter(WeatherHistory.user_id == current_user.id)\
                .order_by(WeatherHistory.searched_at.desc())\
                .all()
    return history