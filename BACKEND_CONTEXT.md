# BACKEND_CONTEXT.md

# Weather Intelligence Pro - Backend Context

## Overview

The backend is built using **FastAPI** and follows a modular, service-oriented architecture.

It is responsible for:

* User Authentication
* Weather APIs
* AQI Monitoring
* Water Quality Analysis
* AI Predictions
* Analytics
* Report Generation
* Notifications
* WebSocket Communication
* Admin Operations

The backend is designed to be scalable, secure, and maintainable.

---

# Technology Stack

Framework

* FastAPI

Language

* Python 3.12+

ORM

* SQLAlchemy

Database

* SQLite (Development)
* PostgreSQL (Production - Planned)

Authentication

* JWT
* OAuth2 Password Bearer

Password Hashing

* Passlib (bcrypt)

Validation

* Pydantic

Testing

* Pytest

ML

* Scikit-learn

Server

* Uvicorn

---

# Folder Structure

backend/

```
backend/

routes/
services/
middleware/
dependencies/
exceptions/
ml/
tests/
utils/
database.py
models.py
schemas.py
security.py
config.py
main.py
```

---

# Request Flow

Client

↓

FastAPI Route

↓

Dependency Injection

↓

Middleware

↓

Service Layer

↓

Database / ML / External API

↓

Response Model

↓

JSON Response

---

# Core Modules

## main.py

Application Entry Point

Responsibilities

* Create FastAPI App
* Register Routes
* Register Middleware
* Register Exception Handlers
* Configure CORS

Never place business logic here.

---

## routes/

Contains all API endpoints.

Example

auth.py

weather.py

aqi.py

prediction.py

analytics.py

reports.py

admin.py

notifications.py

websocket.py

Routes should only

* Receive Request

* Validate Input

* Call Services

* Return Response

---

## services/

Contains business logic.

Example

weather_service.py

aqi_service.py

report_service.py

prediction_service.py

analytics_service.py

notification_service.py

Never access services directly from frontend.

Routes should always call services.

---

## dependencies/

Reusable FastAPI dependencies.

Includes

Current User

Admin User

Manager User

Authentication Helper

Role Checker

Database Session

---

## middleware/

Global middleware.

Current

Authentication

Admin

Logging

Rate Limiting

Execution Time

Request Logging

Middleware should never contain business logic.

---

## exceptions/

Centralized exception handling.

Contains

Custom Exceptions

Exception Handlers

Error Responses

Always raise custom exceptions where possible.

---

## utils/

Helper functions.

Examples

Logger

Validators

Date Helpers

Formatters

JWT Helpers

Keep utilities stateless.

---

## ml/

Machine Learning components.

Files

dataset.csv

model.pkl

scaler.pkl

train_model.py

predict_model.py

Load trained models once during startup.

Never retrain during API requests.

---

## tests/

Pytest test suite.

Coverage

Authentication

Weather

AQI

Forecast

Prediction

Reports

Analytics

Admin

WebSocket

Current

34 Tests Passing

---

# Authentication

JWT Based

Flow

Register

↓

Login

↓

Receive Token

↓

Bearer Authorization

↓

Protected APIs

---

# Database

ORM

SQLAlchemy

Main Tables

users

weather_history

aqi_history

water_quality

reports

notifications

search_history

Use ORM only.

Avoid raw SQL.

---

# Security

Password Hashing

JWT

Protected Routes

Role-Based Access

Admin Authorization

Rate Limiting

Input Validation

CORS

---

# API Categories

Authentication

Weather

AQI

Water

Prediction

Forecast

Reports

Analytics

Notifications

Admin

WebSocket

---

# Response Format

Success

```json
{
  "success": true,
  "message": "...",
  "data": {}
}
```

Error

```json
{
  "success": false,
  "message": "...",
  "error": "..."
}
```

---

# Logging

Every request should log

Timestamp

Route

Method

Execution Time

Status Code

Errors

Authentication Events

---

# Error Handling

Use centralized handlers.

Raise

HTTPException

or

Custom Exceptions

Never return plain strings.

---

# Environment Variables

Store

JWT Secret

Database URL

API Keys

SMTP Credentials

Never hardcode secrets.

Use .env.

---

# Coding Standards

Use type hints.

Follow PEP8.

Keep functions under 50 lines where practical.

Prefer reusable services.

Avoid duplicate code.

Separate concerns.

---

# Future Backend Improvements

Redis

Celery

Docker

CI/CD

PostgreSQL

Alembic

Caching

Async Database

Microservices

---

# AI Assistant Instructions

When editing backend code

1. Never place business logic inside routes.

2. Reuse existing services.

3. Keep middleware lightweight.

4. Preserve JWT authentication.

5. Update schemas whenever models change.

6. Add tests for every endpoint.

7. Maintain RESTful API principles.

8. Preserve folder structure.

9. Explain breaking changes before implementing them.

10. Keep code production-ready.

---

# Backend Status

Authentication

Complete

Weather APIs

Complete

AQI APIs

Complete

Water APIs

Complete

Prediction APIs

Complete

Analytics

Complete

Reports

Complete

Testing

Operational

Middleware

Complete

Dependencies

Complete

Exceptions

Complete

WebSockets

Implemented

Deployment

In Progress

---

# Mission

Build a secure, scalable, enterprise-grade backend capable of powering AI-driven environmental intelligence, analytics, reporting, and real-time monitoring.
