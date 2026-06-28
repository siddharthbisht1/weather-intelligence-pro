import pandas as pd

# ==========================================
# Excel Export Helper
# ==========================================

def save_dataframe(df: pd.DataFrame, filename: str) -> bool:
    """
    Saves a Pandas DataFrame to an Excel file, omitting the index column.
    """
    df.to_excel(filename, index=False)
    
    return True