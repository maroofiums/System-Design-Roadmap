# 🟢 DAY 5 - Joins (Advanced Thinking)

## 🎯 Core Idea

> Real data is rarely stored in one table.

Instead, systems split data into multiple tables:

* Users
* Orders
* Transactions
* Products
* Logs

To combine them, we use **JOINS**.

---

# 🧠 Why Multiple Tables?

## Example:

### Users Table

| user_id | name | age |
| ------- | ---- | --- |
| 1       | Ali  | 22  |
| 2       | Sara | 25  |

---

### Orders Table

| order_id | user_id | amount |
| -------- | ------- | ------ |
| 101      | 1       | 500    |
| 102      | 2       | 900    |
| 103      | 1       | 200    |

---

## 🧠 Problem

If you want:

> Which user made which order?

Need both tables together.

---

# 🧠 Solution = JOIN

---

# 🟢 1. INNER JOIN

## SQL

```sql id="ij1"
SELECT users.name, orders.amount
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id;
```

---

## Result

| name | amount |
| ---- | ------ |
| Ali  | 500    |
| Sara | 900    |
| Ali  | 200    |

---

## Meaning

Only matching rows from both tables.

---

# 🧠 Think Like This

```text id="join1"
users.user_id = orders.user_id
```

Use common key to connect tables.

---

# 🟢 2. LEFT JOIN

## SQL

```sql id="lj1"
SELECT users.name, orders.amount
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id;
```

---

## Meaning

* Keep all users
* Add orders if available
* If no order → NULL

---

## Example

If Hamza has no orders:

| name  | amount |
| ----- | ------ |
| Ali   | 500    |
| Sara  | 900    |
| Hamza | NULL   |

---

# 🧠 Why This Matters for ML

Real ML datasets are built using joins.

---

## Example Fraud Detection

Need:

* User age (users table)
* Order amount (orders table)
* Payment type (payments table)

Use joins to combine.

---

## Example Customer Churn

Need:

* customer profile
* subscription history
* support tickets

All in separate tables.

---

# ⚙️ Python Example (SQLite)

```python id="pyjoin1"
import sqlite3

conn = sqlite3.connect("ml_data.db")
cursor = conn.cursor()

cursor.execute("""
SELECT users.name, orders.amount
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id
""")

rows = cursor.fetchall()

print(rows)

conn.close()
```

---

# 🧠 Important Join Types

| Join       | Meaning                                            |
| ---------- | -------------------------------------------------- |
| INNER JOIN | Only matching rows                                 |
| LEFT JOIN  | Keep all left table rows                           |
| RIGHT JOIN | Keep all right table rows (not in SQLite standard) |
| FULL JOIN  | Keep all rows from both                            |

---

# 🧠 Real Engineer Thinking

Instead of:

❌ Store everything in one giant table

Use:

✅ Normalized tables + joins when needed

Why?

* Cleaner design
* Less duplication
* Easier updates

---

# 🧠 ML Mindset

```text id="mljoin"
Multiple Tables → JOIN → Final Dataset → Train Model
```

---

# 🧠 Common Mistakes

## ❌ Joining wrong columns

```sql id="badjoin"
ON users.name = orders.amount
```

Wrong logic.

---

## ❌ Forgetting ON condition

Creates huge meaningless combinations.

---

# ✍️ Your Task

Create:

### users table

| user_id | name |

### orders table

| order_id | user_id | amount |

Then run:

```sql id="taskjoin"
SELECT users.name, orders.amount
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id;
```

---

# ✅ Output Checklist

After today you should:

* Understand why tables are separated
* Know common keys connect tables
* Use INNER JOIN
* Understand LEFT JOIN
* See how ML datasets are built from joins

---

# 🧠 Final Mindset Shift

Before:

❌ One table = enough

After:

✅ Real data lives in many tables, joins create intelligence

---
