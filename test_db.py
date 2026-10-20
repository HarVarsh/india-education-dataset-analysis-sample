
import sqlite3
from pathlib import Path

# Find the database relative to this Python file.
PROJECT_DIR = Path(__file__).resolve().parent
DB_PATH = PROJECT_DIR / "database" / "education_analysis.db"

print("Database path:", DB_PATH)

if not DB_PATH.exists():
    raise FileNotFoundError(
        f"Database not found: {DB_PATH}"
    )

with sqlite3.connect(DB_PATH) as conn:
    tables = conn.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        ORDER BY name;
    """).fetchall()

    print("Tables in database:")
    for table in tables:
        print(table[0])
