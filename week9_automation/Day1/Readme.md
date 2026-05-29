# DAY 1 - Introduction to ML Automation

Today’s goal is to understand why automation is necessary in real-world ML systems.

Most beginners train a model once and stop there.

Real ML systems continuously:

* receive new data
* retrain models
* validate performance
* deploy updates
* monitor failures

That full lifecycle is called:

# MLOps Automation

---

# 1. Problem With Manual ML Workflows

A beginner workflow usually looks like:

```text
Collect Data
    ↓
Train Model
    ↓
Save Model
    ↓
Deploy
```

This works only once.

But real-world data changes constantly.

Examples:

* User behavior changes
* Fraud patterns change
* Market prices change
* Language trends change

So model performance slowly drops.

This is called drift.

---

# 2. What is Drift?

Drift means:

> The data distribution changes over time.

Example:

A spam detection model trained in 2024 may fail in 2026 because spam messages evolve.

Two important types:

---

## Data Drift

Input data changes.

Example:

```text
Training Age Range: 20–40
New Data Age Range: 50–80
```

Model becomes unstable.

---

## Concept Drift

Relationship between input and output changes.

Example:

```text
Old:
"Free money" = spam

New:
AI-generated scams use normal language
```

Model predictions become wrong.

---

# Why Retraining Matters

Without retraining:

```text
Accuracy ↓
Predictions worsen
Business loses trust
```

So companies automate retraining pipelines.

---

# 3. Retraining Pipelines

A retraining pipeline is an automated ML workflow.

Pipeline stages:

```text
Data → Preprocessing → Train → Evaluate → Save
```

Let’s understand each stage.

---

## Step 1 - Data Collection

New data arrives from:

* databases
* APIs
* logs
* user activity
* sensors

Example:

```python
import pandas as pd

df = pd.read_csv("data/new_data.csv")
```

---

## Step 2 - Preprocessing

Clean and transform data.

Examples:

* Handle missing values
* Encoding
* Scaling
* Feature engineering

```python
X = df.drop("target", axis=1)
y = df["target"]
```

---

## Step 3 - Train

Train model again on latest data.

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X, y)
```

---

## Step 4 - Evaluate

Check whether new model is good.

Metrics:

* Accuracy
* Precision
* Recall
* F1-score

Example:

```python
accuracy = model.score(X, y)
```

---

## Step 5 - Save

Store trained model.

```python
import joblib

joblib.dump(model, "models/model.pkl")
```

---

# Complete Pipeline Flow

```text
New Data Arrives
       ↓
Preprocessing
       ↓
Training
       ↓
Evaluation
       ↓
Save New Model
       ↓
Deploy Updated Model
```

---

# 4. Scheduling

Automation means:

> Run jobs automatically at specific times.

Instead of manually retraining models every day.

---

# Common Scheduling Tools

| Tool        | Purpose                        |
| ----------- | ------------------------------ |
| Cron        | Linux scheduler                |
| APScheduler | Python scheduler               |
| Airflow     | Complex workflow orchestration |

---

# Cron (Basic Idea)

Linux cron jobs run commands automatically.

Example:

```text
0 2 * * * python retrain.py
```

Meaning:

```text
Run retraining daily at 2 AM
```

---

# APScheduler

Python-based scheduler.

Simple and beginner-friendly.

Example:

```python
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', minutes=1)
def retrain_job():
    print("Retraining Started")

scheduler.start()
```

This runs every minute automatically.

---

# Airflow (Intro Only)

Used in large-scale ML systems.

Features:

* DAG workflows
* Dependency management
* Retry handling
* Monitoring UI

Large companies use:

* Apache Airflow
* Kubeflow
* Prefect

You’ll learn basics later.

---

# 5. Continuous Training (CT)

Continuous Training means:

> Automatically retrain models when new data arrives.

Flow:

```text
New Data
   ↓
Trigger Training
   ↓
Evaluate
   ↓
Deploy Better Model
```

This keeps models updated.

---

# 6. Continuous Deployment (CD)

Continuous Deployment means:

> Automatically deploy validated models.

Example flow:

```text
Train New Model
      ↓
Accuracy > Threshold?
      ↓ YES
Deploy Automatically
```

---

# 7. CI/CD for ML

Traditional software CI/CD focuses on code.

ML CI/CD focuses on:

* code
* data
* models
* metrics

---

# Difference Between DevOps and MLOps

| Traditional DevOps | MLOps               |
| ------------------ | ------------------- |
| Deploy code        | Deploy models       |
| Unit tests         | Data validation     |
| Build application  | Retrain pipeline    |
| Monitor servers    | Monitor model drift |

---

# Real Production ML Lifecycle

```text
Data Collection
      ↓
Validation
      ↓
Training
      ↓
Evaluation
      ↓
Versioning
      ↓
Deployment
      ↓
Monitoring
      ↓
Retraining
```

This cycle never stops.

---

# Practice Section

## Mini Task

Create this simple training pipeline.

```python
def train_pipeline():
    print("Training Started")
    print("Training Finished")

train_pipeline()
```

---

# Your Task (Important)

Create file:

```text
pipelines/retrain.py
```

Add:

```python
def train_pipeline():
    print("Loading Data...")
    
    print("Preprocessing...")
    
    print("Training Model...")
    
    print("Evaluating...")
    
    print("Saving Model...")
    
    print("Pipeline Completed")

train_pipeline()
```

---

# Expected Understanding After Day 1

You should now understand:

* Why ML systems need automation
* Why retraining matters
* What drift is
* What pipelines are
* What scheduling means
* What CI/CD means in ML
* High-level MLOps lifecycle

---
