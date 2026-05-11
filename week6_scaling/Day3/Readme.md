# Day 3 - Caching (Redis)

## Goal

Understand how caching improves API performance by reducing repeated computation and database load.

---

## What is Caching?

Caching is the process of storing frequently used data in a fast-access storage layer so future requests can be served faster.

Instead of recomputing or querying the database every time, we reuse stored results.

---

## Cache Hit vs Cache Miss

### Cache Hit

When requested data is found in cache.

```text
Request → Cache → Response (FAST)
```

### Cache Miss

When requested data is NOT in cache.

```text
Request → Cache (miss) → DB / ML Model → Store in Cache → Response
```

---

## Why Caching Matters

Without caching:

* Every request hits ML model or database
* High latency
* High CPU usage

With caching:

* Repeated requests are served instantly
* Reduced load on ML model and database
* Lower cost and better scalability

---

## Redis Basics

We use entity["software","Redis"] as an in-memory key-value store for caching.

### Key Concepts

* Key-Value Store

  * Example: `"user_1_prediction" → "result"`

* TTL (Time To Live)

  * Expiration time for cached data
  * Example: cache expires after 60 seconds

---

## Architecture with Caching

```text
Request
   ↓
Cache (Redis)
   ↓ (miss)
Database / ML Model
   ↓
Store result in Cache
   ↓
Response
```

---

## How Caching Helps ML APIs

In ML systems:

* Same inputs often repeat
* Model inference is expensive

Example:

* Input: "house price prediction features"
* Instead of re-running model, return cached result

---

## Task

### 1. Integrate Redis into ML API

* Connect FastAPI with Redis
* Store prediction results using a unique key

---

### 2. Cache Prediction Results

Example logic:

* Input → Generate hash key
* Check Redis
* If exists → return cached result
* If not → run model → store result

---

### 3. Measure Performance

Compare:

* Without caching → latency higher
* With caching → near instant response

Track:

* Response time
* CPU usage
* Number of model calls

---

## Outcome

After this day you should understand:

* What caching is and why it matters
* Difference between cache hit and miss
* How Redis works as a caching layer
* How caching improves ML API performance

---