
from database_utils import run_query

summary = run_query("Query1.sql")
print("Query1")
print(summary)

comparison = run_query("Query2.sql")
print("\nQuery2")
print(comparison)

missing = run_query("Query3.sql")
print("\nQuery3")
print(missing)
