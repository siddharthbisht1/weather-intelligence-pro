import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "Weather Intelligence Pro"
VERSION = "1.0.0"
DEBUG = os.getenv("DEBUG", "True") == "True"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database/users.db")

SECRET_KEY = os.getenv("SECRET_KEY", "weather_intelligence_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_OPENWEATHER_API_KEY")
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
AIR_POLLUTION_BASE_URL = "https://api.openweathermap.org/data/2.5/air_pollution"
GEO_BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"


EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME", "")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")


class Settings:
    APP_NAME: str = APP_NAME
    VERSION: str = VERSION
    DEBUG: bool = DEBUG
    DATABASE_URL: str = DATABASE_URL
    SECRET_KEY: str = SECRET_KEY
    ALGORITHM: str = ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 240
    OPENWEATHER_API_KEY: str = OPENWEATHER_API_KEY
    EMAIL_USERNAME: str = EMAIL_USERNAME
    EMAIL_PASSWORD: str = EMAIL_PASSWORD
    ALLOWED_ORIGINS: list = ["*"]

settings = Settings()

APP_NAME = settings.APP_NAME
VERSION = settings.VERSION
DEBUG = settings.DEBUG
ALLOWED_ORIGINS = settings.ALLOWED_ORIGINS