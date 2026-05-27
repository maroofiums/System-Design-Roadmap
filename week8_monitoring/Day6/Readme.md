# Day 6 - Build Monitored ML System (README)

## Overview

This project demonstrates an end-to-end **ML Monitoring System** built using FastAPI.
It combines:

* Prediction API
* Logging system
* Metrics tracking
* Data drift detection
* Concept drift monitoring
* Performance dashboard

---

## Architecture

```text id="z8v6kq"
User Request
     ↓
FastAPI API
     ↓
Prediction Engine
     ↓
Logging Layer
     ↓
Metrics Storage (CSV)
     ↓
Drift Detection Module
     ↓
Monitoring Dashboard (/summary)
```

---

## Features

### 1. Prediction API

Endpoint:

```text id="p2m0xq"
/predict?value=10
```

Returns:

* prediction result
* status (success/fail)
* logs request automatically

---

### 2. Logging System

Tracks:

* API requests
* Predictions
* Errors
* Metrics snapshots

Log files:

```text id="k8t0nd"
logs/app.log
logs/prediction.log
logs/error.log
logs/metrics.log
```

---

### 3. Metrics Tracking

Every request stores:

| Column    | Description      |
| --------- | ---------------- |
| timestamp | Request time     |
| latency   | Response time    |
| status    | success / failed |

Stored in:

```text id="x9k1mw"
data/metrics.csv
```

---

### 4. Drift Detection

#### Data Drift

Detects changes in input distribution using statistical tests.

* Method: KS Test
* Compares: train vs production data

#### Concept Drift

Detects change in relationship between input and output.

* Monitors accuracy drop
* Uses rolling performance checks

---

### 5. Monitoring Dashboard

Endpoint:

```text id="q1v8rt"
/summary?threshold=0.002
```

Returns:

* total requests
* average latency
* min/max latency
* failed requests
* slow requests

---

## Folder Structure

```text id="h4n2pc"
ml_monitoring_project/
│
├── app/
│   ├── main.py
│   ├── logger.py
│   ├── metrics.py
│   ├── drift.py
│   └── monitoring.py
│
├── data/
│   ├── train.csv
│   ├── production.csv
│   └── metrics.csv
│
├── logs/
│   ├── app.log
│   ├── prediction.log
│   ├── error.log
│   └── metrics.log
│
├── dashboards/
│   └── metrics_summary.py
│
├── requirements.txt
└── README.md
```

---

## Installation

```bash id="j9v3ab"
pip install -r requirements.txt
```

---

## Run the Project

```bash id="w2k8fd"
uvicorn app.main:app --reload
```

---

## Test API

### Predict

```text id="t8p4lm"
http://127.0.0.1:8000/predict?value=10
```

### Summary Dashboard

```text id="n1x7qz"
http://127.0.0.1:8000/summary
```

---

## Example Outputs

### Prediction Response

```json id="c7v1pd"
{
  "input": 10,
  "prediction": "positive"
}
```

---

### Metrics Response

```json id="m4k8yt"
{
  "total_requests": 5,
  "average_latency": 0.0012,
  "min_latency": 0.0009,
  "max_latency": 0.0021,
  "failed_requests": 1,
  "slow_requests": 2
}
```

---

## Key Concepts Learned

* ML system monitoring
* Logging architecture
* Metrics collection pipeline
* Data drift detection (KS Test)
* Concept drift monitoring
* Production-level API design

---

## Improvements (Future Work)

* Replace CSV with database (PostgreSQL)
* Real-time streaming metrics
* Grafana dashboard integration
* Alert system (email/Telegram)
* Docker deployment
* Kubernetes scaling
* Model version tracking (MLflow)

---

## Summary

This project simulates a **real-world ML production system** with monitoring, logging, and drift detection.

It is a foundational step toward building **MLOps-ready systems**.
