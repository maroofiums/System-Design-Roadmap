# Day 2 - Latency vs Throughput & System Trade-offs

### Goal

Learn how ML systems behave under load and how engineers make trade-offs between speed, cost, and scalability.

**Study Time:** 2–4 Hours

---

# Part 1: Latency Deep Dive (45 min)

## What is Latency?

Latency = Time taken to complete one request.

Example:

```text
User
 ↓
FastAPI
 ↓
ML Model
 ↓
Prediction
```

If prediction takes:

```text
80 ms
```

then latency = 80 ms.

---

## Types of Latency

### Network Latency

Time spent traveling over the network.

```text
User → Server
```

### Processing Latency

Time spent inside application.

```text
Feature Extraction
Model Prediction
```

### Database Latency

Time spent fetching data.

```sql
SELECT * FROM users
```

---

## Exercise

For a House Price Prediction API:

Estimate latency for:

* Network
* Database
* Model Prediction

Which component is likely slowest?

---

# Part 2: Throughput Deep Dive (45 min)

## What is Throughput?

Number of requests handled per second.

Example:

```text
1000 requests/sec
```

---

## Scenario

Suppose:

```text
1 request = 100 ms
```

One server handles:

```text
10 requests/sec
```

If traffic increases:

```text
1000 requests/sec
```

System must scale.

---

## Scaling Methods

### Vertical Scaling

```text
4 CPU → 16 CPU
```

Bigger machine.

---

### Horizontal Scaling

```text
Server 1
Server 2
Server 3
Server 4
```

More machines.

Preferred in production.

---

## Exercise

Answer:

Why does Netflix prefer horizontal scaling?

---

# Part 3: Latency vs Throughput Trade-offs (30 min)

## Case 1: Fraud Detection

Need:

```text
Very Low Latency
```

Reason:

Transaction approval must be instant.

---

## Case 2: Recommendation System

Need:

```text
High Throughput
```

Can tolerate slightly higher latency.

Recommendations can be precomputed.

---

## Case 3: Stock Trading

Need:

```text
Ultra Low Latency
```

Milliseconds matter.

---

### Exercise

Choose priority:

| System                      | Latency | Throughput |
| --------------------------- | ------- | ---------- |
| YouTube Recommendations     | ?       | ?          |
| Credit Card Fraud Detection | ?       | ?          |
| Uber ETA                    | ?       | ?          |
| Chatbot API                 | ?       | ?          |

Explain your choices.

---

# Part 4: System Bottlenecks (30 min)

## What is a Bottleneck?

The component that limits performance.

Example:

```text
User
 ↓
API
 ↓
Database
 ↓
Model
```

If database is slow:

```text
Database = Bottleneck
```

---

## Common ML Bottlenecks

### Database

Symptoms:

```text
Slow Queries
```

Solution:

```text
Redis Cache
Read Replicas
```

---

### API Layer

Symptoms:

```text
Too Many Requests
```

Solution:

```text
Load Balancer
Multiple API Servers
```

---

### ML Model

Symptoms:

```text
Prediction Too Slow
```

Solution:

```text
Smaller Model
ONNX
TensorRT
GPU
```

---

## Exercise

Analyze bottlenecks in:

```text
Movie Recommendation System
```

Find:

* 3 bottlenecks
* 3 solutions

---

# Part 5: Real Production Example (30 min)

## Design a URL Spam Detection API

Architecture:

```text
User
 ↓
FastAPI
 ↓
Redis Cache
 ↓
Spam Model
 ↓
PostgreSQL
```

---

### Questions

1. What causes latency?
2. Where can caching help?
3. What happens at 10,000 req/sec?
4. What should be scaled first?
5. What should be monitored?

Write answers in your notes.

---

# Mini Interview Round (15 min)

Without notes answer:

1. Difference between latency and throughput?
2. Why is low latency important for fraud detection?
3. What is a bottleneck?
4. Vertical vs horizontal scaling?
5. Why use Redis?
6. How does caching reduce latency?
7. What component usually becomes bottleneck first?
8. Why not always use the largest ML model?

---

# End of Day 2 Deliverable

Create a document containing:

### Notes

* Latency
* Throughput
* Vertical Scaling
* Horizontal Scaling
* Bottlenecks

### Exercises

* House Price API latency analysis
* Netflix scaling answer
* Latency vs Throughput table
* Movie Recommendation bottleneck analysis
* URL Spam Detection system analysis

### Interview Questions

Answer all 8 questions without looking at notes.

By the end of Day 2, you should be able to discuss performance, scaling, and bottlenecks like a junior ML Systems Engineer.
