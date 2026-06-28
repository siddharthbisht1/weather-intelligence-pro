from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from backend.security import verify_token

# This tells FastAPI how to get the token from the request
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Dependency to be used in routes that require authentication.
    """
    username = verify_token(token)
    
    if username is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    
    return username