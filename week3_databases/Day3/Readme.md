# 🟢 DAY 3 - SQL Queries + Filtering (Deep Understanding)

## 🎯 Core Idea

> Not all stored data should be used every time.

You often need:

* only some rows
* only certain columns
* only clean samples
* only a target class

That is called **querying + filtering**

---

# 🧠 What is SELECT?

`SELECT` means:

> Retrieve data from table

---

## Basic Form

```sql
SELECT column_name FROM table_name;
```

---

## Your Example

```sql
SELECT * FROM data WHERE feature1 > 10;
```

---

# 🧠 SQL Breakdown

| Part          | Meaning               |
| ------------- | --------------------- |
| SELECT        | choose data           |
| *             | all columns           |
| FROM data     | from table named data |
| WHERE         | apply condition       |
| feature1 > 10 | keep matching rows    |

---

# 🧠 What It Means in Plain English

> Give me all rows where `feature1` is greater than 10

---

# 📊 Example Table

| id | feature1 | feature2 | target |
| -- | -------- | -------- | ------ |
| 1  | 5.0      | 2.1      | 0      |
| 2  | 15.2     | 3.8      | 1      |
| 3  | 22.0     | 7.1      | 1      |

---

## Query Result

```sql
SELECT * FROM data WHERE feature1 > 10;
```

Returns:

| id | feature1 | feature2 | target |
| -- | -------- | -------- | ------ |
| 2  | 15.2     | 3.8      | 1      |
| 3  | 22.0     | 7.1      | 1      |

---

# 🧠 Why This Matters for ML

You may need:

## Only valid rows

```sql
SELECT * FROM data WHERE feature1 IS NOT NULL;
```

---

## Only one class

```sql
SELECT * FROM data WHERE target = 1;
```

---

## High-value users / samples

```sql
SELECT * FROM data WHERE salary > 50000;
```

---

# ⚙️ Python Version

```python
import sqlite3

conn = sqlite3.connect("ml_data.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM data
WHERE feature1 > 10
""")

rows = cursor.fetchall()

print(rows)

conn.close()
```

---

# 🧠 Important Filtering Operators

| Operator | Meaning       |
| -------- | ------------- |
| =        | equal         |
| >        | greater than  |
| <        | less than     |
| >=       | greater/equal |
| <=       | less/equal    |
| !=       | not equal     |

---

# 🧠 More Useful Examples

## Exact match

```sql
SELECT * FROM data WHERE target = 1;
```

---

## Range filtering

```sql
SELECT * FROM data WHERE feature1 > 10 AND feature1 < 50;
```

---

## Multiple conditions

```sql
SELECT * FROM data WHERE target = 1 AND feature2 > 20;
```

---

# 🧠 Real Engineer Thinking

Instead of:

❌ Load all data then filter in Python

Use:

✅ Filter inside SQL first

Why?

* Faster
* Cleaner
* Less memory usage

---

# 🧠 ML Mindset

```text
Raw Database → SQL Filtering → Clean Subset → Train Model
```

---

# 🧠 Common Mistakes

## ❌ Pulling everything unnecessarily

```sql
SELECT * FROM huge_table;
```

Then filtering later.

---

## ❌ Wrong conditions

```sql
WHERE feature1 > "10"
```

Use numeric values properly.

---

# ✅ Output Checklist

After today, you should be able to:

* Use SELECT
* Use WHERE
* Filter rows by conditions
* Query subsets for ML training

---

# 🧠 Final Mindset Shift

Before:

❌ Database stores data

After:

✅ Database answers smart questions about data

---

# 🚀 Practice Challenge

Write queries for:

1. Rows where target = 0
2. Rows where feature2 > 5
3. Rows where feature1 between 10 and 30
4. Rows where target = 1 and feature1 > 20

---