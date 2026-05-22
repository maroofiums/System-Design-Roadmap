# Week 8 - Monitoring ML Systems

## Goal

Learn how production ML systems are monitored, how failures are detected, and how to track model quality over time.

By the end of this week, you’ll build a monitored ML system that:

* Logs predictions
* Tracks latency/errors
* Detects data drift
* Detects concept drift
* Alerts when performance drops

---

# Day 1 - Introduction to ML Monitoring

## Learn

### What is Monitoring?

Monitoring means checking whether your ML system is healthy after deployment.

Example:

* Is prediction latency increasing?
* Is model accuracy dropping?
* Are users sending unusual data?
* Is the API failing?

---

## Learn These Metrics

### System Metrics

* CPU usage
* Memory usage
* API latency
* Error rate

### ML Metrics

* Accuracy
* Precision
* Recall
* Prediction distribution

---

## Understand the ML Production Lifecycle

Training → Deployment → Monitoring → Retraining

---

## Practice

Build a tiny prediction API and log:

* Input
* Prediction
* Timestamp

---

## Mini Task

Create:

```python
prediction_logs.csv
```

Columns:

```python
timestamp,input,prediction
```

---

# Day 2 - Logging in ML Systems

## Learn

### What is Logging?

Logs help debug failures.

Types:

* Application logs
* Error logs
* Prediction logs

---

## Learn Python Logging

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Prediction generated")
```

---

## Learn Log Levels

| Level    | Meaning            |
| -------- | ------------------ |
| DEBUG    | Detailed debugging |
| INFO     | Normal events      |
| WARNING  | Suspicious         |
| ERROR    | Failure            |
| CRITICAL | System crash       |

---

## Practice

Add logging to your FastAPI app.

Log:

* Request received
* Prediction completed
* Errors

---

## Project Task

Create:

```python
logs/
```

Inside:

```python
app.log
prediction.log
error.log
```

---

# Day 3 - Monitoring API Performance

## Learn

### Important Production Metrics

* Response time
* Throughput
* Failure rate
* Uptime

---

## Learn Latency

Latency = time taken to return prediction
$
Latency = t_{response} - t_{request}
$
---

## Practice

Track API latency:

```python
import time

start = time.time()

prediction = model.predict(X)

end = time.time()

latency = end - start
```

---

## Store Metrics

Create:

```python
metrics.csv
```

Columns:

```python
timestamp,latency,status
```

---

## Mini Project

Build a dashboard script:

```python
average_latency.py
```

Goal:

* Read metrics
* Calculate average latency
* Detect slow requests

---

# Day 4 - Data Drift

## Learn

### What is Data Drift?

When incoming data distribution changes from training data.

Example:

Training ages:

```python
20-40
```

Production ages:

```python
60-90
```

Model quality drops.

---

## Understand Distribution Shift

Training Data ≠ Real-world Data

---

## Learn Detection Methods

### Statistical Methods

* Mean comparison
* Standard deviation
* Histograms
* KS Test

---

## Practice

Compare:

```python
train.csv
production.csv
```

Check:

* Mean
* Variance
* Feature distributions

---

## Mini Project

Build:

```python
drift_detector.py
```

Features:

* Load train data
* Load production data
* Compare distributions
* Print drift warnings

---

# Day 5 - Concept Drift

## Learn

### What is Concept Drift?

Relationship between input and output changes.

Example:

Spam words in 2024 differ from 2026.

Old model becomes outdated.

---

## Difference

| Type          | Meaning         |
| ------------- | --------------- |
| Data Drift    | Input changes   |
| Concept Drift | Pattern changes |

---

## Learn Detection Ideas

* Accuracy monitoring
* Sliding window evaluation
* Recent-vs-old performance

---

## Practice

Simulate concept drift:

* Train on old dataset
* Test on changed dataset
* Observe accuracy drop

---

## Mini Project

Create:

```python
performance_monitor.py
```

Features:

* Track rolling accuracy
* Alert if accuracy < threshold

---

# Day 6 - Build Monitored ML System

# Project Architecture

```text
User Request
     ↓
FastAPI API
     ↓
Prediction
     ↓
Logging System
     ↓
Metrics Storage
     ↓
Drift Detection
     ↓
Alert System
```

---

# Build Components

## 1. Prediction API

FastAPI endpoint:

```python
/predict
```

---

## 2. Logging Module

Track:

* Inputs
* Predictions
* Errors

---

## 3. Metrics Module

Track:

* Latency
* Request count
* Failures

---

## 4. Drift Detector

Compare:

* Current data
* Training data

---

## 5. Performance Monitor

Track:

* Accuracy
* Confidence
* Prediction distribution

---

# Folder Structure

```text
ml_monitoring_project/
│
├── app/
│   ├── main.py
│   ├── monitoring.py
│   ├── drift.py
│   ├── logger.py
│   └── metrics.py
│
├── logs/
│
├── data/
│
├── dashboards/
│
└── requirements.txt
```

---

# Day 7 - Review + Portfolio Project

## Final Project

# Monitored ML System

## Features

### Monitoring

* Prediction tracking
* Latency tracking
* Error tracking

### ML Monitoring

* Data drift detection
* Performance monitoring
* Accuracy alerts

### Backend

* FastAPI API
* Logging system
* CSV/database storage

---

# README Must Include

## Problem

Why monitoring matters in ML systems.

---

## Architecture Diagram

Show full monitoring pipeline.

---

## Metrics Tracked

* Latency
* Accuracy
* Drift
* Failures

---

## Future Improvements

* Prometheus
* Grafana
* MLflow
* Evidently AI
* Real-time dashboards

---

# End-of-Week Skills

After Week 8 you’ll understand:

* Production ML systems
* Logging pipelines
* Monitoring infrastructure
* Drift detection
* Performance tracking
* Reliability engineering basics

---

# Optional Advanced Topics

If you finish early:

## Learn

* Prometheus
* Grafana
* MLflow
* Evidently AI
* Docker monitoring
* Kubernetes monitoring
* Alerting systems

---

# Recommended Stack

| Purpose             | Tool           |
| ------------------- | -------------- |
| API                 | FastAPI        |
| Logging             | Python logging |
| Storage             | CSV/PostgreSQL |
| Monitoring          | Prometheus     |
| Visualization       | Grafana        |
| Drift Detection     | Evidently AI   |
| Experiment Tracking | MLflow         |
