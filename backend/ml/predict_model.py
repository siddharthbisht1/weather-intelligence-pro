import os
import joblib
import numpy as np

# ==========================================
# Configuration & Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "aqi_forecast.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

# Keep the model and scaler in memory for fast API responses
_model = None
_scaler = None

# ==========================================
# Load AI Artifacts
# ==========================================

def load_artifacts():
    """
    Lazily loads the trained model and scaler into memory.
    """
    global _model, _scaler
    
    if _model is None or _scaler is None:
        if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
            raise FileNotFoundError(
                "AI artifacts missing! Please run 'train_model.py' to generate the .pkl files."
            )
            
        print("🧠 Loading Machine Learning models into memory...")
        _model = joblib.load(MODEL_PATH)
        _scaler = joblib.load(SCALER_PATH)


# ==========================================
# Live AI Prediction
# ==========================================

def predict_aqi(temperature: float, humidity: float, wind_speed: float) -> float:
    """
    Predicts the future Air Quality Index (AQI) based on environmental data.
    """
    # Ensure the model is loaded
    load_artifacts()
    
    # Format the input data to match the training shape: [temp, humidity, wind]
    input_data = np.array([[temperature, humidity, wind_speed]])
    
    # Scale the input using the exact same mathematical rules from training
    scaled_data = _scaler.transform(input_data)
    
    # Generate the prediction
    prediction = _model.predict(scaled_data)
    
    # Return the predicted AQI rounded to 2 decimal places
    return round(float(prediction[0]), 2)