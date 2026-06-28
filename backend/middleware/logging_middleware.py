import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Import the centralized logger we built earlier!
from backend.logging_config import logger

# ==========================================
# Logging Middleware
# ==========================================

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Start the stopwatch
        start_time = time.time()

        # Process the incoming request
        response = await call_next(request)

        # Stop the stopwatch and calculate the total duration
        process_time = round(time.time() - start_time, 4)

        # Log the exact method, path, status, and latency
        logger.info(
            f"{request.method} {request.url.path} - "
            f"Status: {response.status_code} - "
            f"Time: {process_time}s"
        )

        return response