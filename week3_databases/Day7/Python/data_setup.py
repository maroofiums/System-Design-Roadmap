from sklearn.datasets import load_iris
import pandas as pd
import sqlite3
import os

# Create folders if not exist
os.makedirs("Database", exist_ok=True)

# Load Iris dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["target"] = iris.target

# Connect to database
conn = sqlite3.connect("Database/iris.db")

# Save to SQL table
df.to_sql("iris", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully")
print("Iris dataset stored in Database/iris.db")