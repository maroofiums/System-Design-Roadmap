# 📅 Day 6 - Query Optimization Basics (Iris Prediction API)

## 🎯 Goal

Make your ML API more efficient and scalable.

Right now:

```text
GET /history → returns everything
```

Problem:

* Slow when database grows
* Unnecessary memory usage
* Poor scalability

After today:

```text
GET /history?limit=10
GET /history?species=setosa
GET /history?start_date=2026-05-01
```

Your API now behaves more like a production backend.

---

# 📚 Concepts Covered

## 1. Filtering Queries

Instead of returning all rows:

```python
db.query(PredictionHistory).all()
```

Filter specific records:

```python
db.query(PredictionHistory).filter(
    PredictionHistory.prediction == "setosa"
)
```

Use case:

* Show only specific flower predictions
* Reduce unnecessary results

---

# 2. Limiting Results

Bad:

```python
.all()
```

This can return thousands of records.

Better:

```python
.limit(10)
```

Only fetch recent records.

---

# 3. Indexing Basics

Indexes help database search faster.

Without index:

* Database scans entire table

With index:

* Database finds data faster

Example:

```python
prediction = Column(String, index=True)
```

Best fields to index:

* prediction
* created_at

---

# 4. Avoid Heavy Queries

Bad:

```python
SELECT * FROM huge_table
```

Better:

* Fetch required rows only
* Use filters
* Use limits

---

# Updated `models.py`

Add indexes:

```python
from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from database import Base

class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)

    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)

    prediction = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
```

---

# Updated `/history` Endpoint

```python
from fastapi import FastAPI
from datetime import datetime

@app.get("/history")
def get_history(
    limit: int = 10,
    species: str = None,
    start_date: str = None
):

    db = SessionLocal()

    query = db.query(PredictionHistory)

    # Filter by species
    if species:
        query = query.filter(
            PredictionHistory.prediction == species
        )

    # Filter by date
    if start_date:
        parsed_date = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        )

        query = query.filter(
            PredictionHistory.created_at >= parsed_date
        )

    # Latest records first
    records = query.order_by(
        PredictionHistory.created_at.desc()
    ).limit(limit).all()

    history = []

    for record in records:
        history.append({
            "id": record.id,
            "prediction": record.prediction,
            "created_at": record.created_at
        })

    return {
        "total_records": len(history),
        "history": history
    }
```

---

# Example API Calls

---

## Get last 10 predictions

```text
GET /history
```

---

## Get last 5 predictions

```text
GET /history?limit=5
```

---

## Filter only Setosa predictions

```text
GET /history?species=setosa
```

---

## Filter by date

```text
GET /history?start_date=2026-05-01
```

---

## Combine filters

```text
GET /history?species=virginica&limit=3
```

---

# Why This Matters in Real Companies

Large applications may have:

* Millions of records
* Thousands of users
* Heavy traffic

Without optimization:

* Slow API responses
* Higher server costs
* Bad user experience

---

# 🧠 What You Learned

### Filtering

Fetch only relevant data

### Limit

Avoid huge responses

### Indexing

Speed up database searches

### Scalability

Prepare system for growth

---

# Before vs After

### Before

```text
GET /history → everything
```

### After

```text
GET /history?limit=10
GET /history?species=setosa
GET /history?start_date=2026-05-01
```

---

# ⚠️ Common Mistakes

* Using `.all()` everywhere
* Forgetting indexes
* Returning unnecessary columns
* No pagination/limits

---