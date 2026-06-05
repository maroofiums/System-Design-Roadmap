# Week 10 - ML System Design Practice

### Goal

By the end of this week, you should be able to:

* Design production ML systems
* Understand end-to-end ML architecture
* Identify bottlenecks
* Discuss trade-offs like an ML Systems Engineer
* Build a production-style ML project

Since you're already learning FastAPI, ML, deployment concepts, and backend engineering, this week focuses on **thinking in systems rather than models**.

---

# Day 1 - ML System Design Fundamentals

## Theory

### What is an ML System?

Not just a model.

Production ML =

```
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

---

### Core Components

#### Data Layer

* Databases
* Data Warehouse
* Data Lake

Examples:

* PostgreSQL
* MySQL
* MongoDB
* S3

---

#### Training Layer

Responsible for:

* Data Cleaning
* Feature Engineering
* Model Training
* Evaluation

---

#### Serving Layer

Model exposed via:

* FastAPI
* Flask
* gRPC

---

#### Monitoring Layer

Track:

* Accuracy
* Latency
* Errors
* Data Drift

Tools:

* MLflow
* Prometheus
* Grafana

---

### Exercise

Draw architecture for:

```
House Price Prediction System
```

Include:

* User
* API
* Model
* Database

---

# Day 2 - Latency vs Throughput

## Theory

### Latency

Time for one request.

Example:

```
Request → Prediction

50 ms
```

---

### Throughput

Requests handled per second.

Example:

```
500 req/sec
```

---

### Trade-off

Lower latency often means:

```
More resources
Higher cost
```

Higher throughput often means:

```
Batching
Slightly higher latency
```

---

### Real World Examples

#### Fraud Detection

Need:

```
Ultra-low latency
```

Because transaction must be approved instantly.

---

#### Recommendation System

Can tolerate:

```
Higher latency
```

Because recommendations can be precomputed.

---

### Exercise

For each system choose priority:

* YouTube Recommendations
* Credit Card Fraud Detection
* Netflix Suggestions
* Stock Trading Bot

---

# Day 3 - Recommendation System Design

## System

```
Netflix / YouTube
```

---

## Architecture

```text
Users
   ↓
Interaction Logs
   ↓
Feature Store
   ↓
Training Pipeline
   ↓
Recommendation Model
   ↓
API Service
   ↓
Cache
   ↓
Users
```

---

### Components

#### Offline Training

Uses:

* Watch history
* Likes
* Clicks

Train daily.

---

#### Online Serving

FastAPI serves recommendations.

---

#### Cache

Redis

Stores:

```
Top recommendations
```

Avoids recomputation.

---

### Bottlenecks

* Huge user base
* Expensive ranking models
* Cold start problem

---

### Exercise

Design:

```
Movie Recommendation System
```

Draw architecture and explain every component.

---

# Day 4 - Fraud Detection System

## Problem

Detect suspicious transactions.

---

## Requirements

### High Accuracy

Missing fraud is expensive.

### Low Latency

Need prediction in milliseconds.

---

## Architecture

```text
Transaction
      ↓
Feature Extraction
      ↓
Fraud Model
      ↓
Decision Engine
      ↓
Approve / Reject
```

---

### Challenges

#### Imbalanced Data

```
99.9% Normal
0.1% Fraud
```

---

#### Concept Drift

Fraudsters change behavior.

Need retraining.

---

### Exercise

Design:

```
Credit Card Fraud Detection System
```

Answer:

* Where is database?
* Where is cache?
* How often retrain?

---

# Day 5 - Real-Time Prediction System

## Example

Food Delivery ETA

Uber ETA

Stock Prediction

---

## Architecture

```text
User
 ↓
API Gateway
 ↓
Feature Service
 ↓
Model Service
 ↓
Prediction
```

---

### Concepts

#### Online Features

Current:

* Location
* Traffic
* Weather

---

#### Offline Features

Historical:

* Average speed
* Past orders

---

### Challenges

#### Feature Consistency

Training features must match serving features.

---

#### Scalability

Millions of requests.

---

### Exercise

Design:

```
Uber ETA Prediction System
```

Explain:

* Features
* Database
* API
* Model

---

# Day 6 - Fault Tolerance & Bottleneck Analysis

## Theory

### Fault Tolerance

System survives failures.

---

### Example

If model server crashes:

```text
Load Balancer
      ↓
Model Server 1
Model Server 2
Model Server 3
```

Traffic shifts automatically.

---

### Bottleneck Analysis

Ask:

### What breaks first?

Possible bottlenecks:

#### Database

Too many reads.

Solution:

```
Read Replicas
```

---

#### API

Too many requests.

Solution:

```
Horizontal Scaling
```

---

#### Model

Prediction too slow.

Solution:

```
Caching
Smaller Model
GPU
```

---

### Exercise

Analyze bottlenecks in:

```
Movie Recommendation System
```

Find at least:

* 3 bottlenecks
* 3 solutions

---

# Day 7 - Final Project

## Build a Production-Level ML System Design

Choose one:

### Option 1

E-commerce Recommendation System

### Option 2

Fraud Detection System

### Option 3

Real-Time ETA Prediction

---

## Required Components

### Training Pipeline

```text
Raw Data
 ↓
Cleaning
 ↓
Feature Engineering
 ↓
Training
 ↓
Evaluation
 ↓
Model Registry
```

---

### API Layer

```text
FastAPI
```

Endpoints:

```python
POST /predict
GET /health
POST /retrain
```

---

### Database

Store:

* Users
* Predictions
* Logs

Example:

```text
PostgreSQL
```

---

### Cache

```text
Redis
```

Store:

* Frequent predictions
* Recommendations

---

### Monitoring

Track:

* Latency
* Accuracy
* Errors
* Drift

Tools:

* Prometheus
* Grafana
* MLflow

---

### Retraining Pipeline

```text
New Data
 ↓
Scheduled Training
 ↓
Validation
 ↓
Deploy New Model
```

---

# End-of-Week Deliverable

Create a complete design document containing:

1. System Requirements
2. Architecture Diagram
3. Database Design
4. API Design
5. Cache Strategy
6. Monitoring Strategy
7. Retraining Strategy
8. Bottlenecks
9. Scaling Plan
10. Trade-offs