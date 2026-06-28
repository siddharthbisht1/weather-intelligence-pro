import pytest

# We remove the global 'client' initialization 
# and use the 'client' and 'auth_headers' fixtures from conftest.py instead.

# ==========================================
# Forecast API Test
# ==========================================

def test_forecast(client, auth_headers):
    response = client.get("/forecast/Delhi", headers=auth_headers)
    assert response.status_code == 200


# ==========================================
# Forecast Response Structure
# ==========================================

def test_forecast_response(client, auth_headers):
    response = client.get("/forecast/Delhi", headers=auth_headers)
    data = response.json()
    
    assert "city" in data
    assert "forecast" in data
    assert isinstance(data["forecast"], list)


# ==========================================
# Forecast Item Structure
# ==========================================

def test_forecast_item(client, auth_headers):
    response = client.get("/forecast/Delhi", headers=auth_headers)
    data = response.json()
    
    # We use .get() to safely check if 'forecast' exists before checking length
    if data.get("forecast") and len(data["forecast"]) > 0:
        item = data["forecast"][0]
        
        assert "datetime" in item
        assert "temperature" in item
        assert "humidity" in item
        assert "wind_speed" in item
        assert "description" in item


# ==========================================
# Invalid City
# ==========================================

def test_invalid_city(client, auth_headers):
    response = client.get("/forecast/abcdefghxyz", headers=auth_headers)
    # Allows 400 (Bad Request) or 404 (Not Found)
    assert response.status_code in [400, 404]