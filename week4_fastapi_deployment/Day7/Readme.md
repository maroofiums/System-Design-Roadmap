# Day 7 - Dockerize ML API 

## Goal

Containerize your FastAPI + Machine Learning model using Docker so it can run anywhere without environment issues.

---

## What You Built

A complete ML system:

* Trained Iris classification model
* FastAPI prediction API
* Input validation using Pydantic
* Clean JSON responses
* Docker container for deployment

---

## Project Structure

```
Day7/
├── app/
│   ├── iris_model.pkl
│   └── main.py
├── requirements.txt
├── Dockerfile
└── Readme.md
```

---

## API Flow

```
Client Request
      ↓
FastAPI Server
      ↓
Load ML Model (joblib)
      ↓
Prediction
      ↓
JSON Response
```

---

## requirements.txt

Place this in the root `Day7/` folder:

```
fastapi
uvicorn
scikit-learn
joblib
pydantic
```

---

## Dockerfile

```
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## FastAPI Code (main.py)

```
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("iris_model.pkl")

flower_names = ["Setosa", "Versicolor", "Virginica"]

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"status": "success", "message": "API Running"}

@app.post("/predict")
def predict(data: IrisInput):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    pred = model.predict(features)[0]

    return {
        "status": "success",
        "prediction_class": int(pred),
        "prediction_name": flower_names[pred]
    }
```

---

## Build Docker Image

```
docker build -t iris-api .
```

---

## Run Docker Container

```
docker run -p 8000:8000 iris-api
```

---

## Test API

Open:

```
http://localhost:8000/docs
```

Use `/predict` endpoint.

---

## Sample Input

```
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

---

## Sample Output

```
{
  "status": "success",
  "prediction_class": 0,
  "prediction_name": "Setosa"
}
```

---

## What You Learned

* ML model deployment
* FastAPI backend development
* Input validation
* API testing
* Docker containerization
* Production-ready structure

---

## Industry Value

This project represents a real-world ML deployment pipeline used in production systems.

---