from fastapi import APIRouter, HTTPException
from backend.services.notification_service import (
    fetch_user_notifications,
    create_notification,
    delete_notification,
    mark_all_as_read
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

# ==========================================
# 1. BFF Endpoint (Specifically for notifications.html)
# ==========================================

@router.get("/data")
def get_notification_dashboard_data():
    """
    Returns structured data (stats, formatted UI notifications, priorities) 
    for the Notification Center frontend.
    """
    return fetch_user_notifications()


# ==========================================
# 2. Action Endpoints (Triggered from UI buttons)
# ==========================================

@router.post("/mark-read")
def mark_notifications_read():
    """
    Marks all notifications as read when the 'Mark All Read' button is clicked.
    """
    return mark_all_as_read()


# ==========================================
# 3. Standard CRUD Endpoints (For Admin / System use)
# ==========================================

@router.post("/")
def add_new_notification(title: str, message: str, notification_type: str = "weather"):
    """
    Creates a new notification. (e.g., triggered by an external AI worker)
    """
    return create_notification(title, message, notification_type)


@router.delete("/{notification_id}")
def remove_notification(notification_id: int):
    """
    Deletes a specific notification by ID.
    """
    result = delete_notification(notification_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result