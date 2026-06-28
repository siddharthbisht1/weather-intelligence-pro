from fastapi.testclient import TestClient

# In every test file, change the import to:
from backend.main import app
client = TestClient(app)


# ==========================================
# Reports API Test
# ==========================================

def test_reports():
    response = client.get("/reports")
    # Allows 200 (Success), 401 (Unauthorized), or 403 (Forbidden)
    assert response.status_code in [200, 401, 403]


# ==========================================
# Reports Response Type
# ==========================================

def test_reports_response():
    response = client.get("/reports")
    
    # Only test the structure if the request actually bypassed auth
    if response.status_code == 200:
        assert isinstance(response.json(), list)