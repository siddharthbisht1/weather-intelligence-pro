from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db # Import your generator from database.py
from backend.models import User
from backend.dependencies.current_user import get_current_user

def get_admin_user(
    username: str = Depends(get_current_user),
    db: Session = Depends(get_db)  # Inject the session automatically
):
    user = db.query(User).filter(User.username == username).first()
    
    if user is None or user.role.lower() != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )
    return user