import os

# ==========================================
# Create Folder
# ==========================================

def create_folder(path: str):
    """
    Creates a directory if it does not already exist.
    """
    os.makedirs(path, exist_ok=True)


# ==========================================
# Check File Exists
# ==========================================

def file_exists(path: str) -> bool:
    """
    Checks if a file or directory exists at the given path.
    """
    return os.path.exists(path)