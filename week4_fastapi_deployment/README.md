# Week 4 - Model Deployment Roadmap

## Goal: Convert ML Model into API

By the end of this week, you’ll know how to take any trained ML model and turn it into a usable backend service using **FastAPI**.

---

# What You’ll Build This Week

**ML Prediction API**

Example:

* Input: age, income, experience
* Output: salary prediction / fraud prediction / house price prediction

Endpoint:

```bash
POST /predict
```

---

# Tech Stack

* Python
* FastAPI
* Pydantic
* Scikit-learn
* Joblib / Pickle
* Uvicorn

---

# Day by Day Plan

---

## Day 1 - API Basics + FastAPI Intro

## Goal:

Understand how APIs work.

## Learn:

* What is API
* Client → Server → Response
* HTTP Methods:

  * GET
  * POST
* JSON data flow

## Practice:

Build basic FastAPI app:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello"}
```

Run:

```bash
uvicorn main:app --reload
```

## Outcome:

You understand request/response lifecycle.

---

## Day 2 - Request Body + Input Validation

## Goal:

Accept user input safely.

## Learn:

* POST requests
* JSON body
* Pydantic models
* Validation errors

## Build:

```python
from pydantic import BaseModel

class UserInput(BaseModel):
    age: int
    income: float
```

Endpoint:

```python
@app.post("/predict")
def predict(data: UserInput):
    return data
```

## Outcome:

You can receive structured user data.

---

## Day 3 - Train Model + Save Model

## Goal:

Prepare ML model for deployment.

## Learn:

* Train model
* Save model

## Example:

```python
from sklearn.linear_model import LinearRegression
import joblib

model.fit(X,y)

joblib.dump(model,"model.pkl")
```

## Outcome:

You now have deployable model file.

---

## Day 4 - Load Model in API

## Goal:

Use trained model inside FastAPI.

## Build:

```python
model = joblib.load("model.pkl")
```

Inside route:

```python
prediction = model.predict([[age,income]])
```

Return:

```python
{"prediction": 50000}
```

## Outcome:

Real inference working.

---

## Day 5 - Error Handling + Clean Responses

## Learn:

* try/except
* invalid inputs
* missing values
* response formatting

Example:

```python
{
 "status":"success",
 "prediction":50000
}
```

## Outcome:

Professional API structure.

---

## Day 6 - Testing API

## Learn:

Use:

* Swagger Docs

Visit:

```bash
localhost:8000/docs
```

Test:

* valid input
* invalid input
* edge cases

## Outcome:

You can test like real developer.

---

## Day 7 - Final Project

# Build Full ML Prediction API

## Structure:

```bash
project/
│── main.py
│── model.pkl
│── train.py
│── requirements.txt
```

## Endpoints:

```bash
GET /
POST /predict
GET /health
```

---

# Bonus Level (Advanced)

Add:

* Docker
* Logging
* Authentication
* Deploy to Render / Railway
* Batch prediction

---

# Real World Skills You Gain

* Backend + ML combination
* API engineering
* Model serving
* Validation mindset
* Production thinking

---

# After Week 4 You Become

Not just ML learner.

You become someone who can **ship models**.

That’s rare.

---