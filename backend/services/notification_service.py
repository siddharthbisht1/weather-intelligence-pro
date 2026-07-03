from datetime import datetime

# ==========================================
# 1. In-Memory Database (State)
# ==========================================

notifications_db = [
    {
        "id": 1,
        "title": "Heatwave Alert (Dehradun)",
        "message": "Extreme temperatures expected this week. Stay hydrated.",
        "type": "weather",
        "time": datetime.now(),
        "is_read": False
    },
    {
        "id": 2,
        "title": "AQI Warning (Delhi)",
        "message": "Air quality has deteriorated significantly. Wear a mask.",
        "type": "aqi",
        "time": datetime.now(),
        "is_read": False
    },
    {
        "id": 3,
        "title": "AI Prediction Update",
        "message": "Rain expected in 24 hours. Hydration goals updated.",
        "type": "ai",
        "time": datetime.now(),
        "is_read": True
    }
]

# ==========================================
# 2. UI Helper Functions (The BFF Layer)
# ==========================================

def _enrich_for_ui(notif: dict):
    """
    Takes a raw database record and attaches UI-specific classes and icons
    so the frontend doesn't have to write complex if/else logic.
    """
    ui_map = {
        "weather": {"icon": "fa-sun", "color_class": "blue"},
        "aqi": {"icon": "fa-lungs", "color_class": "green"},
        "ai": {"icon": "fa-robot", "color_class": "purple"},
        "danger": {"icon": "fa-triangle-exclamation", "color_class": "red"}
    }
    
    meta = ui_map.get(notif["type"], {"icon": "fa-bell", "color_class": "blue"})
    
    # Format time nicely for the UI (e.g., "Just now" or "2 hours ago")
    # For simplicity, we are returning a static string, but in production, 
    # you'd calculate the time difference here.
    time_str = notif["time"].strftime("%I:%M %p, %d %b")

    return {
        "id": notif["id"],
        "title": notif["title"],
        "message": notif["message"],
        "type": notif["type"],
        "is_read": notif.get("is_read", False),
        "time": time_str,
        "icon": meta["icon"],
        "color_class": meta["color_class"]
    }

# ==========================================
# 3. Core Service Methods
# ==========================================

def fetch_user_notifications():
    """
    The main endpoint for the Dashboard. Reads from the DB and formats for UI.
    """
    enriched_notifications = [_enrich_for_ui(n) for n in notifications_db]
    
    unread_count = sum(1 for n in enriched_notifications if not n["is_read"])
    read_count = len(enriched_notifications) - unread_count

    return {
        "stats": {
            "total": len(enriched_notifications),
            "read": read_count,
            "unread": unread_count
        },
        "notifications": enriched_notifications[::-1], # Return newest first
        "active_priorities": [
            {"level": "high", "color": "#F87171", "text": "Severe Heatwave (Dehradun)"},
            {"level": "medium", "color": "#FACC15", "text": "AQI Rising in Delhi Sector"}
        ]
    }

def create_notification(title: str, message: str, notification_type: str = "weather"):
    """
    Adds a new alert to the system. The dashboard will show this on next refresh.
    """
    new_id = max([n["id"] for n in notifications_db] + [0]) + 1
    
    new_notif = {
        "id": new_id,
        "title": title,
        "message": message,
        "type": notification_type,
        "time": datetime.now(),
        "is_read": False
    }
    notifications_db.append(new_notif)
    return new_notif

def delete_notification(notification_id: int):
    """
    Removes a notification from the DB.
    """
    global notifications_db
    initial_length = len(notifications_db)
    notifications_db = [n for n in notifications_db if n["id"] != notification_id]
    
    if len(notifications_db) == initial_length:
        return {"error": "Notification not found"}
    return {"message": "Notification deleted successfully"}

def mark_all_as_read():
    """
    Marks all unread notifications as read.
    """
    for n in notifications_db:
        n["is_read"] = True
    return {"message": "All marked as read"}