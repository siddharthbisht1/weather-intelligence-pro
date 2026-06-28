import os
import pandas as pd
from sqlalchemy.orm import Session

from models import (
    User,
    WeatherHistory,
    AQIHistory,
    Prediction,
    LoginLog
)

os.makedirs("exports", exist_ok=True)

def export_users(db: Session):
    users = db.query(User).all()
    data = []

    for user in users:
        data.append({
            "ID": user.id,
            "Username": user.username,
            "Email": user.email,
            "Role": user.role,
            "Created At": user.created_at
        })

    df = pd.DataFrame(data)
    df.to_excel("exports/users.xlsx", index=False)

    return "Users exported successfully"


def export_weather_history(db: Session):
    weather = db.query(WeatherHistory).all()
    data = []

    for record in weather:
        data.append({
            "City": record.city,
            "Temperature": record.temperature,
            "Humidity": record.humidity,
            "Wind Speed": record.wind_speed,
            "Searched At": record.searched_at
        })

    df = pd.DataFrame(data)
    df.to_excel("exports/weather_history.xlsx", index=False)

    return "Weather history exported"


def export_aqi_history(db: Session):
    records = db.query(AQIHistory).all()
    data = []

    for record in records:
        data.append({
            "City": record.city,
            "AQI": record.aqi,
            "Searched At": record.searched_at
        })

    df = pd.DataFrame(data)
    df.to_excel("exports/aqi_history.xlsx", index=False)

    return "AQI history exported"

def export_predictions(db: Session):
    predictions = db.query(Prediction).all()
    data = []

    for record in predictions:
        data.append({
            "City": record.city,
            "Predicted AQI": record.predicted_aqi,
            "Predicted Temperature": record.predicted_temperature,
            "Prediction Date": record.prediction_date
        })

    df = pd.DataFrame(data)
    df.to_excel("exports/predictions.xlsx", index=False)

    return "Predictions exported"



def export_login_logs(db: Session):
    logs = db.query(LoginLog).all()
    data = []

    for log in logs:
        data.append({
            "Username": log.username,
            "Login Time": log.login_time
        })

    df = pd.DataFrame(data)
    df.to_excel("exports/login_logs.xlsx", index=False)

    return "Login logs exported"