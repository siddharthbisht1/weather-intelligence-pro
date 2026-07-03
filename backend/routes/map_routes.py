# backend/routes/map_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.dependencies import get_db
from backend.services.map_service import fetch_map_data

router = APIRouter(
    prefix="/maps",
    tags=["Environmental Maps"]
)

@router.get("/data/{city}")
def get_city_map_data(city: str, db: Session = Depends(get_db)):
    """
    BFF Endpoint to fetch geospatial analytics for the Maps Dashboard.
    """
    # db session is injected here for future use when you map this to real db tables
    data = fetch_map_data(city)
    return data