from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from backend.config import settings  
from backend.database import Base, engine

from backend.middleware.logging_middleware import LoggingMiddleware
from backend.middleware.auth_middleware import AuthMiddleware
from backend.middleware.admin_middleware import AdminMiddleware
from backend.middleware.rate_limit import RateLimitMiddleware

from backend.exceptions.exception_handlers import unified_exception_handler
from backend.exceptions.custom_exceptions import (
    UserNotFoundException,
    InvalidCredentialsException,
    UnauthorizedException,
    WeatherNotFoundException,
    AQINotFoundException
)
from backend.routes import ai_routes
from backend.routes import (
    auth_routes, weather_routes, aqi_routes, water_routes,
    analytics_routes, report_routes, history_routes, 
    notification_routes, admin_routes, forecast_routes, websocket_routes,
    prediction_routes, map_routes, observability_routes, legal_routes,
    satellite_routes, workflow_routes   
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print(f"🚀 {settings.APP_NAME} v{settings.VERSION} is now ONLINE.")
    yield 

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
    description="Enterprise-Grade Weather Intelligence API",
    lifespan=lifespan
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    
    if "components" not in openapi_schema:
        openapi_schema["components"] = {}
        
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    
    openapi_schema["security"] = [{"BearerAuth": []}]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Exception Handlers
app.add_exception_handler(UserNotFoundException, unified_exception_handler)
app.add_exception_handler(InvalidCredentialsException, unified_exception_handler)
app.add_exception_handler(UnauthorizedException, unified_exception_handler)
app.add_exception_handler(WeatherNotFoundException, unified_exception_handler)
app.add_exception_handler(AQINotFoundException, unified_exception_handler)

# Custom Middlewares
app.add_middleware(AdminMiddleware)
app.add_middleware(RateLimitMiddleware)
app.add_middleware(LoggingMiddleware)
app.add_middleware(AuthMiddleware)

# CORS Middleware Setup
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "https://weather-intelligence-pro.vercel.app"  # 🚀 TERI VERCEL LINK
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# API ROUTERS 
# ==========================================
app.include_router(auth_routes.router)
app.include_router(weather_routes.router)
app.include_router(aqi_routes.router)
app.include_router(water_routes.router)  # <--- FIX: Ye ab baaki sab jaisa clean hai!
app.include_router(analytics_routes.router)
app.include_router(report_routes.router)
app.include_router(history_routes.router)
app.include_router(notification_routes.router)
app.include_router(admin_routes.router)
app.include_router(forecast_routes.router)
app.include_router(websocket_routes.router)
app.include_router(prediction_routes.router)
app.include_router(ai_routes.router)
app.include_router(map_routes.router)
app.include_router(observability_routes.router)
app.include_router(legal_routes.router)
app.include_router(satellite_routes.router)
app.include_router(workflow_routes.router)

# ==========================================
# HEALTH CHECKS
# ==========================================
@app.get("/", tags=["Health & Status"])
def home():
    return {"message": f"{settings.APP_NAME} API Running 🚀", "version": settings.VERSION}

@app.get("/health", tags=["Health & Status"])
def health_check():
    return {"status": "healthy", "server": "online", "app": settings.APP_NAME}