import random
import string
from datetime import datetime

# ==========================================
# Generate Random ID
# ==========================================

def generate_id(length: int = 8) -> str:
    """Generates a random uppercase alphanumeric string."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


# ==========================================
# Current Timestamp
# ==========================================

def get_current_time() -> datetime:
    """Returns the current system datetime."""
    return datetime.now()


# ==========================================
# Format DateTime
# ==========================================

def format_datetime(dt: datetime) -> str:
    """Formats a datetime object to YYYY-MM-DD HH:MM:SS."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# ==========================================
# Temperature Converter
# ==========================================

def celsius_to_fahrenheit(temperature: float) -> float:
    """Converts Celsius to Fahrenheit, rounded to 2 decimal places."""
    return round((temperature * 9 / 5) + 32, 2)


# ==========================================
# Percentage Calculator
# ==========================================

def calculate_percentage(value: float, total: float) -> float:
    """Calculates percentage safely, avoiding division by zero."""
    if total == 0:
        return 0.0
    return round((value / total) * 100, 2)


# ==========================================
# AQI Category
# ==========================================

def get_aqi_category(aqi: int) -> str:
    """Returns a human-readable category for a given AQI."""
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Poor"
    elif aqi <= 300:
        return "Very Poor"
    return "Hazardous"


# ==========================================
# Temperature Status
# ==========================================

def get_temperature_status(temp: float) -> str:
    """Returns a human-readable status for a given temperature (Celsius)."""
    if temp >= 40:
        return "Extreme Heat"
    elif temp >= 30:
        return "Hot"
    elif temp >= 20:
        return "Pleasant"
    else:
        return "Cold"


# ==========================================
# Success Response
# ==========================================

def success_response(message: str, data=None) -> dict:
    """Standardizes successful API JSON responses."""
    return {
        "success": True,
        "message": message,
        "data": data
    }


# ==========================================
# Error Response
# ==========================================

def error_response(message: str) -> dict:
    """Standardizes error API JSON responses."""
    return {
        "success": False,
        "message": message
    }