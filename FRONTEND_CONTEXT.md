# FRONTEND_CONTEXT.md

# Weather Intelligence Pro - Frontend Context

## Overview

The frontend is an enterprise-grade administrative dashboard built using HTML, CSS, and JavaScript.

It communicates with the FastAPI backend using REST APIs secured with JWT Bearer Authentication.

The design follows a modern glassmorphism theme with dark mode styling inspired by enterprise platforms such as Azure Portal, AWS Console, Datadog, and Grafana.

---

# Technology Stack

Frontend

* HTML5
* CSS3
* JavaScript (Vanilla)
* Chart.js
* Font Awesome
* Google Fonts (Poppins)

Backend Integration

* FastAPI
* JWT Authentication
* REST APIs
* JSON

---

# Folder Structure

frontend/

├── admin/

│

├── assets/

│ ├── css/

│ ├── js/

│ ├── images/

│ └── icons/

│

├── index.html

└── login.html

---

# Admin Pages

Current Pages

master-dashboard.html

deployment-center.html

user-tracking-center.html

reports-command.html

data-governance-center.html

data-quality-center.html

satellite-command.html

cybersecurity-command-center.html

compliance-center.html

cloud-command-center.html

analytics.html

alert-center.html

computer-vision-center.html

cost-optimization-center.html

customer-support-center.html

api-management-center.html

admin-login.html

---

# Master Dashboard

Purpose

Main control center for the entire Weather Intelligence Pro platform.

Contains

System Health

Live Traffic

Weather Queries

Charts

API Statistics

Navigation Sidebar

Sync Live Data Button

---

# Deployment Center

Purpose

Monitor deployment status.

Displays

Deployment progress

Server status

Environment information

Release version

Container health

---

# User Tracking Center

Purpose

Track user activities.

Displays

Active Users

Search History

Authentication Logs

Failed Login Attempts

Recent Activities

Export Logs

---

# Reports Command

Purpose

Generate and download reports.

Supported

PDF

Excel

CSV

Weather Reports

AQI Reports

Analytics Reports

---

# Data Governance Center

Purpose

Manage datasets.

Features

Dataset Overview

Data Integrity

Storage Statistics

Access Logs

Compliance Status

---

# Data Quality Center

Purpose

Monitor environmental data quality.

Displays

Missing Values

Validation Score

Duplicate Detection

Sensor Health

---

# Satellite Command

Purpose

Satellite monitoring dashboard.

Displays

Satellite Status

Image Feed

Cloud Coverage

Rainfall Monitoring

---

# Cybersecurity Command Center

Purpose

Security Operations Center (SOC).

Features

Attack Dashboard

Firewall Logs

Threat Intelligence

Security Incidents

Authentication Events

WAF Monitoring

SSL Status

---

# Compliance Center

Purpose

Compliance monitoring.

Supports

ISO

SOC

GDPR

Internal Policies

Audit Logs

---

# Cloud Command Center

Purpose

Cloud infrastructure management.

Displays

CPU Usage

RAM Usage

Network Traffic

Cloud Health

Node Status

Cluster Status

---

# Analytics Dashboard

Purpose

Business Intelligence dashboard.

Displays

Charts

API Usage

Monthly Growth

Weather Trends

AQI Trends

---

# Alert Center

Purpose

Incident management.

Displays

Critical Alerts

Warnings

Notifications

Resolved Incidents

---

# Computer Vision Center

Purpose

Future AI image analysis.

Planned

Satellite Detection

Flood Mapping

Wildfire Detection

Storm Detection

---

# Cost Optimization Center

Purpose

Cloud cost monitoring.

Displays

Infrastructure Cost

Storage Usage

Monthly Budget

Forecasted Cost

Savings

---

# Customer Support Center

Purpose

Helpdesk dashboard.

Displays

Support Tickets

Response Time

Customer Satisfaction

Pending Issues

---

# API Management Center

Purpose

Monitor APIs.

Displays

API Health

Latency

Request Count

Error Rate

Authentication Logs

---

# Navigation

Every page includes

Sidebar

Header

Logout Button

Responsive Layout

Consistent Navigation

Users should be able to navigate between every admin page without page reload issues.

---

# Authentication

Login Page

admin-login.html

Workflow

User Login

↓

Receive JWT

↓

Store Token

↓

Access Dashboard

↓

Call Protected APIs

Logout clears

localStorage

sessionStorage

Authorization headers

---

# API Integration

Each page communicates with FastAPI.

Example

Weather

GET /weather/history

AQI

GET /aqi/history

Analytics

GET /analytics/dashboard

Reports

GET /reports/pdf

Authentication

POST /auth/login

Always send

Authorization

Bearer Token

---

# Charts

Library

Chart.js

Used For

Traffic

Weather

AQI

Analytics

Threat Monitoring

Cloud Usage

Charts should update dynamically using backend responses.

---

# Styling Guidelines

Theme

Dark

Primary Colors

Blue

Purple

Cyan

Accent Colors

Green

Yellow

Red

Typography

Poppins

Cards

Glassmorphism

Rounded Corners

Soft Shadows

Blur Effects

---

# Responsive Design

Support

Desktop

Laptop

Tablet

Minimum Width

1024px

Future

Mobile Responsive

---

# JavaScript Responsibilities

Authentication

API Calls

Token Storage

Charts

Dynamic Tables

Export Buttons

Notifications

Auto Refresh

Logout

Avoid embedding business logic inside HTML.

Keep JavaScript modular.

---

# Security

Never expose

Passwords

Secrets

API Keys

JWT Secret

Validate JWT before every protected request.

Handle expired tokens gracefully.

---

# Future Improvements

React Migration

Tailwind Components

Dark/Light Theme

Real-Time WebSockets

Interactive Maps

3D Globe

Satellite Visualization

AI Chat Assistant

Voice Commands

Multi-language Support

---

# Design Principles

Consistency

Minimalism

Enterprise UX

Fast Loading

High Contrast

Reusable Components

Scalable Layout

---

# AI Assistant Instructions

When modifying the frontend

1. Preserve the existing UI theme.

2. Do not redesign completed pages unless requested.

3. Keep navigation consistent.

4. Maintain glassmorphism styling.

5. Use reusable CSS classes.

6. Avoid inline styling when possible.

7. Keep JavaScript modular.

8. Every new page must match the existing design system.

9. Connect UI components to FastAPI endpoints whenever available.

10. Maintain responsive layouts.

---

# Current Frontend Status

Admin Login

Complete

Master Dashboard

Complete

Cloud Command

Complete

Cybersecurity Center

Complete

Compliance Center

Complete

Deployment Center

Complete

User Tracking

Complete

Reports

Complete

Analytics

Complete

API Management

Complete

Customer Support

Complete

Cost Optimization

Complete

Computer Vision

Complete

Satellite Command

Complete

Alert Center

Complete

Backend Integration

In Progress

Authentication

Complete

UI Theme

Complete

Responsive Design

Partial

---

# Mission

Provide a modern enterprise command center for monitoring weather intelligence, AI predictions, cloud infrastructure, security operations, analytics, and environmental data through a unified administrative dashboard.
