from fastapi import Depends
from sqlalchemy.orm import Session

# Local imports
from backend.database import get_db
from backend.models import User
from backend.dependencies.auth_helper import require_auth
from backend.dependencies.roles import require_role

from backend.exceptions.custom_exceptions import UserNotFoundException 

def get_manager(
    username: str = Depends(require_auth),
    db: Session = Depends(get_db)
):
    """
    Dependency to fetch the current user and ensure they have manager privileges.
    """
    user = db.query(User).filter(User.username == username).first()

    if user is None:
        
        raise UserNotFoundException()

    require_role(user.role, "manager")

    return user