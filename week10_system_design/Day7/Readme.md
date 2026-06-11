# Day 7 - Final Project (Production-Level ML System)

Since your goal is ML Engineering and backend development, I recommend building **Option 2: Fraud Detection System**.

Why?

* Strong ML component
* Strong backend component
* Real-time prediction
* Database design
* Monitoring
* Retraining
* Common ML System Design interview question

---

# Project: Credit Card Fraud Detection System

## Functional Requirements

The system should:

* Accept transaction requests
* Predict fraud probability
* Approve or reject transactions
* Store transaction history
* Monitor model performance
* Retrain periodically

---

# High-Level Architecture

```text
                    User
                      │
                      ▼
               FastAPI Service
                      │
          ┌───────────┼───────────┐
          ▼                       ▼
       Redis                 PostgreSQL
          │                       │
          └───────────┬───────────┘
                      ▼
               Feature Service
                      │
                      ▼
                 ML Model
                      │
                      ▼
               Decision Engine
                      │
             Approve / Reject
                      │
                      ▼
                Transaction Log
                      │
                      ▼
                Monitoring
                      │
                      ▼
             Retraining Pipeline
```

---

# Training Pipeline

## Step 1: Raw Data

Data sources:

```text
Transactions
User Profiles
Merchant Data
Device Data
```

Example:

```json
{
  "amount": 1200,
  "merchant": "Amazon",
  "country": "PK",
  "device": "Mobile"
}
```

---

## Step 2: Data Cleaning

Remove:

* Missing values
* Duplicate transactions
* Corrupted records

---

## Step 3: Feature Engineering

Create features:

```text
Transactions in last 24 hours
Average transaction amount
Country mismatch
Time since last transaction
Merchant risk score
```

---

## Step 4: Training

Model choices:

1. Logistic Regression (baseline)
2. Random Forest
3. XGBoost

Recommended:

```text
XGBoost
```

because fraud datasets are usually tabular.

---

## Step 5: Evaluation

Metrics:

```text
Precision
Recall
F1 Score
PR-AUC
```

Avoid accuracy alone because fraud data is highly imbalanced.

---

## Step 6: Model Registry

Store versions:

```text
fraud_model_v1
fraud_model_v2
fraud_model_v3
```

Use:

* MLflow

---

# API Layer (FastAPI)

## POST /predict

Input:

```json
{
  "user_id": 101,
  "amount": 5000,
  "merchant": "Amazon"
}
```

Output:

```json
{
  "fraud_probability": 0.92,
  "decision": "REJECT"
}
```

---

## GET /health

Returns:

```json
{
  "status": "healthy"
}
```

Used by monitoring tools.

---

## POST /retrain

Triggers retraining pipeline.

Only admin/internal access.

---

# Database Design

Use:

```text
PostgreSQL
```

---

## Users Table

```sql
users
------
user_id
name
country
created_at
```

---

## Transactions Table

```sql
transactions
------------
transaction_id
user_id
amount
merchant
prediction
timestamp
```

---

## Logs Table

```sql
logs
-----
log_id
event
timestamp
```

---

# Cache Layer

Use:

```text
Redis
```

Store:

### Recent User Activity

```text
Last 20 Transactions
```

---

### Computed Features

```text
Average Spend
Transaction Count
```

---

### Frequent Predictions

Avoid recomputing repeatedly.

---

# Monitoring

## What to Track?

### Latency

```text
Average Response Time
```

Target:

```text
< 100 ms
```

---

### Errors

```text
5xx Errors
Timeouts
```

---

### Accuracy

Compare predictions against confirmed fraud cases.

---

### Data Drift

Check whether:

```text
Training Data
```

differs from

```text
Production Data
```

---

## Tools

* Prometheus
* Grafana
* MLflow

---

# Retraining Pipeline

```text
New Transactions
        ↓
Feature Engineering
        ↓
Training
        ↓
Validation
        ↓
Model Registry
        ↓
Deployment
```

---

## Retraining Frequency

Recommended:

```text
Daily
```

Trigger earlier if:

* Drift detected
* Precision drops
* Recall drops

---

# Fault Tolerance

## Multiple API Servers

```text
Load Balancer
      │
 ┌────┼────┐
 ▼    ▼    ▼
API1 API2 API3
```

---

## Multiple Model Servers

```text
Load Balancer
      │
 ┌────┼────┐
 ▼    ▼    ▼
M1   M2   M3
```

---

## Database Replicas

```text
Primary DB
     │
 ┌───┴───┐
 ▼       ▼
Replica Replica
```

---

# Bottlenecks and Solutions

| Bottleneck      | Cause                  | Solution                         |
| --------------- | ---------------------- | -------------------------------- |
| Database        | Too many reads         | Redis + Read Replicas            |
| API             | Heavy traffic          | Horizontal Scaling               |
| Model           | Slow inference         | XGBoost + Multiple Model Servers |
| Feature Service | Expensive calculations | Precompute Features              |

---

# Trade-offs

| Choice              | Benefit            | Cost                |
| ------------------- | ------------------ | ------------------- |
| Larger Model        | Better Accuracy    | Higher Latency      |
| More Features       | Better Detection   | More Complexity     |
| Frequent Retraining | Better Performance | Higher Compute Cost |
| More Caching        | Faster Responses   | More Memory         |

---

# End-of-Week Deliverable

Create a document containing:

1. Problem Statement
2. Functional Requirements
3. Architecture Diagram
4. Training Pipeline
5. Database Design
6. API Design
7. Redis Strategy
8. Monitoring Strategy
9. Retraining Strategy
10. Fault Tolerance Design
11. Bottlenecks & Solutions
12. Trade-offs
