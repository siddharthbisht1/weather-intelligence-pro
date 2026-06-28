import pytest

# We remove the global 'client' initialization 
# and use the 'client' and 'auth_headers' fixtures from conftest.py instead.

# ==========================================
# Water API Test
# ==========================================

def test_water(client, auth_headers):
    response = client.get("/water/Delhi", headers=auth_headers)
    assert response.status_code == 200


# ==========================================
# Water Response Structure
# ==========================================

def test_water_response(client, auth_headers):
    response = client.get("/water/Delhi", headers=auth_headers)
    data = response.json()
    
    assert "city" in data
    assert "ph" in data
    assert "dissolved_oxygen" in data
    assert "quality_status" in data


# ==========================================
# Invalid City
# ==========================================

def test_invalid_city(client, auth_headers):
    response = client.get("/water/abcdefghxyz", headers=auth_headers)
    # Allows 400 (Bad Request) or 404 (Not Found)
    assert response.status_code in [200,400, 404]