import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from fastapi.testclient import TestClient

# 1. Ensure the root directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# 2. Now import your app
from backend.main import app
from backend.database import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# In backend/main.py, do NOT use 'from config import ...'
# Use:
from backend.config import settings
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # This line ensures your SQL models are actually turned into tables
    Base.metadata.create_all(bind=engine) 
    yield
    Base.metadata.drop_all(bind=engine)
# 3. Setup Test DB
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
            
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
# Make sure you have pytest imported at the top of conftest.py
import pytest 

# ... (your other fixtures like client and setup_database remain here) ...

@pytest.fixture
def auth_headers(client):
    """
    Registers a user, logs them in, and returns the Authorization header.
    """
    # 1. Register a test user
    client.post(
        "/auth/register",
        json={
            "username": "testuser_auth",
            "email": "testauth@example.com",
            "password": "password123"
        }
    )
    
    # 2. Log in to get the token
    response = client.post(
        "/auth/login",
        json={
            "username": "testuser_auth",
            "password": "password123"
        }
    )
    
    # 3. Return the header dictionary
    token = response.json().get("access_token")
    return {"Authorization": f"Bearer {token}"}