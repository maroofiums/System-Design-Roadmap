# Day 6 - Fault Tolerance & Bottleneck Analysis

## Goal

Learn how production ML systems stay available when components fail and how to identify system bottlenecks before they become serious problems.

---

# Part 1: Fault Tolerance

## What is Fault Tolerance?

A system's ability to continue working even when some components fail.

Example:

```text
              Load Balancer
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
 Model Server1  Model Server2  Model Server3
```

If Model Server 2 crashes:

```text
Model Server2 ❌
```

Traffic automatically shifts to:

```text
Model Server1
Model Server3
```

Users still receive recommendations.

---

## Common Fault Tolerance Techniques

### Redundancy

Multiple copies of services.

```text
3 API Servers
3 Model Servers
```

---

### Load Balancer

Distributes traffic across healthy servers.

Examples:

* Nginx
* HAProxy
* Cloud Load Balancers

---

### Database Replication

```text
Primary DB
    │
    ├── Replica 1
    └── Replica 2
```

If one replica fails, others continue serving reads.

---

### Monitoring

Detect failures quickly.

Tools:

* Prometheus
* Grafana

Monitor:

* CPU
* Memory
* Errors
* Latency

---

# Part 2: Bottleneck Analysis

## Key Question

Always ask:

```text
What breaks first?
```

The answer is usually your bottleneck.

---

# Movie Recommendation System

Architecture:

```text
Users
   ↓
FastAPI
   ↓
Redis
   ↓
Recommendation Model
   ↓
PostgreSQL
```

---

# Bottleneck 1 - Database

## Problem

Millions of users request recommendations.

Every request triggers:

```sql
SELECT watch_history
FROM users
```

Database becomes overloaded.

---

## Symptoms

* Slow queries
* High latency
* Database CPU spikes

---

## Solutions

### Redis Cache

Store frequently used recommendations.

```text
User 101
↓
Cached Results
```

No database query required.

---

### Read Replicas

```text
Primary DB
    │
 ┌──┴──┐
 ▼     ▼
Replica1 Replica2
```

Spread read traffic.

---

### Denormalization

Store frequently accessed data together.

Reduce joins.

---

# Bottleneck 2 - Recommendation Model

## Problem

Deep ranking models are expensive.

Example:

```text
Rank 1 Million Movies
```

Too slow.

---

## Symptoms

* High inference latency
* CPU/GPU overload

---

## Solutions

### Candidate Generation

Instead of:

```text
1,000,000 Movies
```

retrieve:

```text
Top 500 Candidates
```

Then rank only those.

---

### Smaller Model

Trade a little accuracy for speed.

---

### More Model Servers

```text
Load Balancer
      │
 ┌────┼────┐
 ▼    ▼    ▼
M1   M2   M3
```

Scale horizontally.

---

# Bottleneck 3 - API Layer

## Problem

Huge traffic spikes.

Example:

```text
New movie release
```

Millions of requests arrive.

---

## Symptoms

* Request timeout
* Server crashes
* High response times

---

## Solutions

### Horizontal Scaling

```text
API1
API2
API3
API4
```

Add more servers.

---

### Load Balancer

Distribute traffic evenly.

---

### Rate Limiting

Prevent abuse.

Example:

```text
100 requests/minute
```

per user.

---

# Fault Tolerance Analysis

## What if Redis Fails?

Fallback:

```text
Redis ❌
   ↓
PostgreSQL
```

System becomes slower but still works.

---

## What if Model Server Fails?

```text
Model 1 ❌
```

Load balancer routes traffic to:

```text
Model 2
Model 3
```

---

## What if Database Replica Fails?

Other replicas continue serving reads.

---

# Final Exercise Answer

## Bottleneck 1

### Database

Problem:

```text
Too many read requests
```

Solutions:

* Redis Cache
* Read Replicas
* Denormalization

---

## Bottleneck 2

### Recommendation Model

Problem:

```text
Slow inference
```

Solutions:

* Candidate Generation
* Smaller Models
* Multiple Model Servers

---

## Bottleneck 3

### API Layer

Problem:

```text
Traffic spikes
```

Solutions:

* Horizontal Scaling
* Load Balancer
* Rate Limiting

---

# Interview Questions

1. What is fault tolerance?
2. Why use a load balancer?
3. What is a bottleneck?
4. How do you identify bottlenecks?
5. Why use read replicas?
6. What happens if Redis crashes?
7. Why not use a huge recommendation model?
8. What breaks first in a recommendation system with 100 million users?

---

# Deliverable

Create a **Movie Recommendation System Reliability Report** containing:

1. System Architecture
2. Fault Tolerance Strategy
3. Three Bottlenecks
4. Three Solutions
5. Failure Scenarios
6. Scaling Strategy
7. Interview Question Answers
