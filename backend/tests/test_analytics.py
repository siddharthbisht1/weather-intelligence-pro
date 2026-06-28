import pytest

# We remove the global 'client' initialization 
# and use the 'client' and 'auth_headers' fixtures from conftest.py instead.

# ==========================================
# Dashboard Analytics
# ==========================================

def test_dashboard(client, auth_headers):
    response = client.get("/analytics/dashboard", headers=auth_headers)
    assert response.status_code == 200


# ==========================================
# Users Analytics
# ==========================================

def test_users(client, auth_headers):
    response = client.get("/analytics/users", headers=auth_headers)
    assert response.status_code == 200


# ==========================================
# Weather Searches Analytics
# ==========================================

def test_weather_searches(client, auth_headers):
    response = client.get("/analytics/weather-searches", headers=auth_headers)
    assert response.status_code == 200


# ==========================================
# AQI Searches Analytics
# ==========================================

def test_aqi_searches(client, auth_headers):
    response = client.get("/analytics/aqi-searches", headers=auth_headers)
    assert response.status_code == 200


# ==========================================
# Dashboard Response Structure
# ==========================================

def test_dashboard_response(client, auth_headers):
    response = client.get("/weather/city?q=London", headers=auth_headers)
    data = response.json()
    
    assert isinstance(data, dict)