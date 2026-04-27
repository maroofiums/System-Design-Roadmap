# Day4 - Iris Prediction API using FastAPI

A production-style Machine Learning API that loads a trained **Iris Classification Model** and serves real-time predictions using **FastAPI**.

This project demonstrates how to move from a Jupyter Notebook model to a deployable backend API.

---

# Project Structure

```text
Day4/
┣ app/
┃ ┣ iris_model.pkl
┃ ┗ main.py
┣ Notebook/
┃ ┗ model.ipynb
┗ Readme.md
````

---

# Project Objective

Deploy a trained Machine Learning model as a REST API.

Users send flower measurements and receive predicted species instantly.

---

# What This Project Covers

* Loading trained model with Joblib
* FastAPI backend creation
* POST prediction endpoint
* JSON request/response flow
* Pydantic input validation
* Real-time inference
* Swagger API testing

---

# Dataset Used

This project uses the famous **Iris Flower Dataset**.

## Target Classes

* Setosa
* Versicolor
* Virginica

## Input Features

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

---

# Tech Stack

* Python
* FastAPI
* Uvicorn
* Scikit-learn
* Joblib
* Pydantic
* Jupyter Notebook

---

# API Flow

```text
Client Request
     ↓
FastAPI Server
     ↓
Load Trained Model
     ↓
Run Prediction
     ↓
Return JSON Response
```

---

# Model Loading

```python id="n1nqf2"
import joblib

model = joblib.load("iris_model.pkl")
```

The saved model is loaded once when the server starts.

---

# Main API Code

```python id="dzqfxw"
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
    return {"message": "Iris Prediction API Running"}

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
        "prediction_class": int(pred),
        "prediction_name": flower_names[pred]
    }
```

---

# API Endpoints

## GET /

Health/Home route.

Response:

```json id="oqz9li"
{
  "message": "Iris Prediction API Running"
}
```

---

## POST /predict

Predict flower species.

### Request Body

```json id="w0j7p1"
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Response

```json id="nq6d9q"
{
  "prediction_class": 0,
  "prediction_name": "Setosa"
}
```

---

# How to Run Project

## Step 1: Install Dependencies

```bash id="qgkrw0"
pip install fastapi uvicorn scikit-learn joblib
```

---

## Step 2: Navigate to App Folder

```bash id="kv2ekn"
cd app
```

---

## Step 3: Run Server

```bash id="gxw6wi"
uvicorn main:app --reload
```

---

## Step 4: Open Swagger Docs

```text
http://127.0.0.1:8000/docs
```

Use interactive testing UI.

---

# Example Predictions

## Example 1

Input:

```json id="uzd3dj"
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Output:

```json id="fuv5rm"
{
  "prediction_name": "Setosa"
}
```

---

## Example 2

Input:

```json id="s7kkc7"
{
  "sepal_length": 6.2,
  "sepal_width": 2.9,
  "petal_length": 4.3,
  "petal_width": 1.3
}
```

Output:

```json id="r2lrm6"
{
  "prediction_name": "Versicolor"
}
```

---

# Validation Features

FastAPI + Pydantic automatically validates:

* Missing fields
* Wrong data types
* Invalid JSON

Example bad request:

```json id="w8j6uo"
{
  "sepal_length": "abc"
}
```

Returns structured error automatically.

---

# Why This Project Matters

Many beginners stop here:

```text
Notebook Accuracy = 97%
```

But industry needs:

```text
Real APIs
Real Inference
Real Deployment
```

This project bridges that gap.

---

# Skills Demonstrated

* Backend Development
* ML Model Deployment
* API Design
* Input Validation
* Production Thinking
* Real-time Inference

---

# Future Improvements

## API Improvements

* Add confidence score
* Batch predictions
* Logging
* Error handling middleware
* API versioning

## Deployment Improvements

* Dockerize project
* Deploy on Render / Railway
* CI/CD pipeline
* Monitoring

## ML Improvements

* Better models
* Hyperparameter tuning
* Retraining pipeline

---

# What I Learned

Through this project I practiced:

* Converting ML model into API
* Serving predictions via FastAPI
* Handling structured inputs
* Returning JSON outputs
* Backend + ML integration

---
