import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

os.makedirs("./backend/database", exist_ok=True)

DATABASE_URL = "sqlite:///./backend/database/users.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} 
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    """
    Creates an independent database session for each request
    and securely closes it when the request is finished.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()