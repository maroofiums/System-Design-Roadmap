# DAY 6 - CI/CD FOR ML 

## Goal

Automate the full ML workflow:

* Testing
* Training validation
* Model checks
* API validation
* Deployment readiness

---

## What is CI/CD in ML?

CI/CD means:

* CI (Continuous Integration): Code + model tests run automatically
* CD (Continuous Deployment): System is deployed automatically if checks pass

---

## ML CI/CD Pipeline Flow

```text id="cicd1"
Push Code to GitHub
        ↓
GitHub Actions Trigger
        ↓
Install Dependencies
        ↓
Run Unit Tests
        ↓
Run Training Pipeline
        ↓
Validate Model Metrics
        ↓
Build Docker Image
        ↓
Deploy (optional stage)
```

---

## Project Structure

```text id="cicd2"
Day6/
│
├── .github/
│   └── workflows/
│       └── mlops.yml
│
├── pipeline/
│   └── retrain.py
│
├── src/
│   ├── data_loader.py
│   ├── trainer.py
│   ├── evaluator.py
│   └── model_saver.py
│
├── tests/
│   ├── test_data.py
│   ├── test_training.py
│   └── test_api.py
│
└── app/
    ├── main.py
    └── model_loader.py
```

---

## GitHub Actions Workflow

### File: `.github/workflows/mlops.yml`

```yaml id="cicd3"
name: ML CI/CD Pipeline

on:
  push:
    branches: [ "main" ]

jobs:
  build-and-test:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install Dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Unit Tests
        run: pytest

      - name: Run Training Pipeline
        run: python -m pipeline.retrain

      - name: Validate Model Metrics
        run: python tests/test_training.py
```

---

## ML-Specific CI Checks

### 1. Data Validation

Check:

* Missing values
* Shape consistency
* Feature correctness

Example:

```python id="cicd4"
assert X.shape[0] > 0
assert y is not None
```

---

### 2. Model Quality Check

Only allow deployment if:

```text id="cicd5"
accuracy >= 0.90
```

Example:

```python id="cicd6"
assert metrics["accuracy"] > 0.90
```

---

### 3. API Health Test

Check FastAPI is working:

```python id="cicd7"
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api():
    response = client.get("/")
    assert response.status_code == 200
```

---

## Training Validation Test

### tests/test_training.py

```python id="cicd8"
from pipeline.retrain import retrain_model

def test_training():

    metrics = retrain_model()

    assert metrics["accuracy"] >= 0.90
```

---

## Requirements File

```text id="cicd9"
fastapi
uvicorn
scikit-learn
joblib
pytest
```

---

## How CI/CD Works

```text id="cicd10"
Developer pushes code
        ↓
GitHub Actions runs
        ↓
Tests executed automatically
        ↓
Model is trained
        ↓
Model is validated
        ↓
If success → pipeline passes
        ↓
Else → pipeline fails
```

---

## Docker Build Stage (Optional Extension)

Add this step:

```yaml id="cicd11"
- name: Build Docker Image
  run: |
    docker build -t iris-ml-api .
```

---

## Full CI/CD Flow

```text id="cicd12"
Code Push
   ↓
Test Code
   ↓
Train Model
   ↓
Validate Metrics
   ↓
Build Image
   ↓
Deploy (future step)
```

---

## Key Learnings

* CI/CD for ML systems
* GitHub Actions automation
* Model validation in pipelines
* Automated training execution
* Testing ML + API together

---

## Limitations

* No cloud deployment yet
* No model registry integration
* No rollback system
* No monitoring system

---