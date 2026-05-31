# Day 3 - Scheduling Automation

## Overview

In Day 3, we automated the retraining pipeline created in Day 2 using APScheduler.

The system now retrains the model automatically at fixed intervals and stores a new version of the model after each successful training run.

---

## Project Structure

```text
Day3
├── models
│   ├── iris_model_1.pkl
│   ├── iris_model_2.pkl
│   ├── iris_model_3.pkl
│   ├── ...
│   └── iris_model_27.pkl
│
├── pipeline
│   ├── retrain.py
│   └── scheduler.py
│
└── src
    ├── data_loader.py
    ├── evaluator.py
    ├── model_saver.py
    └── trainer.py
```

---

## Objective

Automate model retraining without manual execution.

Instead of running:

```bash
python -m pipeline.retrain
```

the scheduler automatically triggers retraining.

---

## Technologies Used

* Python
* APScheduler
* Scikit-Learn
* Joblib

---

## Workflow

```text
Scheduler
    ↓
Load Data
    ↓
Train Model
    ↓
Evaluate Model
    ↓
Save New Version
    ↓
Wait For Next Schedule
```

---

## Scheduler

### scheduler.py

Uses APScheduler's BlockingScheduler.

```python
scheduler = BlockingScheduler()
```

A scheduled job runs periodically:

```python
@scheduler.scheduled_job("interval", minutes=1)
```

which calls:

```python
retrain_model()
```

---

## Model Versioning

Each retraining cycle creates a new model file:

```text
iris_model_1.pkl
iris_model_2.pkl
iris_model_3.pkl
...
```

This provides simple model versioning.

Benefits:

* Previous models are preserved
* Easy rollback
* Track training history

---

## Components

### data_loader.py

Responsible for:

* Loading Iris dataset
* Train/Test splitting

---

### trainer.py

Responsible for:

* Creating RandomForestClassifier
* Training the model

---

### evaluator.py

Calculates:

* Accuracy
* Precision
* Recall
* F1 Score

---

### model_saver.py

Creates versioned model files using Joblib.

Example:

```python
joblib.dump(model, model_path)
```

---

### retrain.py

Main retraining pipeline.

Pipeline stages:

```text
Load
 ↓
Train
 ↓
Evaluate
 ↓
Save
```

---

## Example Output

```text
Retraining Model...

Data Loading...
Model Training...
Evaluating Model...

Metrics:
------------------------------
accuracy: 0.9000
f1: 0.8997
recall: 0.9000
precision: 0.9024

Model Saved: models\iris_model_27.pkl
Model Retrained
```

---

## Key Concepts Learned

### Scheduling

Automatically execute ML tasks at fixed intervals.

### Automation

Remove manual retraining steps.

### Versioning

Store multiple trained model versions.

### Modular Design

Separate responsibilities into independent modules.

---

## Limitations

Current system:

* Saves every model
* No experiment tracking
* No model comparison
* No deployment logic

---

## Outcome

You now have an automated retraining system capable of:

* Periodic execution
* Model evaluation
* Versioned model storage
* Modular ML pipeline design

This is your first complete MLOps automation workflow.
