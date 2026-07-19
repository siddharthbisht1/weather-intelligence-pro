import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")
os.makedirs(DB_DIR, exist_ok=True)

DB_PATH = os.path.join(DB_DIR, "users.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

# 5. Engine aur Session setup (Tera code)
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
def init_db():
    Base.metadata.create_all(bind=engine)