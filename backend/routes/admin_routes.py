from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Updated to match your exact folder structure
from backend.dependencies import get_db

from backend.services.admin_service import (
    get_admin_dashboard,
    get_all_users,
    get_user_by_id,
    delete_user,
    get_login_logs
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


# ==========================================
# Admin Dashboard
# ==========================================

@router.get("/dashboard")
def admin_dashboard(
    db: Session = Depends(get_db)
):
    return get_admin_dashboard(db)


# ==========================================
# Get All Users
# ==========================================

@router.get("/users")
def fetch_users(
    db: Session = Depends(get_db)
):
    return get_all_users(db)


# ==========================================
# Get User By ID
# ==========================================

@router.get("/users/{user_id}")
def fetch_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = get_user_by_id(
        user_id,
        db
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# ==========================================
# Delete User
# ==========================================

@router.delete("/users/{user_id}")
def remove_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    response = delete_user(
        user_id,
        db
    )

    if "error" in response:
        raise HTTPException(
            status_code=404,
            detail=response["error"]
        )

    return response


# ==========================================
# Login Logs
# ==========================================

@router.get("/login-logs")
def fetch_login_logs(
    db: Session = Depends(get_db)
):
    return get_login_logs(db)