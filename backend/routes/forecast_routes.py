from fastapi import APIRouter, HTTPException
from backend.services.forecast_service import get_forecast

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"]
)

# ==========================================
# Get 5-Day Forecast
# ==========================================

@router.get("/{city}")
def fetch_forecast(city: str):
    forecast_data = get_forecast(city)

    if "error" in forecast_data:
        raise HTTPException(
            status_code=404,
            detail=forecast_data["error"]
        )

    return forecast_data