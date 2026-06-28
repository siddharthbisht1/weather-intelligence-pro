from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

# Import your new AI inference engine
from backend.ml.predict_model import predict_aqi

# Import your master utility helpers
from backend.utils.helpers import success_response, error_response, get_aqi_category

# ==========================================
# Router Setup
# ==========================================

router = APIRouter(
    prefix="/ai",
    tags=["AI Predictions"]
)

# ==========================================
# Pydantic Schema (Input Validation)
# ==========================================

class PredictionRequest(BaseModel):
    temperature: float = Field(..., description="Current temperature in Celsius")
    humidity: float = Field(..., description="Current humidity percentage")
    wind_speed: float = Field(..., description="Current wind speed in m/s")


# ==========================================
# AI Prediction Endpoint
# ==========================================

@router.post("/predict")
def generate_prediction(data: PredictionRequest):
    """
    Feeds environmental data into the Random Forest model to predict future AQI.
    """
    try:
        # 1. Run the live AI prediction using the exact inputs
        predicted_aqi = predict_aqi(
            temperature=data.temperature,
            humidity=data.humidity,
            wind_speed=data.wind_speed
        )

        # 2. Get the human-readable category for the dashboard
        category = get_aqi_category(int(predicted_aqi))

        # 3. Format the final output payload
        result = {
            "predicted_aqi": predicted_aqi,
            "health_category": category,
            "inputs": {
                "temperature": data.temperature,
                "humidity": data.humidity,
                "wind_speed": data.wind_speed
            }
        }

        # 4. Return using your standardized success formatter
        return success_response("AI Prediction generated successfully", result)

    except FileNotFoundError as e:
        # This catches the error if you haven't run train_model.py yet!
        raise HTTPException(status_code=500, detail=str(e))
        
    except Exception as e:
        return error_response(f"Prediction failed: {str(e)}")