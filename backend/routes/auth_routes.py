from datetime import timedelta, datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from backend.database import get_db
from backend.models import LoginLog, User
from backend.schemas import UserCreate, UserLogin
from backend.security import hash_password, verify_password, create_access_token
from backend.config import settings

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@router.get("/me")
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
        
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
        
    return {
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "phone": "+91 98765 43210", 
        "location": "Dehradun, India"
    }


@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
        role=user.role 
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": f"User registered successfully with role: {user.role}"}


@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(
        data={"sub": db_user.username, "role": db_user.role}, 
        expires_delta=timedelta(minutes=60)
    )
    
    try:
        new_login_log = LoginLog(
            user_id=db_user.id,
            username=db_user.username,  
            login_time=datetime.now(timezone.utc)
        )
        db.add(new_login_log)
        db.commit()
    except Exception as e:
        print(f"Login log save nahi hua: {e}")
        db.rollback()
        
    return {
        "message": "Login Successful",
        "access_token": access_token,
        "token_type": "bearer",
        "role": db_user.role
    }