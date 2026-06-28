import time
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

# ==========================================
# Request Cache
# ==========================================

request_history = {}

# Maximum requests allowed
MAX_REQUESTS = 100

# Time window in seconds
TIME_WINDOW = 60

# ==========================================
# Rate Limit Middleware
# ==========================================

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()

        # 1. Create history for new clients
        if client_ip not in request_history:
            request_history[client_ip] = []

        # 2. Remove expired requests (outside the 60-second window)
        request_history[client_ip] = [
            timestamp for timestamp in request_history[client_ip]
            if current_time - timestamp < TIME_WINDOW
        ]

        # 3. Check request count against the maximum limit
        if len(request_history[client_ip]) >= MAX_REQUESTS:
            return JSONResponse(
                status_code=429,
                content={"detail": "Too many requests. Please try again later."}
            )

        # 4. Store the current request timestamp
        request_history[client_ip].append(current_time)

        # 5. Proceed to the next middleware or route
        response = await call_next(request)
        return response