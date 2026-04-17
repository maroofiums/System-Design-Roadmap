# 🟢 WEEK 3 - Database Fundamentals (ML + Data Storage)

## 🎯 Weekly Goal

Understand how real systems store, retrieve, and use data for ML pipelines.

By the end you will:

* Understand SQL basics
* Query datasets properly
* Store ML datasets in a database
* Pull data back for training

---

# 🟢 DAY 1 - Database Basics + Setup

## 🎯 Goal

Understand what databases are + setup SQLite

---

## ✍️ Tasks

* Install SQLite (or use Python sqlite3)
* Create simple table

```python id="db1"
import sqlite3

conn = sqlite3.connect("ml_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    feature1 REAL,
    feature2 REAL,
    target INTEGER
)
""")

conn.commit()
conn.close()
```

---

## 🧠 Focus

* Understand table structure
* Think of ML dataset as table

---

## ✅ Output

* Database created
* Table exists

---

# 🟢 DAY 2 - SQL CRUD Operations

## 🎯 Goal

Learn basic data operations

---

## ✍️ Tasks

### Insert

```python id="db2"
cursor.execute("INSERT INTO data VALUES (1, 10.5, 20.3, 1)")
```

---

### Read

```python id="db3"
cursor.execute("SELECT * FROM data")
print(cursor.fetchall())
```

---

## 🧠 Focus

* Understand how data flows in/out of DB

---

## ✅ Output

* Can insert and retrieve data

---

# 🟢 DAY 3 - SQL Queries + Filtering

## 🎯 Goal

Learn SELECT logic

---

## ✍️ Tasks

```sql
SELECT * FROM data WHERE feature1 > 10;
```

---

## 🧠 Focus

* Filtering = selecting training data

---

## ✅ Output

* Can query subsets of data

---

# 🟢 DAY 4 - Primary Key + Structure Thinking

## 🎯 Goal

Understand data design

---

## ✍️ Tasks

* Modify table with IDs
* Understand uniqueness

---

## 🧠 Focus

> Every ML row must be uniquely identifiable

---

## ✅ Output

* Proper structured table

---

# 🟢 DAY 5 - Joins (Advanced Thinking)

## 🎯 Goal

Connect multiple tables

---

## Example:

Users + Transactions

---

## 🧠 Focus

> Real ML data often comes from multiple sources

---

## ✅ Output

* Simple join queries working

---

# 🟢 DAY 6 - ML + Database Integration

## 🎯 Goal

Load training data from SQL

---

## ✍️ Task

```python id="ml_sql"
import pandas as pd
import sqlite3

conn = sqlite3.connect("ml_data.db")

df = pd.read_sql_query("SELECT * FROM data", conn)

X = df.drop("target", axis=1)
y = df["target"]
```

---

## 🧠 Focus

> ML does NOT always start from CSV

---

## ✅ Output

* Data loaded from database into ML pipeline

---

# 🟢 DAY 7 - Final Project (ML + SQL System)

## 🎯 Goal

Complete pipeline

---

## System Flow:

1. Store data in SQL
2. Query data
3. Train ML model
4. Evaluate

---

## ✍️ Task Flow

```text
SQL → Pandas → ML Model → Evaluation
```

---

## 🧠 Final Insight

> This is how real companies work

---

# 🧠 WEEK 3 FINAL UNDERSTANDING

You now understand:

* Data storage layer (SQL)
* Query layer (SQL commands)
* ML layer (Python)
* Integration layer (pipeline)

---

# 🚀 WHAT YOU BUILT THIS WEEK

* SQL database
* CRUD system
* Query system
* ML dataset loader from DB
* Basic ML pipeline using SQL data
