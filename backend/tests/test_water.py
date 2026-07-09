import pytest

def test_water(client, auth_headers):
    # Naya Correct URL
    response = client.get("/water/data/Delhi", headers=auth_headers) 
    assert response.status_code == 200

def test_water_response(client, auth_headers):
    response = client.get("/water/data/Delhi", headers=auth_headers)
    data = response.json()
    
    # API ke naye detailed structure ke hisaab se asserts
    assert "city" in data
    assert "kpis" in data
    assert "ph" in data["kpis"]
    
def test_invalid_city(client, auth_headers):
    response = client.get("/water/data/abcdefghxyz", headers=auth_headers)
    assert response.status_code in [200, 400, 404]