# 📅 Day 2 - CRUD Operations

## 🎯 Goal

Learn how to interact with a database (core backend skill)

---

## 📚 Concepts Covered

### 1. What is CRUD?

CRUD = basic database operations used in almost every backend system.

* **C → Create** → Insert new data
* **R → Read** → Fetch existing data
* **U → Update** → Modify existing data
* **D → Delete** → Remove data

---

## Example:

```sql
INSERT → Create
SELECT → Read
UPDATE → Update
DELETE → Delete
```

With SQLAlchemy:

```python
session.add()
session.query()
session.commit()
session.delete()
```

---

## 2. SQLAlchemy Sessions

A session is used to communicate with the database.

```python
session = SessionLocal()
```

It helps you:

* Insert records
* Query records
* Update records
* Delete records

Think of session as:

```python
Python ↔ Session ↔ Database
```

---

## 3. Insert vs Query

### Insert

Adding new record into database

```python
new_prediction = Prediction(value=0.92)
session.add(new_prediction)
session.commit()
```

---

### Query

Reading existing records

```python
data = session.query(Prediction).all()
```

---

# 🛠️ Full Practical Code

```python
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Table model
class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float)

# Create table
Base.metadata.create_all(bind=engine)

# Session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# -------------------
# CREATE
# -------------------
def create_prediction(value):
    new_prediction = Prediction(value=value)
    session.add(new_prediction)
    session.commit()
    print("Data inserted successfully")

# -------------------
# READ
# -------------------
def read_predictions():
    data = session.query(Prediction).all()

    print("\nAll Predictions:")
    for row in data:
        print(f"ID: {row.id}, Value: {row.value}")

# -------------------
# UPDATE
# -------------------
def update_prediction(record_id, new_value):
    record = session.query(Prediction).filter(
        Prediction.id == record_id
    ).first()

    if record:
        record.value = new_value
        session.commit()
        print("Data updated successfully")
    else:
        print("Record not found")

# -------------------
# DELETE
# -------------------
def delete_prediction(record_id):
    record = session.query(Prediction).filter(
        Prediction.id == record_id
    ).first()

    if record:
        session.delete(record)
        session.commit()
        print("Data deleted successfully")
    else:
        print("Record not found")

# -------------------
# FILTERING
# -------------------
def filter_predictions():
    data = session.query(Prediction).filter(
        Prediction.value > 0.8
    ).all()

    print("\nFiltered Predictions:")
    for row in data:
        print(row.id, row.value)

# Run
if __name__ == "__main__":
    create_prediction(0.95)
    create_prediction(0.72)

    read_predictions()

    update_prediction(1, 0.99)

    filter_predictions()

    delete_prediction(2)

    read_predictions()
```

---

# 🔍 What You Learned

### Create

Insert new prediction

### Read

Fetch all predictions

### Update

Modify existing record

### Delete

Remove record

### Filter

Retrieve specific records

---

# 🧠 Database Flow

```id="9xcz7m"
Client → API → Session → Database
                ↑
         CRUD Operations
```

---

# ⚠️ Common Mistakes

* Forgetting `commit()` after update/delete
* Using `.all()` when only one record needed
* Forgetting filters
* Not handling missing records

---