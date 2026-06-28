from fastapi import Request
from fastapi.responses import JSONResponse
async def dispatch(self, request: Request, call_next):
    # OPTIONS request ko bina token ke jaane do
    if request.method == "OPTIONS":
        return await call_next(request)
        
    # Yahan tumhara baaki auth logic hoga...
from starlette.middleware.base import BaseHTTPMiddleware

from backend.security import verify_token

# ==========================================
# Authentication Middleware
# ==========================================

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        # 1. Define Public Routes (No token required)
        public_routes = [
            "/",
            "/docs",
            "/redoc",
            "/openapi.json",
            "/auth/login",
            "/auth/register"
        ]

        if request.url.path in public_routes:
            return await call_next(request)

        # 2. Extract Authorization Header
        token = request.headers.get("Authorization")

        if not token:
            return JSONResponse(
                status_code=401,
                content={"detail": "Authorization token missing"}
            )

        # 3. Strip out the "Bearer " prefix
        token = token.replace("Bearer ", "")

        # 4. Verify the Token via Security Module
        username = verify_token(token)

        if username is None:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid or expired token"}
            )

        # 5. Attach the authenticated username to the request state
        request.state.username = username

        # 6. Pass the request to the next layer
        response = await call_next(request)
        return response