# 📅 Day 5 - Build History API (Iris Prediction System)

## 🎯 Goal

Retrieve stored prediction history like real-world applications.

Your API currently does this:

```text
User → Predict → Save to DB
```

After Day 5:

```text
User → Predict → Save to DB → Retrieve History
```

Now users can view previous predictions.

---

# 📚 Concepts Covered

## 1. Querying Database

You already know how to store data.

Now you'll retrieve it:

```python
db.query(Model).all()
```

This fetches all records from database.

---

## 2. Serialization (DB → JSON)

Database objects cannot directly return in API response.

FastAPI converts them into JSON format.

Example:

Database Record:

```text
sepal_length = 5.1
prediction = setosa
```

API Response:

```json
{
  "sepal_length": 5.1,
  "prediction": "setosa"
}
```

---

# Iris Prediction System Flow

```text
User Input
   ↓
Predict Endpoint
   ↓
ML Model Prediction
   ↓
Save to Database
   ↓
History Endpoint
   ↓
Return Past Predictions
```

---

# Updated Project Structure

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
└── requirements.txt
```

---

# Step 1 - Update `models.py`

Since you're building Iris prediction API:

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

    prediction = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
```

---

# Step 2 - Update `schemas.py`

```python
from pydantic import BaseModel

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
```

---

# Step 3 - Update `main.py`

```python
from fastapi import FastAPI
import pickle
import numpy as np

from database import SessionLocal, engine, Base
from models import PredictionHistory
from schemas import IrisInput

Base.metadata.create_all(bind=engine)

# Load trained iris model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

app = FastAPI()

species = ["setosa", "versicolor", "virginica"]

# -----------------------
# Predict Endpoint
# -----------------------
@app.post("/predict")
def predict(data: IrisInput):

    db = SessionLocal()

    input_data = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    prediction_index = model.predict(input_data)[0]
    prediction_label = species[prediction_index]

    # Save to DB
    new_record = PredictionHistory(
        sepal_length=data.sepal_length,
        sepal_width=data.sepal_width,
        petal_length=data.petal_length,
        petal_width=data.petal_width,
        prediction=prediction_label
    )

    db.add(new_record)
    db.commit()

    return {
        "prediction": prediction_label
    }

# -----------------------
# History Endpoint
# -----------------------
@app.get("/history")
def get_history():

    db = SessionLocal()

    records = db.query(PredictionHistory).all()

    history = []

    for record in records:
        history.append({
            "id": record.id,
            "sepal_length": record.sepal_length,
            "sepal_width": record.sepal_width,
            "petal_length": record.petal_length,
            "petal_width": record.petal_width,
            "prediction": record.prediction,
            "created_at": record.created_at
        })

    return {
        "history": history
    }
```

---

# Step 4 - Run API

```bash
uvicorn main:app --reload
```

---

# Step 5 - Test `/predict`

Input:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Response:

```json
{
  "prediction": "setosa"
}
```

---

# Step 6 - Test `/history`

Visit:

```text
http://127.0.0.1:8000/history
```

Response:

```json
{
  "history": [
    {
      "id": 1,
      "prediction": "setosa"
    }
  ]
}
```

---

# 🧠 What You Learned

### Querying

Retrieve stored predictions

### Serialization

Convert DB objects → JSON response

### API Design

Multiple endpoints

### Persistence

Users can track old predictions

---

# Real Backend Flow

```text
POST /predict → Make prediction + Save data
GET /history → Retrieve previous predictions
```

---

# ⚠️ Common Mistakes

* Returning raw SQLAlchemy objects directly
* Forgetting database session
* Incorrect model input order
* Not storing full feature values

---