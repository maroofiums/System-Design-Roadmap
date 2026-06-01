# Day 4 - Model Versioning + MLflow (MLOps)

## Goal

In Day 4, we upgrade our ML pipeline from manual model saving to **MLflow-based experiment tracking system**.

Instead of only saving models like:

```

iris_model_1.pkl
iris_model_2.pkl
iris_model_3.pkl

```

We now track:

- Experiments
- Parameters
- Metrics
- Models
- Artifacts
- Runs history

---

# Project Structure

```

Day4/
│
├── pipeline/
│   └── retrain.py
│
├── src/
│   ├── data_loader.py
│   ├── trainer.py
│   ├── evaluator.py
│   ├── model_saver.py
│   └── mlflow_tracker.py
│
|── models/
|── Readme.md

````

---

# What is MLflow?

MLflow is an MLOps tool used for:

- Experiment tracking
- Model versioning
- Logging metrics
- Saving models (artifacts)
- Comparing different runs

---

# Installation

```bash
pip install mlflow
````

---

# Core MLflow Concepts

## 1. Experiment

A project or group of runs.

Example:

```
Iris-RandomForest
```

---

## 2. Run

One training session.

Example:

```
Run 1 → accuracy 0.95
Run 2 → accuracy 0.97
```

---

## 3. Parameters

Model settings:

* n_estimators
* random_state

---

## 4. Metrics

Performance values:

* accuracy
* precision
* recall
* f1-score

---

## 5. Artifacts

Saved files:

* model.pkl
* confusion matrix
* classification report

---

# MLflow Code Example

```python
import mlflow

with mlflow.start_run():

    mlflow.log_param("model", "RandomForest")

    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(model, "model")
```

---

# Pipeline Flow (Day 4 System)

```
Load Data
    ↓
Train Model
    ↓
Evaluate Model
    ↓
Log to MLflow
    ↓
Save Model (optional local backup)
```

---

# File Responsibilities

## data_loader.py

* Load Iris dataset
* Split into train/test

---

## trainer.py

* Train RandomForest model
* Return model + parameters

---

## evaluator.py

* Calculate:

  * accuracy
  * precision
  * recall
  * f1-score
* Return metrics + confusion matrix

---

## model_saver.py

* Save model using joblib
* Store in /models

---

## mlflow_tracker.py

* Start MLflow run
* Log parameters
* Log metrics
* Save model in MLflow
* Store artifacts (reports, matrices)

---

## retrain.py (Main Pipeline)

* Orchestrates everything
* Calls all modules
* Sends results to MLflow
* Saves model if performance is good

---

# Run Project

```bash
python -m pipeline.retrain
```

---

# Start MLflow UI

```bash
mlflow ui
```

Open:

```
http://127.0.0.1:5000
```

---

# What You Will See in MLflow UI

* Experiments list
* Run history
* Metrics graphs
* Parameters comparison
* Saved models
* Artifacts

---

# Why MLflow is Important

Before MLflow:

* Manual tracking
* File-based versioning
* No experiment history

After MLflow:

* Full tracking system
* Compare experiments
* Reproducibility
* Production-ready ML system

---

# Key Learning

* Experiment tracking
* Model versioning
* MLOps lifecycle
* Artifact logging
* Pipeline orchestration

---
