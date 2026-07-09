import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# .env file se variables load karne ke liye
load_dotenv()

# Environment variable se URL lo, agar na mile toh SQLite fallback
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./backend/database/users.db")

# PRO TIP: Render kabhi-kabhi URL 'postgres://' format mein deta hai, 
# par SQLAlchemy ko ab 'postgresql://' chahiye hota hai. Yeh line usko fix karegi:
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# connect_args sirf SQLite ko chahiye, Postgres ko nahi
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

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