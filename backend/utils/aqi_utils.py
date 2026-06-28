# ==========================================
# AQI Status Categorization
# ==========================================

def aqi_category(aqi: float) -> str:
    """
    Categorizes the Air Quality Index (AQI) into standard human-readable labels.
    """
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Poor"
    elif aqi <= 300:
        return "Very Poor"
    
    return "Hazardous"