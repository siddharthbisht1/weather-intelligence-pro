from fastapi import APIRouter, Depends, HTTPException
from backend.dependencies.auth_helper import require_auth # Your existing dependency
from backend.dependencies.roles import require_role # This new helper

router = APIRouter()

@router.get("/manager-dashboard")
def get_manager_data(username: str = Depends(require_auth)):
    # Let's assume you fetch user_role from your database first
    user_role = get_user_role_from_db(username) 
    
    # Use your new helper
    require_role(user_role, "manager")
    
    return {"message": "Welcome to the manager dashboard!"}