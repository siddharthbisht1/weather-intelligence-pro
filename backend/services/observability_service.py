# backend/services/observability_service.py
import random
from datetime import datetime, timedelta

def fetch_system_metrics():
    """
    Generates real-time system observability metrics for the dashboard.
    """
    now = datetime.now()
    
    # Generate dynamic log timestamps
    def get_time(minutes_ago):
        return (now - timedelta(minutes=minutes_ago)).strftime("[%H:%M:%S]")

    return {
        "kpis": {
            "uptime": "99.99%",
            "active_services": random.randint(22, 26),
            "response_time": f"{random.randint(90, 180)}ms",
            "requests_hr": f"{random.randint(80, 95)}K",
            "data_processed": f"{random.uniform(2.5, 3.2):.1f} TB",
            "ai_accuracy": f"{random.uniform(92.0, 96.5):.1f}%"
        },
        "charts": {
            # 7 data points for the line/bar charts
            "cpu": [random.randint(30, 60) for _ in range(7)],
            "memory": [random.randint(50, 80) for _ in range(7)],
            "network": [random.randint(10, 40) for _ in range(7)],
            "api": [random.randint(100, 250) for _ in range(7)]
        },
        "services_status": [
            {"name": "Weather API", "icon": "fa-cloud", "color": "#4ADE80", "status": "Operational", "uptime": "99.9%"},
            {"name": "AQI Service", "icon": "fa-wind", "color": "#4ADE80", "status": "Operational", "uptime": "100%"},
            {"name": "Database", "icon": "fa-database", "color": "#FACC15", "status": "High Load", "uptime": "98.5%"}
        ],
        "resource_table": [
            {"name": "Weather API", "cpu": f"{random.randint(20, 40)}%", "mem": f"{random.randint(30, 50)}%", "status": "Healthy", "color": "#4ADE80"},
            {"name": "Prediction Engine", "cpu": f"{random.randint(60, 85)}%", "mem": f"{random.randint(60, 80)}%", "status": "High Load", "color": "#FACC15"},
            {"name": "Database cluster-1", "cpu": f"{random.randint(70, 95)}%", "mem": f"{random.randint(80, 95)}%", "status": "Warning", "color": "#F87171"}
        ],
        "alerts": [
            {"level": "danger", "icon": "fa-circle-exclamation", "color": "#F87171", "bg": "rgba(248,113,113,0.1)", "msg": f"Database CPU spiked to {random.randint(85, 95)}%."},
            {"level": "warning", "icon": "fa-cloud-rain", "color": "#FACC15", "bg": "rgba(250,204,21,0.1)", "msg": "API rate limit approaching for Weather endpoint."},
            {"level": "success", "icon": "fa-circle-check", "color": "#4ADE80", "bg": "rgba(74,222,128,0.1)", "msg": "Prediction engine cache cleared successfully."}
        ],
        "logs": [
            {"time": get_time(1), "level": "INFO", "color": "#4ADE80", "msg": "Weather API responded successfully."},
            {"time": get_time(3), "level": "WARN", "color": "#FACC15", "msg": "High memory consumption detected in AI node."},
            {"time": get_time(5), "level": "ERROR", "color": "#F87171", "msg": "Failed to sync external AQI provider."},
            {"time": get_time(7), "level": "INFO", "color": "#4ADE80", "msg": "System backup completed."}
        ],
        "realtime": {
            "current_cpu": f"{random.randint(40, 70)}%",
            "requests_min": random.randint(1200, 1600),
            "active_sensors": random.randint(55, 60)
        }
    }