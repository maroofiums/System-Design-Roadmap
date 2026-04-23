# 🟢 DAY 7 - Final Project (ML + SQL System)

## 🎯 Goal

Build a complete end-to-end machine learning pipeline using a database as the data source.

This is the point where all previous days connect into one real system.

---

## 🧠 Core Idea

Instead of loading CSV files manually:

```text
SQL Database → Query Data → Pandas → ML Model → Evaluation
```

This is how production systems are designed.

---

## 📁 Final Project Architecture

```text
📦 Day7
 ┣ 📂Database
 ┃ ┗ iris.db
 ┣ 📂Model
 ┃ ┗ model.pkl
 ┣ 📂Python
 ┃ ┣ data_setup.py
 ┃ ┗ train.py
 ┣ README.md
 ┗ requirements.txt
```

---

## ⚙️ Step 1 - Store Data in SQL

```python
from sklearn.datasets import load_iris
import pandas as pd
import sqlite3

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["target"] = iris.target

conn = sqlite3.connect("Database/iris.db")

df.to_sql("iris", conn, if_exists="replace", index=False)

conn.close()
```

### What happened:

* Dataset loaded from sklearn
* Converted into DataFrame
* Stored inside SQLite database

---

## ⚙️ Step 2 - Query Data from SQL

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("Database/iris.db")

query = "SELECT * FROM iris"

df = pd.read_sql_query(query, conn)

conn.close()
```

### Why this matters:

You can change SQL queries anytime to filter or select custom training data.

---

## ⚙️ Step 3 - Train ML Model

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)
```

---

## ⚙️ Step 4 - Evaluate Model

```python
from sklearn.metrics import accuracy_score

pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)

print("Accuracy:", acc)
```

---

## ⚙️ Step 5 - Save Model

```python
import pickle

with open("Model/model.pkl", "wb") as f:
    pickle.dump(model, f)
```

---

## 🧠 Full Pipeline Flow

```text
Iris Dataset
   ↓
SQLite Database
   ↓
SQL Query
   ↓
Pandas DataFrame
   ↓
Train/Test Split
   ↓
Random Forest Model
   ↓
Accuracy Evaluation
   ↓
Saved model.pkl
```

---

## 🧠 What You Learned This Week

### Database Skills

* SQLite basics
* CRUD operations
* SQL queries
* Filtering
* Joins

### ML Skills

* Loading data from database
* Model training
* Evaluation
* Saving models using pickle

### System Thinking

* Data storage layer
* Query layer
* ML training layer
* Deployment artifact layer

---

## 🧠 Final Insight

Real companies do not manually use CSV files every day.
They build systems where:

* Data flows automatically
* Models retrain from databases
* Predictions are served through APIs

---

## 🧠 Final Mindset Shift

Before:
ML = Notebook experiment

After:
ML = Connected production system

---
