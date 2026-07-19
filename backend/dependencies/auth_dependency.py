from fastapi import APIRouter, Depends
# Import your new helper
from backend.dependencies.auth_helper import require_auth 

router = APIRouter()

@router.get("/my-weather-data")
def get_weather(username: str = Depends(require_auth)):
    return {"message": f"Hello {username}, here is your secure weather data!"}