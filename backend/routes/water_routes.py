# File: backend/routes/water_routes.py
from fastapi import APIRouter, HTTPException
from backend.services.water_service import fetch_water_quality_data

router = APIRouter(
    prefix="/water",
    tags=["Water Quality"]
)

@router.get("/data/{city}")
def get_water_dashboard_data(city: str):
    """
    BFF Endpoint to fetch localized water quality metrics and map coordinates.
    """
    try:
        return fetch_water_quality_data(city)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))