import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Ensure database directory exists
os.makedirs("./database", exist_ok=True)

# 2. Database URL (Directly using SQLite for now)
DATABASE_URL = "sqlite:///./database/users.db"

# 3. Create Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} # Required for SQLite in FastAPI
)

# 4. Create SessionLocal
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 5. Create Base class for your models
Base = declarative_base()

# 6. Database Session Dependency
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