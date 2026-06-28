from fastapi import APIRouter, HTTPException

from backend.services.aqi_service import get_aqi

router = APIRouter(
    prefix="/aqi",
    tags=["AQI"]
)


# ==========================================
# Get AQI Data
# ==========================================

@router.get("/{city}")
def fetch_aqi(city: str):
    aqi_data = get_aqi(city)

    if "error" in aqi_data:
        raise HTTPException(
            status_code=404,
            detail=aqi_data["error"]
        )

    return aqi_data