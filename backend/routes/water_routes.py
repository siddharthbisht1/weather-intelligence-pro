from fastapi import APIRouter, HTTPException

from backend.services.water_service import get_water_quality

router = APIRouter(
    prefix="/water",
    tags=["Water Quality"]
)


# ==========================================
# Get Water Quality Data
# ==========================================

@router.get("/{city}")
def fetch_water_quality(city: str):
    water_data = get_water_quality(city)

    if "error" in water_data:
        raise HTTPException(
            status_code=404,
            detail=water_data["error"]
        )

    return water_data