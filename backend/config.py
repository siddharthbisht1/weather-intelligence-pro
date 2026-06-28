import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ==========================================
# Application Settings
# ==========================================
APP_NAME = "Weather Intelligence Pro"
VERSION = "1.0.0"
DEBUG = os.getenv("DEBUG", "True") == "True"

# ==========================================
# Database Configuration
# ==========================================
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database/users.db")

# ==========================================
# JWT Configuration
# ==========================================
SECRET_KEY = os.getenv("SECRET_KEY", "weather_intelligence_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

# ==========================================
# OpenWeather API Configuration
# ==========================================
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_OPENWEATHER_API_KEY")
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
AIR_POLLUTION_BASE_URL = "https://api.openweathermap.org/data/2.5/air_pollution"
GEO_BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"

# ==========================================
# Email Configuration (Added these to match .env)
# ==========================================
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME", "")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")

# ==========================================
# Settings Class (The Single Source of Truth)
# ==========================================
class Settings:
    APP_NAME: str = APP_NAME
    VERSION: str = VERSION
    DEBUG: bool = DEBUG
    DATABASE_URL: str = DATABASE_URL
    SECRET_KEY: str = SECRET_KEY
    ALGORITHM: str = ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES: int = ACCESS_TOKEN_EXPIRE_MINUTES
    OPENWEATHER_API_KEY: str = OPENWEATHER_API_KEY
    EMAIL_USERNAME: str = EMAIL_USERNAME
    EMAIL_PASSWORD: str = EMAIL_PASSWORD
    ALLOWED_ORIGINS: list = ["*"]

settings = Settings()
# Add these back if you want to keep importing them individually
APP_NAME = settings.APP_NAME
VERSION = settings.VERSION
DEBUG = settings.DEBUG
ALLOWED_ORIGINS = settings.ALLOWED_ORIGINS