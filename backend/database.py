import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# 1. DATABASE URLs SETUP
# ==========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")
os.makedirs(DB_DIR, exist_ok=True)

# Primary (Neon Postgres) aur Fallback (SQLite) URLs
PRIMARY_URL = os.getenv("DATABASE_URL")
FALLBACK_URL = f"sqlite:///{os.path.join(DB_DIR, 'users.db')}"

# ==========================================
# 2. AUTO-FAILOVER CONNECTION LOGIC
# ==========================================
engine = None

try:
    print("🔄 Attempting to connect to Primary Database (Neon Postgres)...")
    # Engine banaya (Primary ke liye)
    temp_engine = create_engine(PRIMARY_URL)
    
    # Connection test karne ke liye ek dummy connect try karte hain
    with temp_engine.connect() as conn:
        print("✅ Success: Connected to Primary Cloud Database!")
    
    # Agar upar error nahi aaya, toh primary engine final ho gaya
    engine = temp_engine

except Exception as e:
    print(f"⚠️ Primary DB Connection Failed! Error: {e}")
    print("🔄 Switching to Fallback Database (Local SQLite)...")
    
    # Fallback (SQLite) engine activate kar diya
    engine = create_engine(
        FALLBACK_URL, 
        connect_args={"check_same_thread": False}
    )
    print("✅ Success: Connected to Fallback SQLite Database!")

# ==========================================
# 3. SESSION & BASE SETUP
# ==========================================
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
    """
    App start hone par tables create karega (Primary ya Fallback jo bhi active ho).
    """
    # Import models explicitly taaki tables map ho sakein
    from backend import models 
    Base.metadata.create_all(bind=engine)