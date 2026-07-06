# backend/routes/satellite_routes.py
from fastapi import APIRouter, HTTPException
from backend.services.satellite_service import fetch_satellite_data

router = APIRouter(
    prefix="/satellite",
    tags=["Satellite Telemetry"]
)

@router.get("/data/{region}")
def get_satellite_dashboard_data(region: str):
    """
    BFF Endpoint: Fetches Live OpenWeather data and telemetry mapped for the frontend.
    """
    try:
        return fetch_satellite_data(region)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))