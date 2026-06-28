# ==========================================
# Predicted Risk Level Categorization
# ==========================================

def risk_level(predicted_aqi: float) -> str:
    """
    Determines the health risk level based on the predicted AQI.
    """
    if predicted_aqi <= 100:
        return "Low"
    elif predicted_aqi <= 200:
        return "Moderate"
    
    return "High"