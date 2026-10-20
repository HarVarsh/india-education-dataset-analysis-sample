
import sqlite3
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DB_PATH = PROJECT_DIR / "database" / "education_analysis.db"
QUERY_DIR = PROJECT_DIR / "queries"


def load_sql(query_name):
    """Read a saved SQL query from the queries folder."""
    sql_path = QUERY_DIR / query_name

    if not sql_path.is_file():
        raise FileNotFoundError(
            f"SQL file not found: {sql_path}"
        )

    return sql_path.read_text(encoding="utf-8")


def run_query(query_name, params=()):
    """Execute a saved SELECT query and return a DataFrame."""
    if not DB_PATH.is_file():
        raise FileNotFoundError(
            f"Database not found: {DB_PATH}"
        )

    sql = load_sql(query_name)

    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(
            sql,
            conn,
            params=params
        )
