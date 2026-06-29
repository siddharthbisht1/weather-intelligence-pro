from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# ====================================
# User Schemas
# ====================================
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = "user"
class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


# ====================================
# Weather Schemas
# ====================================
class WeatherBase(BaseModel):
    city: str
    temperature: float
    humidity: float
    wind_speed: float

class WeatherCreate(WeatherBase):
    pass  # Input ke time bas base fields chahiye

class WeatherResponse(WeatherBase):
    id: int
    searched_at: datetime  # Database se timestamp tracking ke liye

    class Config:
        from_attributes = True


# ====================================
# AQI Schemas
# ====================================
class AQIBase(BaseModel):
    city: str
    aqi: int
    pm25: Optional[float] = None  # Extra monitoring data ke liye
    pm10: Optional[float] = None

class AQICreate(AQIBase):
    pass

class AQIResponse(AQIBase):
    id: int
    recorded_at: datetime

    class Config:
        from_attributes = True


# ====================================
# Water Quality Schemas
# ====================================
class WaterBase(BaseModel):
    city: str
    ph: float
    dissolved_oxygen: float
    quality_status: str

class WaterCreate(WaterBase):
    pass

class WaterResponse(WaterBase):
    id: int
    recorded_at: datetime

    class Config:
        from_attributes = True


# ====================================
# Prediction Schemas
# ====================================
class PredictionBase(BaseModel):
    city: str
    predicted_aqi: float
    predicted_temperature: float
    prediction_date: datetime

class PredictionCreate(PredictionBase):
    pass

class PredictionResponse(PredictionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ====================================
# Notification Schemas
# ====================================
class NotificationBase(BaseModel):
    title: str
    message: str

class NotificationCreate(NotificationBase):
    user_id: Optional[int] = None  # Agar specific user ko bhejni ho, nahi toh broadcast

class NotificationResponse(NotificationBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ====================================
# Report Schemas
# ====================================
class ReportBase(BaseModel):
    report_name: str
    report_type: str  # e.g., 'PDF', 'CSV'

class ReportCreate(ReportBase):
    generated_by: int  # Admin ki ID tracking ke liye

class ReportResponse(ReportBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ====================================
# Login Log Schemas (Sirf Response/Read-only hota hai system ke liye)
# ====================================
class LoginLogResponse(BaseModel):
    id: int
    username: str
    login_time: datetime
    ip_address: Optional[str] = None  # Security auditing ke liye mast feature hai

    class Config:
        from_attributes = True
class ChatRequest(BaseModel):
    user_message: str

class ChatResponse(BaseModel):
    reply: str