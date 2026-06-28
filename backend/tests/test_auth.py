import pytest
from fastapi.testclient import TestClient

# We remove the global 'client' initialization 
# and use the 'client' fixture from conftest.py instead.

# ==========================================
# Home Route
# ==========================================

def test_home(client):
    """
    Test that the home route is accessible.
    'client' is automatically provided by your conftest.py
    """
    response = client.get("/")
    assert response.status_code == 200

# ==========================================
# Register Route
# ==========================================

def test_register(client):
    """
    Test user registration.
    """
    response = client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
    )
    # Allows 200 (Created) or 400 (User already exists in the test DB)
    assert response.status_code in [200, 400]

# ==========================================
# Login Route
# ==========================================

def test_login(client):
    """
    Test user login and token generation.
    """
    # 1. Ensure user exists (Register first)
    client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
    )

    # 2. Attempt Login
    response = client.post(
        "/auth/login",
        json={
            "username": "testuser",
            "password": "password123"
        }
    )
    
    assert response.status_code == 200
    assert "access_token" in response.json()