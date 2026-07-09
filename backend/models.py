from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, timezone  # <--- timezone yahan import kiya

from backend.database import Base


# ====================================
# User Table
# ====================================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc)) # <-- FIX


# ====================================
# Weather History Table
# ====================================

class WeatherHistory(Base):
    __tablename__ = "weather_history"
    
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    temperature = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
    searched_at = Column(DateTime, default=lambda: datetime.now(timezone.utc)) # <-- FIX


class AQIHistory(Base):
    __tablename__ = "aqi_history"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    aqi = Column(Integer)
    searched_at = Column(DateTime, default=lambda: datetime.now(timezone.utc)) # <-- FIX


class WaterQuality(Base):
    __tablename__ = "water_quality"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    ph = Column(Float)
    dissolved_oxygen = Column(Float)
    quality_status = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc)) # <-- FIX


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    predicted_aqi = Column(Float)
    predicted_temperature = Column(Float)
    prediction_date = Column(DateTime, default=lambda: datetime.now(timezone.utc)) # <-- FIX


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    message = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc)) # <-- FIX


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    report_name = Column(String)
    report_type = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc)) # <-- FIX


class LoginLog(Base):
    __tablename__ = "login_logs"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    login_time = Column(DateTime, default=lambda: datetime.now(timezone.utc)) # <-- FIX