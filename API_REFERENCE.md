# API_REFERENCE.md

# Weather Intelligence Pro - API Reference

Version: 1.0.0

Base URL

http://127.0.0.1:8000

Production URL

TBD

---

# Authentication

Authentication uses JWT Bearer Tokens.

Protected endpoints require:

Authorization: Bearer <JWT_TOKEN>

---

# Authentication APIs

## Register User

POST /auth/register

Request

```json
{
    "username": "john",
    "email": "john@example.com",
    "password": "Password@123"
}
```

Response

```json
{
    "success": true,
    "message": "User registered successfully"
}
```

---

## Login

POST /auth/login

Request

```json
{
    "username": "john",
    "password": "Password@123"
}
```

Response

```json
{
    "access_token": "...",
    "token_type": "bearer"
}
```

---

# Weather APIs

## Fetch Weather

POST /weather/fetch

Query

city=Delhi

Headers

Authorization: Bearer Token

Response

```json
{
    "city": "Delhi",
    "temperature": 34.8,
    "humidity": 62,
    "wind_speed": 3.2
}
```

---

## Weather History

GET /weather/history

Headers

Authorization: Bearer Token

Response

```json
[
    {
        "city":"Delhi",
        "temperature":34.5,
        "humidity":60,
        "recorded_at":"2026-06-26T10:20:00"
    }
]
```

---

# AQI APIs

## Fetch AQI

GET /aqi/{city}

Example

/aqi/Delhi

Response

```json
{
    "city":"Delhi",
    "aqi":165,
    "category":"Unhealthy"
}
```

---

## AQI History

GET /aqi/history

---

# Water Quality APIs

## Water Quality

GET /water/{city}

Response

```json
{
    "city":"Delhi",
    "ph":7.3,
    "dissolved_oxygen":8.1,
    "quality":"Good"
}
```

---

# Forecast APIs

## Forecast

GET /forecast/{city}

Response

```json
{
    "city":"Delhi",
    "forecast":[
        {
            "date":"2026-06-27",
            "temperature":35,
            "humidity":55
        }
    ]
}
```

---

# AI Prediction APIs

## Predict AQI

POST /ai/predict

Request

```json
{
    "temperature":32.5,
    "humidity":45,
    "wind_speed":3.2
}
```

Response

```json
{
    "predicted_aqi":142
}
```

---

# Analytics APIs

## Dashboard Analytics

GET /analytics/dashboard

Response

```json
{
    "total_users":120,
    "weather_requests":5400,
    "aqi_requests":3200
}
```

---

## Weather Searches

GET /analytics/weather-searches

---

## AQI Searches

GET /analytics/aqi-searches

---

## Users

GET /analytics/users

---

# Reports APIs

## Export Excel

GET /reports/excel

Downloads

Weather History Excel

---

## Export CSV

GET /reports/csv

---

## Export PDF

GET /reports/pdf

---

# Notification APIs

## Send Notification

POST /notifications/send

---

## Notification History

GET /notifications/history

---

# WebSocket APIs

Endpoint

/ws

Purpose

Real-time Weather Updates

Real-time AQI

Live Dashboard Updates

Notifications

---

# Admin APIs

Admin Login

POST /admin/login

Admin Dashboard

GET /admin/dashboard

User Management

GET /admin/users

Delete User

DELETE /admin/users/{id}

System Logs

GET /admin/logs

---

# Response Format

Success

```json
{
    "success":true,
    "message":"Operation Successful",
    "data":{}
}
```

Error

```json
{
    "success":false,
    "message":"Something went wrong",
    "error":"Description"
}
```

---

# Authentication Flow

Register

↓

Login

↓

Receive JWT

↓

Authorize Swagger

↓

Access Protected APIs

---

# HTTP Status Codes

200 OK

201 Created

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

422 Validation Error

500 Internal Server Error

---

# External APIs

OpenWeather API

Current Weather

Forecast

Air Pollution

---

# Database Tables

users

weather_history

aqi_history

water_quality

notifications

reports

search_history

---

# Testing

Framework

pytest

Current Status

34 Tests Passing

Test Coverage

Authentication

Weather

AQI

Forecast

Prediction

Analytics

Reports

Admin

WebSocket

---

# AI Assistant Notes

Never modify endpoint URLs without updating this file.

Always keep request and response schemas synchronized with Pydantic models.

Whenever a new endpoint is created:

1. Add it here.

2. Add Swagger documentation.

3. Add Pytest test cases.

4. Update README if it is a major feature.

Maintain REST API principles.

Follow JWT authentication for all protected routes.
