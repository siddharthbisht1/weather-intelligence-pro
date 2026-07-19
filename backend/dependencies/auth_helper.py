from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from backend.security import verify_token
from backend.exceptions.custom_exceptions import InvalidCredentialsException



oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def require_auth(token: str = Depends(oauth2_scheme)):
    """
    Validates the provided JWT token and returns the corresponding username.
    """
    username = verify_token(token)

    if username is None:
        raise InvalidCredentialsException()

    return username