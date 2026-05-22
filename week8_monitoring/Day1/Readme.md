# Day 1 - Introduction to ML Monitoring Notes

# What is Monitoring?

Monitoring means checking whether your ML system is working properly after deployment.

A deployed ML model can fail because:

* Data changes
* Users behave differently
* Server becomes slow
* Predictions become inaccurate
* API crashes

Monitoring helps detect these issues early.

---

# Example Problems Monitoring Detects

## 1. Increasing Latency

Prediction API becomes slower over time.

Latency = t_{response} - t_{request}

---

## 2. Accuracy Drop

Model predictions become incorrect.

Accuracy = \frac{Correct\ Predictions}{Total\ Predictions}

---

## 3. Unusual Input Data

Users send data different from training data.

Example:

Training:

```python
age = 20-40
```

Production:

```python
age = 80-100
```

This may reduce model performance.

---

## 4. API Failures

Server errors increase.

Error\ Rate = \frac{Failed\ Requests}{Total\ Requests}

---

# Types of Monitoring

# 1. System Monitoring

Tracks infrastructure health.

## Important Metrics

| Metric       | Meaning         |
| ------------ | --------------- |
| CPU Usage    | Processor load  |
| Memory Usage | RAM consumption |
| API Latency  | Response speed  |
| Error Rate   | Failed requests |

---

# 2. ML Monitoring

Tracks model behavior and quality.

## Important Metrics

| Metric                  | Meaning                      |
| ----------------------- | ---------------------------- |
| Accuracy                | Correct predictions          |
| Precision               | Correct positive predictions |
| Recall                  | Positive cases detected      |
| Prediction Distribution | Model prediction patterns    |

---

# ML Production Lifecycle

```text
Training
   ↓
Deployment
   ↓
Monitoring
   ↓
Retraining
```

Explanation:

| Stage      | Meaning                     |
| ---------- | --------------------------- |
| Training   | Model learns patterns       |
| Deployment | Model goes live             |
| Monitoring | Track performance           |
| Retraining | Update model using new data |

---

# Practice Project

Goal:

Build a small prediction API that logs:

* Input
* Prediction
* Timestamp

---

# Project Structure

```text
Day1/
├── app.py
├── prediction_logs.csv
|__ Readme.md
```

---

# Install Requirements

```bash
pip install fastapi uvicorn pandas
```

---

# Build Tiny Prediction API

## app.py

```python
from fastapi import FastAPI
import pandas as pd
from datetime import datetime
import os

app = FastAPI()

LOG_FILE = "prediction_logs.csv"

# Create CSV if not exists
if not os.path.exists(LOG_FILE):

    df = pd.DataFrame(columns=[
        "timestamp",
        "input",
        "prediction"
    ])

    df.to_csv(LOG_FILE, index=False)


@app.get("/predict")

def predict(value: int):

    # Dummy prediction logic
    prediction = "positive" if value > 5 else "negative"

    # Create log entry
    log = {
        "timestamp": datetime.now(),
        "input": value,
        "prediction": prediction
    }

    # Append to CSV
    df = pd.DataFrame([log])

    df.to_csv(
        LOG_FILE,
        mode="a",
        header=False,
        index=False
    )

    return {
        "input": value,
        "prediction": prediction
    }
```

---

# Run Server

```bash
uvicorn app:app --reload
```

---

# Test API

Open:

```text
http://127.0.0.1:8000/predict?value=10
```

---

# Example Output

```json
{
    "input": 10,
    "prediction": "positive"
}
```

---

# prediction_logs.csv

```csv
timestamp,input,prediction
2026-05-22 12:10:01,10,positive
2026-05-22 12:11:14,2,negative
```

---

# What You Learned

## Concepts

* ML monitoring
* System monitoring
* ML monitoring metrics
* Production lifecycle

---

## Practical Skills

* FastAPI basics
* Prediction logging
* CSV storage
* Timestamp tracking

---

# Mini Challenge

Improve prediction logic:

```python
if value > 8:
    prediction = "high"

elif value > 4:
    prediction = "medium"

else:
    prediction = "low"
```

Then verify logs are saved correctly in:

```python
prediction_logs.csv
```
