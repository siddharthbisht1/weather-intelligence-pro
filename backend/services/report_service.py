# backend/services/report_service.py
import random
from datetime import datetime, timedelta

def fetch_report_dashboard_data():
    """
    Simulates fetching report generation metrics and history from the database.
    """
    # Simulate data for the last 6 months
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    trend_data = [random.randint(15, 90) for _ in range(6)]
    
    # Total sum of generated reports
    total_generated = sum(trend_data)

    # Mock list of recent reports
    recent_reports = [
        {"id": "REP-1042", "name": "Monthly AQI Summary", "format": "PDF", "date": "Today, 10:00 AM", "status": "Ready", "color": "#F87171"},
        {"id": "REP-1043", "name": "Weekly Weather Data", "format": "Excel", "date": "Yesterday, 2:30 PM", "status": "Ready", "color": "#4ADE80"},
        {"id": "REP-1044", "name": "Water Quality Analysis", "format": "CSV", "date": "02 Jul 2026", "status": "Processing", "color": "#38BDF8"},
        {"id": "REP-1045", "name": "AI Prediction Logs", "format": "JSON", "date": "01 Jul 2026", "status": "Ready", "color": "#A855F7"}
    ]

    return {
        "kpis": {
            "total_reports": total_generated,
            "pdf_count": int(total_generated * 0.45),
            "excel_count": int(total_generated * 0.35),
            "scheduled": random.randint(5, 12)
        },
        "chart": {
            "labels": months,
            "data": trend_data
        },
        "recent_reports": recent_reports
    }