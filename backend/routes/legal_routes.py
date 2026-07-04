# backend/routes/legal_routes.py
from fastapi import APIRouter
from backend.services.legal_service import fetch_privacy_policy

router = APIRouter(
    prefix="/legal",
    tags=["Legal & Compliance"]
)

@router.get("/privacy-policy")
def get_privacy_policy():
    """
    BFF Endpoint to fetch the latest Privacy Policy content for the frontend.
    """
    return fetch_privacy_policy()