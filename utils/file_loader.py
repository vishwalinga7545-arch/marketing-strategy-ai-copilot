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

def summarize_dataframe(df):
    """
    Convert dataframe into a text summary for LLM analysis
    """
    summary = []

    summary.append(f"Total rows: {df.shape[0]}")
    summary.append(f"Total columns: {df.shape[1]}")
    summary.append(f"Columns: {list(df.columns)}")

    summary.append("\nSample data:")
    summary.append(df.head(5).to_string())

    return "\n".join(summary)
