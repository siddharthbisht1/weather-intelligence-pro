from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

from backend.exceptions.custom_exceptions import (
    UserNotFoundException,
    InvalidCredentialsException,
    UnauthorizedException,
    WeatherNotFoundException,
    AQINotFoundException
)

# ==========================================
# Unified Custom Exception Handler
# ==========================================

async def unified_exception_handler(request: Request, exc: HTTPException):
    """
    Handles any custom exception that inherits from HTTPException,
    dynamically pulling the status code and detail.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail
        }
    )