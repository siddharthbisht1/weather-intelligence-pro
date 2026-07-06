# backend/services/workflow_service.py
import random
from datetime import datetime

def fetch_workflow_dashboard_data():
    """
    Simulates fetching automated triggers, execution logs, and pipeline success rates.
    """
    # Simulate execution times and success/failure logic
    executions = [
        {"name": "Daily Weather Summary", "duration": f"{round(random.uniform(1.2, 3.5), 1)} sec", "status": "Success", "color": "#4ADE80"},
        {"name": "AQI Alert Threshold", "duration": f"{round(random.uniform(0.5, 1.5), 1)} sec", "status": "Success", "color": "#4ADE80"},
        {"name": "Email Service Batch", "duration": f"{round(random.uniform(5.0, 9.5), 1)} sec", "status": random.choice(["Delayed", "Success"]), "color": "#FACC15"},
        {"name": "DB Auto-Backup", "duration": "12.4 sec", "status": "Success", "color": "#4ADE80"},
        {"name": "External API Sync", "duration": "Timeout", "status": "Failed", "color": "#F87171"}
    ]
    
    # Shuffle to make it look alive on refresh
    random.shuffle(executions)

    alerts = [
        {"msg": "Warning: AQI Threshold Triggered in Delhi", "color": "#FACC15", "bg": "rgba(250,204,21,0.1)", "border": "#FACC15"},
        {"msg": "Error: SendGrid Email API Timeout", "color": "#F87171", "bg": "rgba(248,113,113,0.1)", "border": "#F87171"},
        {"msg": "Success: Morning Forecast Batch Sent", "color": "#4ADE80", "bg": "rgba(74,222,128,0.1)", "border": "#4ADE80"}
    ]
    random.shuffle(alerts)

    return {
        "kpis": {
            "active_workflows": random.randint(20, 30),
            "emails_sent": random.randint(150, 500),
            "alerts_triggered": random.randint(40, 90),
            "success_rate": round(random.uniform(97.5, 99.9), 1)
        },
        "charts": {
            "success_trend": [round(random.uniform(95, 100), 1) for _ in range(7)],
            "trigger_distribution": [random.randint(300, 500), random.randint(100, 200), random.randint(50, 100), random.randint(80, 150), random.randint(20, 60)]
        },
        "recent_executions": executions[:4], # Send top 4
        "recent_alerts": alerts[:2] # Send top 2
    }