import os
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext

# 1. Initialize CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 2. JWT Configuration (Loads from .env in production)
SECRET_KEY = os.getenv("SECRET_KEY", "weather_intelligence_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# ==========================================
# Password Hashing (Bcrypt Limit Fix)
# ==========================================

def hash_password(password: str) -> str:
    # Bcrypt has a hard 72-byte limit. 
    # We truncate the password string to 72 characters before hashing 
    # to prevent the ValueError (500 Internal Server Error).
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # 1. Truncate the incoming password to match the hashing logic
    truncated_password = plain_password[:72]
    
    # 2. Print statements for debugging (Terminal mein check karna)
    # Ye tumhare project ke output mein dikhega ki kya check ho raha hai
    # print(f"DEBUG: Comparing '{truncated_password}' with hash '{hashed_password[:10]}...'")
    
    is_valid = pwd_context.verify(truncated_password, hashed_password)
    
    # print(f"DEBUG: Password match result: {is_valid}")
    
    return is_valid
# ==========================================
# JWT Token Generation & Verification
# ==========================================

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    
    # Python 3.12 Best Practice: Use timezone-aware UTC datetimes
    now = datetime.now(timezone.utc)
    
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            return None
        return username
    except JWTError:
        return None