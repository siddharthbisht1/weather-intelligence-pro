import re

# ==========================================
# Email Validator
# ==========================================

def validate_email(email: str) -> bool:
    """
    Checks if the provided string is a valid email address format.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


# ==========================================
# Password Validator
# ==========================================

def validate_password(password: str) -> bool:
    """
    Checks if the password meets minimum security requirements.
    Currently: Must be at least 8 characters long.
    """
    return len(password) >= 8