# Day 4 - Fraud Detection System Design

## Goal

Learn how banks and payment companies detect fraudulent transactions in real time while maintaining:

* High Accuracy
* Low Latency
* High Availability

---

# Understanding the Problem

When a customer swipes a credit card:

```text
Transaction
    ↓
Fraud Detection System
    ↓
Approve / Reject
```

The decision usually must happen in:

```text
50–200 ms
```

If the system is slow:

* Customer waits
* Payment fails
* Business loses money

If the system misses fraud:

* Financial loss
* Chargebacks
* Customer complaints

---

# Credit Card Fraud Detection Architecture

```text
                Customer
                    │
                    ▼
          Credit Card Transaction
                    │
                    ▼
             API Gateway
                    │
                    ▼
          Feature Extraction Service
                    │
            ┌───────┴────────┐
            │                │
            ▼                ▼
      Redis Cache      PostgreSQL
            │                │
            └───────┬────────┘
                    ▼
              Fraud Model
                    │
                    ▼
            Decision Engine
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
      Approve               Reject
                    │
                    ▼
             Transaction Logs
                    │
                    ▼
           Training Pipeline
                    │
                    ▼
              New Model
```

---

# Component Explanation

## 1. Transaction Request

Example:

```json
{
  "user_id": 101,
  "amount": 500,
  "merchant": "Amazon",
  "location": "Karachi"
}
```

This arrives through FastAPI.

---

## 2. Feature Extraction

Create features such as:

```text
Amount
Transactions Today
Average Spending
Merchant Category
Location Distance
Time Since Last Purchase
```

Example:

```text
Normal Amount = $50

Current Amount = $5000
```

Potential fraud signal.

---

# Where is Database?

### PostgreSQL

Stores:

* User profiles
* Transaction history
* Merchant information
* Fraud labels
* Audit logs

Example:

```text
Users Table
Transactions Table
Fraud Cases Table
```

Database sits before model prediction because features often require historical data.

---

# Where is Cache?

### Redis

Used for:

```text
Recent Transactions
User Features
Frequently Accessed Data
```

Example:

Instead of:

```sql
SELECT transactions
FROM database
```

for every request,

we fetch recent activity directly from Redis.

Benefits:

* Lower latency
* Reduced database load
* Faster feature generation

---

# Fraud Model

Input:

```text
Feature Vector
```

Output:

```text
Fraud Probability
```

Example:

```text
0.02 → Safe

0.98 → Fraud
```

Possible models:

* XGBoost
* LightGBM
* Random Forest
* Neural Networks

In industry, XGBoost and LightGBM are very common.

---

# Decision Engine

Business rules are combined with ML.

Example:

```text
Fraud Score > 0.90
    Reject

Fraud Score 0.50-0.90
    Manual Review

Fraud Score < 0.50
    Approve
```

---

# Challenge 1 - Imbalanced Data

Typical dataset:

```text
99.9% Normal

0.1% Fraud
```

Problem:

A model predicting:

```text
Always Normal
```

achieves:

```text
99.9% Accuracy
```

but is useless.

---

## Better Metrics

Use:

* Precision
* Recall
* F1 Score
* PR-AUC

Not just accuracy.

---

# Challenge 2 - Concept Drift

Fraud patterns change.

Example:

```text
2025 Fraud Pattern
      ↓
Model Learns It

2026 Fraudsters Change Strategy
      ↓
Model Performance Drops
```

This is called:

```text
Concept Drift
```

---

# How Often Retrain?

Depends on fraud volume.

### Small System

```text
Weekly
```

---

### Medium System

```text
Daily
```

---

### Large Bank

```text
Every Few Hours
```

or continuous retraining.

For interview answers:

```text
Daily retraining is a good balance.
```

---

# Bottlenecks

## 1. Database Reads

Problem:

Millions of transaction lookups.

Solution:

```text
Redis Cache
Read Replicas
```

---

## 2. Feature Generation

Problem:

Complex calculations.

Solution:

```text
Precompute Features
Store in Redis
```

---

## 3. Model Inference

Problem:

Prediction too slow.

Solution:

```text
Smaller Model
ONNX
Model Optimization
```

---

# Trade-offs

| Choice              | Benefit          | Cost                |
| ------------------- | ---------------- | ------------------- |
| Bigger Model        | Better Accuracy  | Higher Latency      |
| Frequent Retraining | Adapt Faster     | Higher Compute Cost |
| More Features       | Better Detection | Slower Prediction   |
| Redis Cache         | Faster Requests  | Extra Memory Cost   |

---

# Interview Questions

1. Why is accuracy important in fraud detection?
2. Why is latency important?
3. Why is fraud detection an imbalanced dataset problem?
4. Why is accuracy a bad metric here?
5. What is concept drift?
6. Why use Redis?
7. Where would PostgreSQL be used?
8. How often should models be retrained?

---

# Deliverable

Create a Fraud Detection System Design document containing:

1. Architecture Diagram
2. Database Design
3. Redis Usage
4. Feature List
5. Model Choice
6. Decision Rules
7. Bottlenecks
8. Retraining Strategy
9. Trade-offs
10. Answers to the 8 interview questions
