import os
from datetime import datetime
import pandas as pd

# ==========================================
# File Configuration
# ==========================================

LOG_FILE = "exports/system_logs.xlsx"

COLUMNS = [
    "Timestamp",
    "Username",
    "Module",
    "Action",
    "Details"
]


# ==========================================
# Initialize Excel File
# ==========================================

def initialize_excel():
    # SAFETY CHECK: Ensure the 'exports' folder exists before saving!
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    if not os.path.exists(LOG_FILE):
        df = pd.DataFrame(columns=COLUMNS)
        df.to_excel(LOG_FILE, index=False)


# ==========================================
# Log Entry
# ==========================================

def log_to_excel(username: str, module: str, action: str, details: str = ""):
    initialize_excel()

    try:
        df = pd.read_excel(LOG_FILE)
    except:
        df = pd.DataFrame(columns=COLUMNS)

    new_entry = {
        "Timestamp": datetime.now(),
        "Username": username,
        "Module": module,
        "Action": action,
        "Details": details
    }

    df = pd.concat(
        [df, pd.DataFrame([new_entry])],
        ignore_index=True
    )

    df.to_excel(LOG_FILE, index=False)

    return {
        "message": "Log saved successfully"
    }


# ==========================================
# Weather Search Logger
# ==========================================

def log_weather_search(username, city):
    return log_to_excel(
        username=username,
        module="Weather",
        action="Search",
        details=f"City: {city}"
    )


# ==========================================
# AQI Search Logger
# ==========================================

def log_aqi_search(username, city):
    return log_to_excel(
        username=username,
        module="AQI",
        action="Search",
        details=f"City: {city}"
    )


# ==========================================
# Water Quality Logger
# ==========================================

def log_water_quality(username, city):
    return log_to_excel(
        username=username,
        module="Water",
        action="Search",
        details=f"City: {city}"
    )


# ==========================================
# AI Prediction Logger
# ==========================================

def log_prediction(username, city):
    return log_to_excel(
        username=username,
        module="AI",
        action="Prediction",
        details=f"City: {city}"
    )


# ==========================================
# Login Logger
# ==========================================

def log_login(username):
    return log_to_excel(
        username=username,
        module="Authentication",
        action="Login"
    )


# ==========================================
# Error Logger
# ==========================================

def log_error(error_message):
    return log_to_excel(
        username="System",
        module="Error",
        action="Exception",
        details=error_message
    )