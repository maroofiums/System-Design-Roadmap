# 🟢 DAY 2 - SQL CRUD Operations (Deep Understanding)

## 🎯 Core Idea

CRUD means:

| Letter | Meaning |
| ------ | ------- |
| C      | Create  |
| R      | Read    |
| U      | Update  |
| D      | Delete  |

> Every real app and ML system uses CRUD.

Examples:

* User signup → Create
* Dashboard view → Read
* Edit profile → Update
* Remove record → Delete

---

# 🧠 Why This Matters for ML

Your training data must:

* be inserted
* be queried
* be corrected
* be removed if wrong

So CRUD = managing datasets.

---

# ⚙️ Full Setup First

```python id="setupcrud"
import sqlite3

conn = sqlite3.connect("ml_data.db")
cursor = conn.cursor()
```

---

# 🟢 1. CREATE (Insert Data)

## ✍️ Task

```python id="insert1"
cursor.execute(
    "INSERT INTO data VALUES (1, 10.5, 20.3, 1)"
)

conn.commit()
```

---

## 🧠 What Happened?

You added one row:

| id | feature1 | feature2 | target |
| -- | -------- | -------- | ------ |
| 1  | 10.5     | 20.3     | 1      |

---

## 🧠 Insight

> Insert = adding one training sample

---

# 🟢 2. READ (Get Data)

## ✍️ Task

```python id="read1"
cursor.execute("SELECT * FROM data")

rows = cursor.fetchall()

print(rows)
```

---

## Example Output

```python id="readout"
[(1, 10.5, 20.3, 1)]
```

---

## 🧠 Meaning

You retrieved all rows from table.

---

## SQL Breakdown

```sql id="sqlsel"
SELECT * FROM data
```

* SELECT = choose data
* * = all columns
* FROM = from table

---

# 🟢 3. UPDATE (Modify Existing Data)

## ✍️ Example

```python id="upd1"
cursor.execute("""
UPDATE data
SET feature1 = 99.9
WHERE id = 1
""")

conn.commit()
```

---

## Meaning

Change row with id=1

---

# 🟢 4. DELETE (Remove Data)

## ✍️ Example

```python id="del1"
cursor.execute("""
DELETE FROM data
WHERE id = 1
""")

conn.commit()
```

---

## Meaning

Remove one sample from dataset.

---

# 🧠 Focus - Data Flow Thinking

Think like this:

```text id="flowcrud"
Python App → SQL Command → Database → Result Back to Python
```

---

# 🧠 Example

```python id="flow2"
cursor.execute("SELECT * FROM data")
rows = cursor.fetchall()
```

Means:

1. Python asks DB
2. DB searches rows
3. Sends rows back

---

# 🧠 Real ML Example

You may later do:

```python id="mlquery"
SELECT * FROM data WHERE target = 1
```

Use only positive class samples.

---

# 🧠 Common Beginner Mistakes

## ❌ Forgetting commit()

Then inserts/updates may not save.

---

## ❌ No WHERE in update/delete

```sql id="badupd"
DELETE FROM data
```

Deletes everything.

---

# 🧠 Best Practice (Important)

Use parameterized queries:

```python id="safeq"
cursor.execute(
    "INSERT INTO data VALUES (?, ?, ?, ?)",
    (2, 5.1, 7.3, 0)
)
```

Safer and cleaner.

---

# ✅ Output Checklist

After today, you should be able to:

* Insert records
* Read records
* Update records
* Delete records
* Understand DB ↔ Python flow

---

# 🧠 Final Mindset Shift

Before:

❌ Database is static storage

After:

✅ Database is a living system that your code controls

---

# 🚀 Practice Challenge

Do this yourself:

1. Insert 3 rows
2. Read all rows
3. Update one row
4. Delete one row
5. Read again

---