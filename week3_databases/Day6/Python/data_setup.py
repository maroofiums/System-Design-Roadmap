from sklearn.datasets import load_iris
import pandas as pd
import sqlite3

# Load dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["target"] = iris.target

# Connect DB
conn = sqlite3.connect("iris.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS iris (
    sepal_length REAL,
    sepal_width REAL,
    petal_length REAL,
    petal_width REAL,
    target INTEGER
)
""")

# Clear old data (important to avoid duplicates)
cursor.execute("DELETE FROM iris")

# Insert data
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO iris VALUES (?, ?, ?, ?, ?)
    """, tuple(row))

conn.commit()
conn.close()

print("✅ Data inserted into database successfully")