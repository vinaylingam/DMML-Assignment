import sqlite3
import pandas as pd

conn = sqlite3.connect("feature_store.db")

# Read first 5 rows
df_check = pd.read_sql("SELECT * FROM feature_store LIMIT 5;", conn)
print(df_check)

conn.close()
