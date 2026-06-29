from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.services.aqi_service import get_aqi_service
from sqlalchemy import func
from backend.models import AQIHistory 

router = APIRouter(
    prefix="/aqi",
    tags=["AQI"]
)


# ==========================================
# Get AQI Data
# ==========================================

@router.get("/{city}")
def fetch_aqi(city: str):
    aqi_data = get_aqi_service(city)

    if "error" in aqi_data:
        raise HTTPException(
            status_code=404,
            detail=aqi_data["error"]
        )

    return aqi_data
@router.get("/history/{city}")
def get_aqi_history(city: str, db: Session = Depends(get_db)):
    # Case-insensitive search (saari city ko lowercase mein compare karo)
    history = db.query(AQIHistory)\
                .filter(func.lower(AQIHistory.city) == city.lower())\
                .order_by(AQIHistory.searched_at.desc())\
                .limit(7)\
                .all()
    
    return {"success": True, "data": history}
 