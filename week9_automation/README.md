# Week 9 - Automation (MLOps)

## Main Goal

Build a fully automated ML lifecycle system:

* Train model automatically
* Detect new data
* Retrain model
* Save new versions
* Deploy/update model automatically
* Add CI/CD pipeline

By the end of this week, you’ll have a mini production-grade ML automation system.

---

# Tech Stack

You’ll use:

* Python
* FastAPI
* Scikit-learn
* MLflow
* GitHub Actions
* APScheduler / Cron
* Docker
* SQLite/PostgreSQL
* Joblib

---

# Final Architecture

```text
New Data Arrives
       ↓
Data Validation
       ↓
Retraining Pipeline
       ↓
Model Evaluation
       ↓
Versioning (MLflow)
       ↓
Auto Deployment
       ↓
FastAPI serves latest model
       ↓
CI/CD updates automatically
```

---

# DAY 1 - Introduction to ML Automation

## Topics

### What is MLOps Automation?

Understand:

* Manual ML workflow problems
* Why retraining matters
* Drift
* Continuous training
* Continuous deployment

---

## Learn These Concepts

### 1. Retraining Pipelines

Pipeline stages:

```text
Data → Preprocessing → Train → Evaluate → Save
```

---

### 2. Scheduling

Automate jobs using:

* Cron
* APScheduler
* Airflow (intro only)

---

### 3. CI/CD for ML

Difference:

| Traditional DevOps | MLOps                 |
| ------------------ | --------------------- |
| Deploy code        | Deploy models         |
| Unit tests         | Data/model validation |
| Build app          | Retrain pipeline      |

---

# Practice

## Build Folder Structure

```text
automated_ml_system/
│
├── app/
├── data/
├── models/
├── pipelines/
├── monitoring/
├── tests/
├── .github/workflows/
├── requirements.txt
└── main.py
```

---

## Mini Task

Create:

```python
def train_pipeline():
    print("Training Started")
    print("Training Finished")
```

---

# DAY 2 - Build Retraining Pipeline

## Goal

Create automated retraining logic.

---

# Learn

## Pipeline Stages

### Step 1 - Load Data

```python
df = pd.read_csv("data/train.csv")
```

---

### Step 2 - Preprocess

```python
X = df.drop("target", axis=1)
y = df["target"]
```

---

### Step 3 - Train

```python
from sklearn.ensemble import RandomForestClassifier
```

---

### Step 4 - Evaluate

Use:

* Accuracy
* F1-score
* Confusion matrix

---

### Step 5 - Save Model

```python
joblib.dump(model, "models/model.pkl")
```

---

# Project Task

Create:

```text
pipelines/
    retrain.py
```

Inside:

```python
def retrain():
    # load
    # preprocess
    # train
    # evaluate
    # save
```

---

# DAY 3 - Scheduling Automation

# Goal

Automatically run retraining every X minutes/hours.

---

# Learn APScheduler

Install:

```bash
pip install apscheduler
```

---

# Example

```python
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', minutes=1)
def retrain_job():
    print("Retraining...")

scheduler.start()
```

---

# Learn

## Scheduler Types

| Type     | Usage           |
| -------- | --------------- |
| Interval | Every X minutes |
| Cron     | Daily/hourly    |
| Date     | One-time        |

---

# Project Task

Create:

```text
pipelines/scheduler.py
```

Scheduler should:

* Trigger retraining
* Save logs
* Handle failures

---

# DAY 4 - Model Versioning + MLflow

# Goal

Track all model versions automatically.

---

# Learn MLflow

Install:

```bash
pip install mlflow
```

---

# Concepts

## Track:

* Parameters
* Metrics
* Artifacts
* Versions

---

# Example

```python
import mlflow

with mlflow.start_run():

    mlflow.log_param("model", "RandomForest")

    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(model, "model")
```

---

# Learn Model Registry

```text
v1 → v2 → v3
```

Understand:

* Staging
* Production
* Archived

---

# Project Task

Integrate MLflow into retraining pipeline.

Every retrain should:

* Create new run
* Log metrics
* Save artifacts
* Register new model version

---

# DAY 5 - Auto Deployment

# Goal

Deploy newest model automatically.

---

# Learn

## Dynamic Model Loading

FastAPI should always load latest model.

---

# Example

```python
model = joblib.load("models/latest.pkl")
```

---

# Advanced Idea

Automatically replace old model:

```text
best_model.pkl
```

---

# FastAPI Integration

Endpoint:

```python
@app.post("/predict")
```

should always use newest model.

---

# Project Task

Build:

```text
app/model_loader.py
```

Features:

* Load latest model
* Reload after retraining
* Handle failures safely

---

# DAY 6 - CI/CD for ML

# Goal

Automate testing + deployment.

---

# Learn GitHub Actions

Create:

```text
.github/workflows/mlops.yml
```

---

# Learn Pipeline Stages

```text
Push Code
    ↓
Run Tests
    ↓
Train Pipeline
    ↓
Build Docker
    ↓
Deploy
```

---

# Example Workflow

```yaml
name: ML Pipeline

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run Tests
        run: pytest
```

---

# Learn

## ML-Specific CI Checks

* Data schema validation
* Model accuracy threshold
* API health tests

---

# Project Task

CI/CD should:

* Run tests
* Check training
* Validate API
* Build Docker image

---

# DAY 7 - Final Automated ML System

# Final Goal

Connect EVERYTHING.

---

# Final Workflow

```text
Scheduler Starts
      ↓
Retraining Pipeline Runs
      ↓
MLflow Logs New Version
      ↓
Best Model Saved
      ↓
FastAPI Reloads Latest Model
      ↓
CI/CD Validates System
      ↓
Deployment Complete
```

---

# Final Features Checklist

## Your System Should Have

### Training Automation

* <input type="checkbox" disabled checked> Auto retraining
* <input type="checkbox" disabled checked> Scheduled jobs
* <input type="checkbox" disabled checked> Logging

---

### Model Management

* <input type="checkbox" disabled checked> Model versioning
* <input type="checkbox" disabled checked> Best model tracking
* <input type="checkbox" disabled checked> Artifact saving

---

### Deployment

* <input type="checkbox" disabled checked> FastAPI inference
* <input type="checkbox" disabled checked> Dynamic model loading
* <input type="checkbox" disabled checked> Docker support

---

### CI/CD

* <input type="checkbox" disabled checked> GitHub Actions
* <input type="checkbox" disabled checked> Tests
* <input type="checkbox" disabled checked> Auto validation

---