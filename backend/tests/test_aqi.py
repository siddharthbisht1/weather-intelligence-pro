import pytest

# We remove the global 'client' initialization 
# and use the 'client' and 'auth_headers' fixtures from conftest.py instead.

# ==========================================
# AQI API Test
# ==========================================

def test_aqi(client, auth_headers):
    response = client.get("/aqi/Delhi", headers=auth_headers)
    assert response.status_code == 200


# ==========================================
# AQI Response Structure
# ==========================================

def test_aqi_response(client, auth_headers):
    response = client.get("/aqi/Delhi", headers=auth_headers)
    data = response.json()
   
    assert "aqi" in data


# ==========================================
# Invalid City
# ==========================================

def test_invalid_city(client, auth_headers):
    response = client.get("/aqi/abcdefghxyz", headers=auth_headers)
    # Allows 404 (Not Found) or 400 (Bad Request)
    assert response.status_code in [404, 400]