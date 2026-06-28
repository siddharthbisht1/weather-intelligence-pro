from datetime import datetime

# ==========================================
# Get Current Timestamp
# ==========================================

def current_timestamp():
    """
    Returns the current system date and time.
    """
    return datetime.now()


# ==========================================
# Format Datetime
# ==========================================

def format_datetime(dt: datetime) -> str:
    """
    Formats a datetime object into a standard YYYY-MM-DD HH:MM:SS string.
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")