from fastapi import HTTPException, status

# ==========================================
# User Exceptions
# ==========================================

class UserNotFoundException(HTTPException):
    def __init__(self, detail: str = "User not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )

class InvalidCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"} # Standard for 401 responses
        )

class UnauthorizedException(HTTPException):
    def __init__(self, detail: str = "Access denied"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail
        )

# ==========================================
# Domain-Specific Exceptions (Weather/AQI)
# ==========================================

class WeatherNotFoundException(HTTPException):
    def __init__(self, detail: str = "Weather data not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )

class AQINotFoundException(HTTPException):
    def __init__(self, detail: str = "AQI data unavailable"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )

class ReportNotFoundException(HTTPException):
    def __init__(self, detail: str = "The requested report was not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )