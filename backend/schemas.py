from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

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

    model_config = ConfigDict(from_attributes=True)

class WeatherBase(BaseModel):
    city: str
    temperature: float
    humidity: float
    wind_speed: float

class WeatherCreate(WeatherBase):
    pass  

class WeatherResponse(WeatherBase):
    id: int
    searched_at: datetime  

    model_config = ConfigDict(from_attributes=True)

class AQIBase(BaseModel):
    city: str
    aqi: int
    pm25: Optional[float] = None  
    pm10: Optional[float] = None

class AQICreate(AQIBase):
    pass

class AQIResponse(AQIBase):
    id: int
    recorded_at: datetime

    model_config = ConfigDict(from_attributes=True)

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

    model_config = ConfigDict(from_attributes=True)

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

    model_config = ConfigDict(from_attributes=True)

class NotificationBase(BaseModel):
    title: str
    message: str

class NotificationCreate(NotificationBase):
    user_id: Optional[int] = None  

class NotificationResponse(NotificationBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReportBase(BaseModel):
    report_name: str
    report_type: str  

class ReportCreate(ReportBase):
    generated_by: int  

class ReportResponse(ReportBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LoginLogResponse(BaseModel):
    id: int
    username: str
    login_time: datetime
    ip_address: Optional[str] = None  

    model_config = ConfigDict(from_attributes=True)

class ChatRequest(BaseModel):
    user_message: str

class ChatResponse(BaseModel):
    reply: str