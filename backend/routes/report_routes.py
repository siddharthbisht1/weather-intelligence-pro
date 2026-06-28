from fastapi import APIRouter, Depends
from pydantic import BaseModel

# Local Imports
from backend.dependencies.auth_helper import require_auth
from backend.exceptions.custom_exceptions import ReportNotFoundException
from backend.services.report_service import (
    get_all_reports,
    get_report_by_id,
    create_report,
    delete_report,
    export_report
)

# ==========================================
# Schemas (You can move this to schemas.py later)
# ==========================================
class ReportCreateRequest(BaseModel):
    report_name: str
    report_type: str

# ==========================================
# Router Setup
# ==========================================
# Adding `Depends(require_auth)` here secures EVERY route in this file
router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
    dependencies=[Depends(require_auth)] 
)

# ==========================================
# Endpoints
# ==========================================

@router.get("/")
def fetch_reports():
    return get_all_reports()

@router.get("/{report_id}")
def fetch_single_report(report_id: int):
    report = get_report_by_id(report_id)
    if not report:
        raise ReportNotFoundException() # Unified exception handling
    return report

@router.post("/")
def add_new_report(payload: ReportCreateRequest):
    # Payload is now securely passed as a JSON body
    return create_report(payload.report_name, payload.report_type)

@router.delete("/{report_id}")
def remove_report(report_id: int):
    result = delete_report(report_id)
    if not result:
        raise ReportNotFoundException()
    return result

@router.get("/{report_id}/export")
def trigger_report_export(report_id: int):
    result = export_report(report_id)
    # If the export fails because the report doesn't exist:
    if "error" in result:
        raise ReportNotFoundException()
    return result