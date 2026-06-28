from fastapi.testclient import TestClient

# In every test file, change the import to:
from backend.main import app

client = TestClient(app)


# ==========================================
# Admin Dashboard
# ==========================================

def test_admin_dashboard():
    response = client.get("/admin/dashboard")
    # Allows 200 (Success), 401 (Unauthorized), or 403 (Forbidden)
    assert response.status_code in [200, 401, 403]


# ==========================================
# Get All Users
# ==========================================

def test_get_users():
    response = client.get("/admin/users")
    assert response.status_code in [200, 401, 403]


# ==========================================
# Login Logs
# ==========================================

def test_login_logs():
    response = client.get("/admin/login-logs")
    assert response.status_code in [200, 401, 403]


# ==========================================
# Reports
# ==========================================

def test_reports():
    response = client.get("/admin/reports")
    assert response.status_code in [200, 401, 403]


# ==========================================
# Admin Response Type
# ==========================================

def test_admin_response():
    response = client.get("/admin/dashboard")
    
    # Only test the structure if the request actually bypassed auth
    if response.status_code == 200:
        assert isinstance(response.json(), dict)