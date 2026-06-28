from fastapi import APIRouter, HTTPException
from backend.services.notification_service import (
    get_all_notifications,
    get_notification_by_id,
    create_notification,
    delete_notification
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

@router.get("/")
def fetch_notifications():
    return get_all_notifications()

@router.get("/{notification_id}")
def fetch_single_notification(notification_id: int):
    notification = get_notification_by_id(notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

@router.post("/")
def add_new_notification(title: str, message: str, notification_type: str):
    return create_notification(title, message, notification_type)

@router.delete("/{notification_id}")
def remove_notification(notification_id: int):
    result = delete_notification(notification_id)
    if not result:
        raise HTTPException(status_code=404, detail="Notification not found")
    return result