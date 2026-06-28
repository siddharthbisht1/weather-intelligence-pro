import requests
from typing import Dict, Any, Optional

# ==========================================
# HTTP GET Request Helper
# ==========================================

def make_get_request(url: str, params: Optional[Dict[str, Any]] = None) -> Any:
    """
    Executes an HTTP GET request and returns the JSON response.
    Raises an exception for bad HTTP status codes (4xx or 5xx).
    """
    response = requests.get(url, params=params)
    
    # Safely throw an error if the API request fails
    response.raise_for_status()
    
    return response.json()