from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

# Local imports
from backend.security import verify_token
from backend.exceptions.custom_exceptions import InvalidCredentialsException

# ==========================================
# OAuth2 Scheme
# ==========================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

# ==========================================
# Require Authentication
# ==========================================

def require_auth(token: str = Depends(oauth2_scheme)):
    """
    Validates the provided JWT token and returns the corresponding username.
    """
    username = verify_token(token)

    if username is None:
        # Replaced the verbose HTTPException with your custom exception
        raise InvalidCredentialsException()

    return username