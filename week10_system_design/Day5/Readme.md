# Day 5 - Real-Time Prediction System Design

## Goal

Learn how real-time ML systems make predictions instantly using live data.

Examples:

* Uber ETA Prediction
* DoorDash Delivery Time Prediction
* Stock Price Prediction
* Ride Fare Estimation

---

# What is a Real-Time Prediction System?

Unlike recommendation systems that can precompute results, real-time systems must predict immediately.

Example:

```text
User requests a ride
      ↓
Current traffic checked
      ↓
Model predicts ETA
      ↓
Result shown instantly
```

Target latency:

```text
100–300 ms
```

---

# Uber ETA Prediction Architecture

```text
                 Rider Request
                       │
                       ▼
                 API Gateway
                       │
                       ▼
                Feature Service
               /               \
              ▼                 ▼
      Online Features     Offline Features
              │                 │
              ▼                 ▼
           Redis          PostgreSQL
              \               /
               ▼             ▼
                 Feature Vector
                       │
                       ▼
                  ETA Model
                       │
                       ▼
                 Prediction
                       │
                       ▼
                   User
```

---

# Step 1: Features

A model is only as good as its features.

---

## Online Features (Real-Time)

These change every second.

Examples:

### Driver Location

```text
Latitude
Longitude
```

---

### Rider Location

```text
Pickup Point
```

---

### Traffic Conditions

```text
Heavy Traffic
Medium Traffic
Light Traffic
```

---

### Weather

```text
Sunny
Rain
Storm
```

---

### Current Time

```text
Rush Hour
Weekend
Night
```

---

## Offline Features (Historical)

Stored and updated periodically.

Examples:

### Average Speed

```text
Road A = 40 km/h
Road B = 20 km/h
```

---

### Driver History

```text
Average trip duration
Average speed
```

---

### Route Statistics

```text
Historical ETA
Historical congestion
```

---

### Past Orders

Used to learn patterns.

---

# Feature Consistency

One of the most important ML system design concepts.

---

## Training

Suppose we train using:

```text
Traffic
Weather
Distance
```

---

## Serving

If we accidentally use:

```text
Distance only
```

Predictions become unreliable.

---

### Rule

Training Features = Serving Features

Always.

This is why many companies use a Feature Store.

---

# Database Design

## PostgreSQL

Stores:

### Drivers

```sql
drivers
--------
driver_id
rating
vehicle_type
```

---

### Trips

```sql
trips
------
trip_id
driver_id
start_time
end_time
distance
```

---

### Historical Data

```sql
trip_history
```

Used for retraining.

---

# Cache Layer

## Redis

Stores:

```text
Current Driver Location
Current Traffic Data
Recent Features
```

Why?

Querying PostgreSQL every second would be too slow.

Redis provides:

```text
Low latency
High throughput
```

---

# API Design

## Prediction Endpoint

```python
POST /predict_eta
```

Request:

```json
{
  "pickup": [24.86, 67.01],
  "destination": [24.90, 67.15]
}
```

Response:

```json
{
  "eta_minutes": 14
}
```

---

## Health Endpoint

```python
GET /health
```

Used by monitoring systems.

---

## Retraining Endpoint

```python
POST /retrain
```

Usually restricted to internal services.

---

# Model Service

Input:

```text
Distance
Traffic
Weather
Driver Location
Time
```

Output:

```text
ETA Prediction
```

---

## Possible Models

### Baseline

```text
Linear Regression
```

---

### Better

```text
Random Forest
XGBoost
LightGBM
```

---

### Advanced

```text
Deep Neural Networks
Graph Neural Networks
```

Large ride-sharing companies often use advanced route-aware models.

---

# Scalability Challenges

Suppose:

```text
1 Million Users
```

request ETA simultaneously.

---

## Problem 1

API overload.

Solution:

```text
Load Balancer
Multiple API Servers
```

---

## Problem 2

Database overload.

Solution:

```text
Redis
Read Replicas
```

---

## Problem 3

Model inference slow.

Solution:

```text
Model Optimization
ONNX
Batching
More Model Servers
```

---

# Bottlenecks

### Traffic Service

Real-time traffic data may be slow.

Solution:

```text
Cache traffic information
```

---

### Database

Millions of reads.

Solution:

```text
Redis
Read Replicas
```

---

### ETA Model

Complex model inference.

Solution:

```text
Optimized serving
Horizontal scaling
```

---

# Trade-offs

| Choice              | Benefit         | Cost              |
| ------------------- | --------------- | ----------------- |
| More Features       | Better Accuracy | Higher Latency    |
| Larger Model        | Better ETA      | Slower Prediction |
| More Caching        | Faster Response | More Memory       |
| Frequent Retraining | Better Accuracy | More Compute      |

---

# Interview Questions

1. What is the difference between online and offline features?
2. Why is feature consistency important?
3. Why use Redis in an ETA system?
4. Why not query PostgreSQL for every request?
5. What data should be stored in PostgreSQL?
6. What is the role of the API Gateway?
7. What happens if traffic data becomes unavailable?
8. How would you scale an ETA system to millions of users?

---

# Deliverable

Create a 2–3 page **Uber ETA Prediction System Design Document** containing:

1. Architecture Diagram
2. Online Features
3. Offline Features
4. Database Design
5. Redis Usage
6. API Design
7. Model Choice
8. Bottlenecks
9. Scaling Strategy
10. Answers to the 8 interview questions
