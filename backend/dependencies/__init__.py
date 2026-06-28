from backend.database import SessionLocal

def get_db():
    """
    FastAPI dependency that creates a new database session for each request
    and ensures it is closed after the request is finished.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()