from datetime import datetime

# ==========================================
# Temporary Notification Storage
# ==========================================

notifications = [
    {
        "id": 1,
        "title": "Heatwave Alert",
        "message": "Extreme temperatures expected this week.",
        "type": "warning",
        "time": datetime.now()
    },
    {
        "id": 2,
        "title": "AQI Warning",
        "message": "Air quality has deteriorated significantly.",
        "type": "danger",
        "time": datetime.now()
    },
    {
        "id": 3,
        "title": "Rain Forecast",
        "message": "Heavy rainfall expected in the next 24 hours.",
        "type": "info",
        "time": datetime.now()
    }
]


# ==========================================
# Get All Notifications
# ==========================================

def get_all_notifications():
    return notifications


# ==========================================
# Get Notification By ID
# ==========================================

def get_notification_by_id(notification_id: int):
    for notification in notifications:
        if notification["id"] == notification_id:
            return notification
    return None


# ==========================================
# Add Notification
# ==========================================

def create_notification(title: str, message: str, notification_type: str):
    new_notification = {
        "id": len(notifications) + 1,
        "title": title,
        "message": message,
        "type": notification_type,
        "time": datetime.now()
    }
    notifications.append(new_notification)
    return new_notification


# ==========================================
# Delete Notification
# ==========================================

def delete_notification(notification_id: int):
    global notifications
    initial_length = len(notifications)
    
    notifications = [
        notification
        for notification in notifications
        if notification["id"] != notification_id
    ]

    # Quick check to see if anything was actually deleted
    if len(notifications) == initial_length:
        return None

    return {
        "message": "Notification deleted successfully"
    }