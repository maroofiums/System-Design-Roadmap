# Week 6 - System Design Basics

## Goal

Understand how to build scalable backend systems and optimize ML APIs for real-world usage.

---

## Day 1 - Scalability Fundamentals

### Topics

* What is scalability?
* Vertical Scaling (Scale Up)
* Horizontal Scaling (Scale Out)
* System bottlenecks (CPU, Memory, Network)

### Notes

* Vertical scaling = increasing power of a single machine
* Horizontal scaling = adding more machines
* Horizontal scaling is preferred for large systems

### Task

* Write when to use vertical vs horizontal scaling
* Analyze your ML API: where will it break first?

---

## Day 2 - Load Balancing

### Topics

* What is a Load Balancer?
* Traffic distribution strategies:

  * Round Robin
  * Least Connections
  * IP Hash

### Architecture

```
Users → Load Balancer → Multiple API Servers
```

### Task

* Run multiple FastAPI instances locally
* Understand how traffic could be distributed

---

## Day 3 - Caching (Redis)

### Topics

* What is caching?
* Cache hit vs cache miss
* Redis basics (key-value store, TTL)

### Architecture

```
Request → Cache → (if miss) → DB / ML Model
```

### Task

* Add Redis caching to ML API
* Cache prediction results
* Measure latency before/after caching

---

## Day 4 - Database Optimization

### Topics

* Database bottlenecks
* Indexing
* Query optimization
* Connection pooling

### Example

```sql
CREATE INDEX idx_email ON users(email);
```

### Task

* Optimize your queries
* Avoid SELECT *

---

## Day 5 - Replication

### Topics

* Primary (write) vs Replica (read)
* Read-heavy systems
* Eventual consistency

### Architecture

```
App → Primary DB (writes)
App → Replica DB (reads)
```

### Task

* Draw system diagram with replicas

---

## Day 6 - Sharding

### Topics

* Database partitioning
* Shard keys
* Horizontal data scaling

### Example

```
Users A-M → DB1
Users N-Z → DB2
```

### Task

* Design a sharding strategy for users table

---

## Day 7 - Mini Project: Scalable ML API

### Architecture

```
User
 ↓
Load Balancer
 ↓
FastAPI Servers
 ↓
Redis Cache
 ↓
Database
 ↓
ML Model
```

### Features

* Add caching (Redis)
* Optimize database queries
* Measure response time
* Logging

### Bonus

* Load testing using Locust or JMeter

---

## Outcome

After completing this week, you will:

* Understand how systems scale
* Build optimized backend APIs
* Improve ML API performance
* Be ready for real-world backend + AI systems

---

## Notes

Focus on practical implementation. Avoid deep distributed systems theory for now.
