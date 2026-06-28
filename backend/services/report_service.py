from datetime import datetime

# ==========================================
# Temporary Report Storage
# ==========================================

reports = [
    {
        "id": 1,
        "report_name": "Delhi Weather Report",
        "report_type": "PDF",
        "created_at": datetime.now()
    },
    {
        "id": 2,
        "report_name": "AQI Analysis Report",
        "report_type": "Excel",
        "created_at": datetime.now()
    }
]


# ==========================================
# Get All Reports
# ==========================================

def get_all_reports():
    return reports


# ==========================================
# Get Report By ID
# ==========================================

def get_report_by_id(report_id: int):
    for report in reports:
        if report["id"] == report_id:
            return report
    return None


# ==========================================
# Create Report
# ==========================================

def create_report(report_name: str, report_type: str):
    new_report = {
        "id": len(reports) + 1,
        "report_name": report_name,
        "report_type": report_type,
        "created_at": datetime.now()
    }
    reports.append(new_report)
    return new_report


# ==========================================
# Delete Report
# ==========================================

def delete_report(report_id: int):
    global reports
    initial_length = len(reports)
    
    reports = [
        report
        for report in reports
        if report["id"] != report_id
    ]
    
    # Check if the report was actually found and deleted
    if len(reports) == initial_length:
        return None

    return {
        "message": "Report deleted successfully"
    }


# ==========================================
# Export Report
# ==========================================

def export_report(report_id: int):
    report = get_report_by_id(report_id)

    if report is None:
        return {
            "error": "Report not found"
        }

    return {
        "message": "Report exported successfully",
        "report": report
    }