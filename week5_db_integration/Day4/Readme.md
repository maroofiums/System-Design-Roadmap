# 📅 Day 4 - Store Predictions in Database

## 🎯 Goal

Make your ML API persistent by storing every prediction request in a database.

Without a database:

```text
User → API → Prediction → Response
```

After today:

```text
User → API → Prediction → Database → Response
```

This is how real-world ML systems work.

---

# 📚 Concepts Covered

## 1. Combining API + Database

Now we combine:

* FastAPI → handles requests
* ML Model → makes predictions
* SQLAlchemy → stores results
* SQLite → saves data permanently

---

## 2. Data Flow After Prediction

New flow:

```text
User Input
    ↓
FastAPI Endpoint
    ↓
Pydantic Validation
    ↓
ML Model Prediction
    ↓
Store Result in DB
    ↓
Return Response
```

---

# What We Store

For every prediction request:

* user input
* model prediction
* timestamp

Example:

| id | area | bedrooms | prediction | created_at |
| -- | ---- | -------- | ---------- | ---------- |
| 1  | 1800 | 3        | 360000     | timestamp  |

---

# 🛠️ Project Structure

```text
project/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── iris_model.pkl
│
|── requirements.txt
└── Readme.md
```

---

# Step 1 - database.py

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./predictions.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
```

---

# Step 2 - models.py

```python
from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from database import Base

class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)
    area = Column(Float)
    bedrooms = Column(Integer)
    prediction = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
```

---

# Step 3 - schemas.py

```python
from pydantic import BaseModel

class HouseInput(BaseModel):
    area: float
    bedrooms: int
```

---

# Step 4 - main.py

```python
from fastapi import FastAPI
import pickle
import numpy as np

from database import SessionLocal, engine, Base
from models import PredictionHistory
from schemas import HouseInput

# Create tables
Base.metadata.create_all(bind=engine)

# Load ML model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

app = FastAPI()

@app.post("/predict")
def predict(data: HouseInput):

    db = SessionLocal()

    # ML prediction
    input_data = np.array([
        [data.area, data.bedrooms]
    ])

    prediction = model.predict(input_data)[0]

    # Save to database
    new_record = PredictionHistory(
        area=data.area,
        bedrooms=data.bedrooms,
        prediction=prediction
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return {
        "message": "Prediction saved successfully",
        "prediction": prediction
    }
```

---

# Step 5 - Run API

```bash
uvicorn main:app --reload
```

---

# Step 6 - Test API

Go to:

```text
http://127.0.0.1:8000/docs
```

Send:

```json
{
  "area": 2000,
  "bedrooms": 4
}
```

---

# Expected Response

```json
{
  "message": "Prediction saved successfully",
  "prediction": 400000
}
```

---

# Database Result

Every request now gets stored:

| id | area | bedrooms | prediction | created_at |
| -- | ---- | -------- | ---------- | ---------- |
| 1  | 2000 | 4        | 400000     | saved time |

---

# 🧠 What You Learned

### FastAPI

Handles request

### ML Model

Predicts output

### SQLAlchemy

Stores results

### SQLite

Persists data

---

# Real Production Flow

```text
Client Request
      ↓
FastAPI
      ↓
ML Prediction
      ↓
Store in DB
      ↓
Return Response
```

---

# ⚠️ Common Mistakes

* Forgetting `db.commit()`
* Not creating tables
* Wrong file imports
* Model input shape mismatch

---
