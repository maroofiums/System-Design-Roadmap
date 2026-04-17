# 🟢 DAY 1 - Database Basics + Setup

## 🎯 Goal
Understand what databases are + setup SQLite and create your first structured ML table.

---

## 🧠 Core Idea
A database is a **structured memory system for your data**.
Instead of storing messy CSV files, we store data in organized tables that can be queried and reused easily.

---

## 🧠 Concept Mapping (ML Perspective)

| Database Concept | ML Equivalent |
|------------------|--------------|
| Database         | Dataset storage system |
| Table            | Dataset |
| Row              | One training sample |
| Column           | Feature or label |
| SQL              | Language to access data |

---

## ✍️ Task — Create SQLite Database

```python
import sqlite3

# Step 1: Connect to database (creates file if not exists)
conn = sqlite3.connect("ml_data.db")
cursor = conn.cursor()

# Step 2: Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    feature1 REAL,
    feature2 REAL,
    target INTEGER
)
""")

# Step 3: Save changes
conn.commit()

# Step 4: Close connection
conn.close()
```

---

## 🧠 Code Breakdown

### 🔹 1. Connection
```python
conn = sqlite3.connect("ml_data.db")
```
Creates a database file or opens existing one.

---

### 🔹 2. Cursor
```python
cursor = conn.cursor()
```
Used to execute SQL commands.

Think of it as a "command executor" for the database.

---

### 🔹 3. Table Creation
```sql
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    feature1 REAL,
    feature2 REAL,
    target INTEGER
)
```
Defines structure of your dataset.

---

### 🔹 4. Commit
```python
conn.commit()
```
Saves changes permanently to the database.

---

### 🔹 5. Close Connection
```python
conn.close()
```
Frees system resources.

---

## 🧠 What You Built

- A SQLite database file (`ml_data.db`)
- A structured table called `data`
- A schema for ML dataset storage

---

## 🧠 Why This Matters for ML

In real systems:
- Data does NOT come from random CSVs
- It comes from databases
- ML pipelines pull data using queries

---

## 🧠 Key Insight
> Database = persistent memory for machine learning data

---

## 🧠 Output Checklist

After running this code, you should have:

- [ ] `ml_data.db` file created
- [ ] Table `data` exists inside it
- [ ] No errors during execution

---

## 🧠 Final Understanding

After this lesson, you should think:

> "I can now design structured storage for ML datasets instead of relying only on CSV files."

---