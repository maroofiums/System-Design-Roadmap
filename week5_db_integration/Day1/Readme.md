# 📅 Day 1 - ORM Foundations

## 🎯 Goal

Understand how Python interacts with a database using ORM (Object Relational Mapping) without writing raw SQL.

---

## 📚 Concepts Covered

### 1. What is ORM?

ORM (Object Relational Mapping) allows you to interact with a database using Python classes instead of SQL queries.

**Mapping:**

```
Python Class  →  Database Table
Object        →  Row
Attribute     →  Column
```

---

### 2. Why Use ORM Instead of SQL?

| Without ORM (SQL)   | With ORM (Python)    |
| ------------------- | -------------------- |
| INSERT INTO table   | session.add(obj)     |
| SELECT * FROM table | session.query(Model) |

**Benefits:**

* Cleaner code
* Less error-prone
* Easier integration with APIs (FastAPI)
* Scalable for large systems

---

### 3. SQLAlchemy Core Components

* **Engine** → Connects to the database
* **Base** → Parent class for models
* **Model** → Represents table structure
* **Session** → Handles database operations

---

## 🛠️ What You Built

### Step 1 - Install Dependency

```bash
pip install sqlalchemy
```

---

### Step 2 - Database Setup

```python
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)
```

---

### Step 3 - Base Class

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

---

### Step 4 - Create Model (Table)

```python
from sqlalchemy import Column, Integer, Float

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float)
```

---

### Step 5 - Create Table

```python
Base.metadata.create_all(bind=engine)
```

---

### Step 6 - Session Setup

```python
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
```

---

### Step 7 - Insert Data

```python
new_prediction = Prediction(value=0.85)
session.add(new_prediction)
session.commit()
```

---

### Step 8 - Read Data

```python
data = session.query(Prediction).all()

for row in data:
    print(row.id, row.value)
```

---

## 🧠 Final Understanding

```
Python Class → SQLAlchemy → Database
       ↓
     Session
       ↓
 Insert / Query Data
```

---

## ⚠️ Common Mistakes

* Forgetting `session.commit()`
* Not running `create_all()` (table won’t exist)
* Confusing engine vs session
* Trying to mix raw SQL with ORM (avoid for now)

---
