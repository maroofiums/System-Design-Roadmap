import pandas as pd
import sqlite3
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Create folder if not exist
os.makedirs("Model", exist_ok=True)

# Connect database
conn = sqlite3.connect("Database/iris.db")

# Load data from SQL
query = "SELECT * FROM iris"
df = pd.read_sql_query(query, conn)

conn.close()

# Split features and target
X = df.drop("target", axis=1)
y = df["target"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, pred)
print("Accuracy:", acc)

# Save model
with open("Model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully")
print("Saved at Model/model.pkl")