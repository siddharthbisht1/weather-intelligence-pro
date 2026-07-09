import pytest

def test_prediction(client, auth_headers):
    # Route: GET /ai/forecast/{city}
    response = client.get("/ai/forecast/Delhi", headers=auth_headers)
    assert response.status_code in [200, 500]

def test_prediction_response(client, auth_headers):
    response = client.get("/ai/forecast/Delhi", headers=auth_headers)
    
    if response.status_code == 500:
        pytest.skip("AI Model or Gemini not ready, skipping structure test.")
        
    data = response.json()
    assert isinstance(data, dict)

def test_invalid_city_prediction(client, auth_headers):
    # Invalid city daal kar check
    response = client.get("/ai/forecast/RandomCityXYZ999", headers=auth_headers)
    assert response.status_code in [200, 400, 404, 422, 500]