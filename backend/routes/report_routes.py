# backend/routes/report_routes.py
from fastapi import APIRouter
from backend.services.report_service import fetch_report_dashboard_data

router = APIRouter(
    prefix="/reports",
    tags=["Reports Hub"]
)

@router.get("/dashboard-data")
def get_dashboard_data():
    """
    BFF Endpoint to fetch metrics and trends for the Reports Dashboard.
    """
    return fetch_report_dashboard_data()