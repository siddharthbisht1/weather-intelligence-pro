from fastapi import APIRouter, HTTPException
from backend.services.prediction_service import generate_ai_prediction

# ==========================================
# Router Setup
# ==========================================

router = APIRouter(
    prefix="/ai",
    tags=["AI Predictions"]
)

# ==========================================
# Unified AI Prediction Endpoint
# ==========================================

@router.get("/forecast/{city}")
def get_dashboard_prediction(city: str):
    """
    BFF Endpoint: Runs Scikit-Learn Model + Gemini LLM and formats it for the frontend.
    """
    try:
        return generate_ai_prediction(city)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))