import os
from datetime import datetime
import pandas as pd

EXCEL_FILE = "exports/activity_tracker.xlsx"

# ==========================================
# Create Excel File If Not Exists
# ==========================================

def initialize_excel():
    # SAFETY CHECK: Ensure the 'exports' folder exists before saving!
    os.makedirs(os.path.dirname(EXCEL_FILE), exist_ok=True)

    if not os.path.exists(EXCEL_FILE):
        with pd.ExcelWriter(
            EXCEL_FILE,
            engine="openpyxl"
        ) as writer:
            pd.DataFrame(
                columns=[
                    "Timestamp",
                    "Username",
                    "Activity",
                    "City",
                    "Details"
                ]
            ).to_excel(
                writer,
                sheet_name="Activity Logs",
                index=False
            )


# ==========================================
# Add Activity
# ==========================================

def log_activity(username, activity, city="", details=""):
    initialize_excel()

    try:
        df = pd.read_excel(
            EXCEL_FILE,
            sheet_name="Activity Logs"
        )
    except:
        df = pd.DataFrame(
            columns=[
                "Timestamp",
                "Username",
                "Activity",
                "City",
                "Details"
            ]
        )

    new_row = {
        "Timestamp": datetime.now(),
        "Username": username,
        "Activity": activity,
        "City": city,
        "Details": details
    }

    df = pd.concat(
        [
            df,
            pd.DataFrame([new_row])
        ],
        ignore_index=True
    )

    with pd.ExcelWriter(
        EXCEL_FILE,
        engine="openpyxl"
    ) as writer:
        df.to_excel(
            writer,
            sheet_name="Activity Logs",
            index=False
        )


# ==========================================
# Track Login
# ==========================================

def track_login(username):
    log_activity(
        username=username,
        activity="Login"
    )


# ==========================================
# Track Weather Search
# ==========================================

def track_weather_search(username, city):
    log_activity(
        username=username,
        activity="Weather Search",
        city=city
    )


# ==========================================
# Track AQI Search
# ==========================================

def track_aqi_search(username, city):
    log_activity(
        username=username,
        activity="AQI Search",
        city=city
    )


# ==========================================
# Track Prediction
# ==========================================

def track_prediction(username, city):
    log_activity(
        username=username,
        activity="AI Prediction",
        city=city
    )


# ==========================================
# Track Water Quality Search
# ==========================================

def track_water_quality(username, city):
    log_activity(
        username=username,
        activity="Water Quality",
        city=city
    )