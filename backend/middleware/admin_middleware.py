from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from backend.security import verify_token
from backend.database import SessionLocal
from backend.models import User

# ==========================================
# Admin Middleware
# ==========================================

class AdminMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        # 1. Pass through normally if it's NOT an admin route
        if not request.url.path.startswith("/admin"):
            return await call_next(request)

        # 2. Extract Authorization Header
        token = request.headers.get("Authorization")

        if not token:
            return JSONResponse(
                status_code=401,
                content={"detail": "Authorization token missing"}
            )

        # 3. Strip prefix and verify token
        token = token.replace("Bearer ", "")
        username = verify_token(token)

        if username is None:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid or expired token"}
            )

        # 4. Connect to the database to check the user's exact role
        db = SessionLocal()
        
        try:
            user = db.query(User).filter(User.username == username).first()

            # 5. Reject if the user doesn't exist or lacks admin privileges
            if user is None or user.role.lower() != "admin":
                return JSONResponse(
                    status_code=403, # 403 Forbidden is perfect here
                    content={"detail": "Admin access required"}
                )
        finally:
            # Always close the DB session to prevent memory leaks!
            db.close()

        # 6. Allow the verified admin to proceed
        return await call_next(request)