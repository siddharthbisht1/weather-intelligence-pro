from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.database import get_db
from backend.services.aqi_service import get_aqi_service
from backend.models import AQIHistory, User
# Current user nikalne ke liye import
from backend.dependencies.current_user import get_current_user 

router = APIRouter(
    prefix="/aqi",
    tags=["AQI"]
)


# ==========================================
# Get AQI Data
# ==========================================

@router.get("/{city}")
def fetch_aqi(
    city: str, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) # Yahan user ko identify kiya
):
    user_id = current_user.id if hasattr(current_user, "id") else 1
    aqi_data = get_aqi_service(city=city, db=db, user_id=user_id)
    if "error" in aqi_data:
        raise HTTPException(
            status_code=404,
            detail=aqi_data["error"]
        )

    return aqi_data


@router.get("/history/{city}")
def get_aqi_history(
    city: str, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) 
):
    
    user_id = current_user.id if hasattr(current_user, "id") else 1
    history = db.query(AQIHistory)\
                .filter(func.lower(AQIHistory.city) == city.lower())\
                .filter(AQIHistory.user_id == user_id)\
                .order_by(AQIHistory.searched_at.desc())\
                .limit(7)\
                .all()
    
    return {"success": True, "data": history}