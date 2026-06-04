# DAY 7 - FINAL AUTOMATED ML SYSTEM

## Goal

Combine everything built during Week 9 into a complete automated ML system.

The system should automatically:

* Retrain models
* Evaluate performance
* Save new versions
* Track experiments
* Reload deployment
* Validate quality
* Support CI/CD automation

---

# Final Workflow

```text id="day7_flow"
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

# System Architecture

```text id="day7_architecture"
             APScheduler
                  │
                  ▼
        Retraining Pipeline
                  │
                  ▼
             Train Model
                  │
                  ▼
          Evaluate Metrics
                  │
                  ▼
       Accuracy Threshold Check
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
     Reject            Accept Model
                             │
                             ▼
                    MLflow Logging
                             │
                             ▼
                     Save Model
                             │
                             ▼
                   Reload FastAPI
                             │
                             ▼
                    Serve Predictions
```

---

# Final Project Structure

```text id="day7_structure"
Day7/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── model_loader.py
│
├── models/
│   └── best_model.pkl
│
├── pipeline/
│   ├── __init__.py
│   ├── retrain.py
│   └── scheduler.py
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── trainer.py
│   ├── evaluator.py
│   ├── model_saver.py
│   └── mlflow_logger.py
│
├── tests/
│   ├── test_data.py
│   ├── test_training.py
│   └── test_api.py
│
├── .github/
│   └── workflows/
│       └── mlops.yml
│
├── requirements.txt
└── README.md
```

---

# Components

## 1. Scheduler

Responsible for automatic retraining.

Example:

```python id="day7_scheduler"
scheduler.add_job(
    retrain_model,
    trigger="interval",
    minutes=10
)
```

Purpose:

* No manual retraining
* Fully automated pipeline

---

## 2. Training Pipeline

File:

```text id="day7_retrain_file"
pipeline/retrain.py
```

Responsibilities:

* Load data
* Train model
* Evaluate model
* Log to MLflow
* Save model
* Reload deployment

---

## 3. Model Evaluation

Metrics:

* Accuracy
* Precision
* Recall
* F1 Score

Example threshold:

```python id="day7_threshold"
if metrics["accuracy"] >= 0.90:
```

Only good models are deployed.

---

## 4. MLflow Tracking

Track:

* Parameters
* Metrics
* Artifacts
* Model Versions

Example:

```python id="day7_mlflow"
mlflow.log_param(
    "n_estimators",
    100
)

mlflow.log_metric(
    "accuracy",
    metrics["accuracy"]
)
```

Benefits:

* Experiment tracking
* Version history
* Reproducibility

---

## 5. Model Registry

Version progression:

```text id="day7_versions"
v1
 ↓
v2
 ↓
v3
 ↓
v4
```

Newest successful version becomes active.

---

## 6. Model Saving

File:

```text id="day7_save"
models/best_model.pkl
```

Purpose:

* Store latest approved model
* Provide deployment artifact

---

## 7. Auto Deployment

After saving:

```python id="day7_reload"
reload_model()
```

Result:

```text id="day7_reload_flow"
New Model Saved
      ↓
Model Reloaded
      ↓
FastAPI Uses Latest Version
```

No server restart required.

---

## 8. FastAPI Inference Service

Endpoint:

```text id="day7_endpoint"
POST /predict
```

Responsibilities:

* Load current model
* Predict class
* Return results

---

## 9. Testing Layer

Files:

```text id="day7_tests"
tests/
├── test_data.py
├── test_training.py
└── test_api.py
```

Checks:

* Data loading
* Training quality
* API health

---

## 10. CI/CD Layer

GitHub Actions automatically:

```text id="day7_cicd"
Push Code
    ↓
Install Dependencies
    ↓
Run Tests
    ↓
Run Training
    ↓
Validate Accuracy
    ↓
Build Deployment Artifact
```

---

# End-to-End Pipeline

```text id="day7_end_to_end"
Scheduler
    ↓
Retraining
    ↓
Evaluation
    ↓
MLflow Logging
    ↓
Model Save
    ↓
FastAPI Reload
    ↓
Testing
    ↓
CI/CD Validation
    ↓
Deployment
```

---

# Technologies Used

| Component     | Technology     |
| ------------- | -------------- |
| ML Model      | Scikit-Learn   |
| Tracking      | MLflow         |
| API           | FastAPI        |
| Scheduling    | APScheduler    |
| Testing       | Pytest         |
| CI/CD         | GitHub Actions |
| Serialization | Joblib         |

---

# Skills Learned in Week 9

* ML automation
* Retraining pipelines
* Scheduling jobs
* Experiment tracking
* Model versioning
* Auto deployment
* FastAPI serving
* Testing ML systems
* CI/CD for ML
* End-to-end MLOps fundamentals

---

# Final Outcome

You have built a complete beginner MLOps system:

```text id="day7_final"
Data
 ↓
Training
 ↓
Evaluation
 ↓
Versioning
 ↓
Tracking
 ↓
Deployment
 ↓
Monitoring Ready
```
