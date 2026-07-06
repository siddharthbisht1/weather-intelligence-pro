# backend/routes/workflow_routes.py
from fastapi import APIRouter, HTTPException
from backend.services.workflow_service import fetch_workflow_dashboard_data

router = APIRouter(
    prefix="/workflow",
    tags=["Workflow Automation"]
)

@router.get("/dashboard-data")
def get_workflow_data():
    """
    BFF Endpoint to fetch workflow execution metrics and logs.
    """
    try:
        return fetch_workflow_dashboard_data()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))