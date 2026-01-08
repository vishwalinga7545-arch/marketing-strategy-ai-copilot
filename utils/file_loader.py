import pandas as pd

def load_marketing_file(uploaded_file):
    """
    Safely load CSV or Excel marketing files with encoding fallback
    """
    try:
        if uploaded_file.name.endswith(".csv"):
            try:
                # Try UTF-8 first
                return pd.read_csv(uploaded_file)
            except UnicodeDecodeError:
                # Fallback for Excel/Windows CSV files
                return pd.read_csv(uploaded_file, encoding="latin1")

        # Excel files
        return pd.read_excel(uploaded_file)

    except Exception as e:
        raise ValueError(f"Error loading file: {e}")
