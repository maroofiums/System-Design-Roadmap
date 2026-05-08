# Day 1 - Scalability Fundamentals

## Goal

Understand how systems handle increasing traffic and why single-server applications eventually fail.

---

## What is Scalability?

Scalability means a system's ability to handle increasing users, requests, and data without major performance issues.

### Example

```text
100 users → system works fine
10,000 users → system slows down/crashes
```

A scalable system should maintain performance as demand grows.

---

# Vertical Scaling (Scale Up)

Increasing resources of a single machine.

### Example

```text
4GB RAM → 32GB RAM
2 CPU cores → 16 CPU cores
```

## Advantages

* Easy to implement
* No architecture changes required
* Good for early-stage startups

## Disadvantages

* Expensive
* Hardware limitations
* Single point of failure

---

# Horizontal Scaling (Scale Out)

Adding multiple servers instead of upgrading one machine.

### Example

```text
Server 1
Server 2
Server 3
Server 4
```

## Advantages

* Better fault tolerance
* Handles massive traffic
* Flexible scaling

## Disadvantages

* More complex architecture
* Requires load balancing
* Data consistency issues

---

# Common System Bottlenecks

## CPU Bottleneck

Heavy computations consume CPU resources.

Examples:

* ML inference
* Data processing

```text
Request → Model Prediction → CPU spikes
```

---

## Memory Bottleneck

Large models or datasets consume too much RAM.

```text
Large ML model → High RAM usage
```

---

## Network Bottleneck

Too many requests overload network bandwidth.

Examples:

* File uploads
* Video streaming
* API traffic spikes

---

## Database Bottleneck

Too many reads/writes slow database performance.

```text
Millions of queries → slow response
```

---

# How Your ML API Might Fail

Current architecture:

```text
User → FastAPI → ML Model → Database
```

Possible failure points:

* Slow model inference
* Database overload
* Server crashes due to high traffic

---

# Solution Evolution

```text
Step 1 → Vertical scaling
Step 2 → Load Balancer
Step 3 → Multiple servers
Step 4 → Caching
Step 5 → Database optimization
```

---

# Task

Analyze your ML API:

* How many requests can it handle?
* Where is the bottleneck?
* CPU?
* Memory?
* Database?
* Network?

Write your findings.

---

# Outcome

After completing Day 1, you should understand:

* Why systems fail under scale
* Vertical vs horizontal scaling
* Common bottlenecks
* How scalable architectures evolve

---

## Real-World Relevance

This directly applies to:

* FastAPI backends
* ML inference APIs
* GenAI applications
* SaaS products

Before learning advanced distributed systems, mastering these fundamentals is critical.
