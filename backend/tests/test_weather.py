import pytest

# ==========================================
# Weather API Test
# ==========================================

def test_weather(client, auth_headers):
    # FIXED: Use POST instead of GET, route is /weather/fetch, and expect 201
    response = client.post("/weather/fetch?city=Delhi", headers=auth_headers)
    assert response.status_code == 201


# ==========================================
# Weather Response Structure
# ==========================================

def test_weather_response(client, auth_headers):
    # FIXED: Update to POST /weather/fetch
    response = client.post("/weather/fetch?city=Delhi", headers=auth_headers)
    data = response.json()
    
    assert "city" in data
    assert "temperature" in data
    assert "humidity" in data
    assert "wind_speed" in data


# ==========================================
# Invalid City
# ==========================================

def test_invalid_city(client, auth_headers):
    # FIXED: Update to POST /weather/fetch
    response = client.post("/weather/fetch?city=abcdefghxyz", headers=auth_headers)
    # Allows 404 (Not Found), 400 (Bad Request), or 422 (Validation Error)
    assert response.status_code in [404, 400, 422]