# DAY 5 - AUTO DEPLOYMENT (ML SYSTEM)

## Goal

Build an ML system where the latest trained model is automatically used in FastAPI without restarting the server.

---

## Problem Statement

### Before Day 5

```text
Train Model → Save Model → API still uses OLD model
```

---

### After Day 5

```text
Train Model → Save Model → API automatically uses NEW model
```

---

## System Architecture

```text
Retraining Pipeline
        ↓
Model Evaluation
        ↓
Save best_model.pkl
        ↓
Reload model in memory
        ↓
FastAPI serves latest model
```

---

## Project Structure

```text
Day5/
│
├── app/
│   ├── main.py              # FastAPI app
│   └── model_loader.py      # Load and reload model
│
├── models/
│   └── best_model.pkl      # Active model file
│
├── pipeline/
│   └── retrain.py          # Training pipeline
│
└── src/
    ├── data_loader.py
    ├── trainer.py
    ├── evaluator.py
    └── model_saver.py
```

---

## Module Breakdown

### 1. data_loader.py

Purpose:
Load dataset and split into train and test sets.

Function:

* load_data()

Output:

* X_train, X_test, y_train, y_test

---

### 2. trainer.py

Purpose:
Train machine learning model.

Function:

* train_model(X_train, y_train)

Output:

* trained model
* parameters

---

### 3. evaluator.py

Purpose:
Evaluate model performance.

Function:

* evaluate_model(model, X_test, y_test)

Metrics:

* accuracy
* precision
* recall
* f1 score

---

### 4. model_saver.py

Purpose:
Save trained model.

Function:

* save_model(model)

Output:

* models/best_model.pkl

---

### 5. model_loader.py (Core Component)

Purpose:
Handle runtime model loading for FastAPI.

Functions:

* load_model()
  Loads model from disk

* get_model()
  Returns cached model for faster inference

* reload_model()
  Reloads updated model after retraining

---

### 6. main.py (FastAPI)

Purpose:
Expose prediction API.

Endpoints:

* GET /
  Health check

* POST /predict
  Uses latest model for prediction

---

### 7. retrain.py (Pipeline Orchestrator)

Purpose:
Controls full ML lifecycle.

Steps:

```text
1. Load data
2. Train model
3. Evaluate model
4. If accuracy >= threshold:
       save model
       reload model in API
```

---

## Auto Deployment Flow

```text
User triggers retraining
        ↓
Model trained
        ↓
Model evaluated
        ↓
best_model.pkl updated
        ↓
reload_model() executed
        ↓
FastAPI immediately uses new model
```

---

## How to Run

### Install dependencies

```bash
pip install fastapi uvicorn scikit-learn joblib
```

---

### Run training pipeline

```bash
python -m pipeline.retrain
```

---

### Start API

```bash
uvicorn app.main:app --reload
```

---

### Open API documentation

```text
http://127.0.0.1:8000/docs
```

---

## Test Input

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

---

## Output

```json
{
  "prediction": 0
}
```

---

## Key Learnings

* ML pipeline automation
* Model lifecycle management
* FastAPI model serving
* Runtime model reloading
* Basic auto deployment system

---

## Limitations

* No MLflow integration
* No CI/CD pipeline
* No model registry
* No monitoring system

---