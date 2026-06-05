# Week 10 - Day 1: ML System Design Fundamentals

## Goal
Understand how a Machine Learning system works in production from data collection to model retraining.

---

# ML System Lifecycle

```text
Data
 ↓
Training Pipeline
 ↓
Model Registry
 ↓
Deployment
 ↓
API Service
 ↓
Monitoring
 ↓
Retraining
```

## 1. Data Layer
### Purpose
Stores raw and processed data used for training and inference.

### Input
- User data
- Logs
- Transactions
- Application data

### Output
- Cleaned datasets for training

### Technologies
- PostgreSQL
- MongoDB
- Amazon S3

---

## 2. Training Pipeline

### Purpose
Transforms raw data into a trained model.

### Steps
1. Data Cleaning
2. Feature Engineering
3. Model Training
4. Model Evaluation

### Input
- Dataset

### Output
- Trained Model

---

## 3. Model Registry

### Purpose
Stores model versions and metadata.

### Why Important?
- Version control for ML models
- Rollback capability
- Experiment tracking

### Tools
- MLflow

---

## 4. Deployment

### Purpose
Makes the trained model available for users.

### Methods
- REST API
- Batch Predictions
- Real-time Predictions

---

## 5. API Service

### Purpose
Receives requests and returns predictions.

### Example
FastAPI endpoint:

```python
POST /predict
```

### Input
House features

### Output
Predicted price

---

## 6. Monitoring

### Purpose
Track system health and model performance.

### Metrics
- Latency
- Throughput
- Accuracy
- Error Rate
- Data Drift

### Tools
- Prometheus
- Grafana
- MLflow

---

## 7. Retraining

### Purpose
Update the model when performance decreases.

### Trigger
- New data arrives
- Data drift detected
- Scheduled retraining

---

# Core System Design Concepts

## Latency

### Definition
Time required to process a single request.

Example:

```text
Request → Prediction = 50ms
```

### Why Important?
Users expect fast responses.

---

## Throughput

### Definition
Number of requests processed per second.

Example:

```text
1000 requests/sec
```

### Why Important?
Determines system capacity.

---

## Scalability

### Definition
Ability to handle increased traffic.

### Methods
- Horizontal Scaling
- Load Balancing

---

## Fault Tolerance

### Definition
Ability to continue operating despite failures.

### Example

```text
Load Balancer
     ↓
Server 1
Server 2
Server 3
```

If one server fails, traffic is routed to others.

---

# Mini Case Study

## House Price Prediction System

### Basic Architecture

```text
User
 ↓
FastAPI
 ↓
House Price Model
 ↓
Database
```

### Improved Production Architecture

```text
User
 ↓
FastAPI
 ↓
Redis Cache
 ↓
House Price Model
 ↓
PostgreSQL

Monitoring
 ↓
MLflow

Retraining Pipeline
```

---

# Interview Questions

1. What is the difference between training and inference?
2. Why is FastAPI commonly used for ML deployment?
3. What is latency?
4. What is throughput?
5. Why do ML models require monitoring?
6. What is data drift?
7. Why is retraining necessary?
8. What happens if an API server crashes?

---

# Day 1 Deliverables

- ML System Lifecycle Notes
- Latency vs Throughput Notes
- House Price Prediction Architecture
- Answers to Interview Questions