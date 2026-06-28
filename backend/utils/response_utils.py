from typing import Any, Optional

# ==========================================
# Success Response Formatter
# ==========================================

def success_response(message: str, data: Optional[Any] = None) -> dict:
    """
    Standardizes successful API responses.
    """
    return {
        "success": True,
        "message": message,
        "data": data
    }


# ==========================================
# Error Response Formatter
# ==========================================

def error_response(message: str) -> dict:
    """
    Standardizes error API responses.
    """
    return {
        "success": False,
        "message": message
    }