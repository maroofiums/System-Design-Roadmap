# Day 7 - Mini Project: Scalable ML API

## Goal
Build a practical backend system that combines all scalability concepts learned throughout the week.

---

## Architecture

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

---

## Features

### 1. Redis Caching
- Cache repeated predictions
- Reduce latency
- Lower model computation cost

---

### 2. Database Optimization
- Add indexes
- Avoid SELECT *
- Optimize slow queries

---

### 3. Response Time Monitoring
Track:
- Average latency
- Slow endpoints
- Cache hit rate

Example:

```python
start_time = time.time()
# prediction logic
print(time.time() - start_time)
````

---

### 4. Logging

Track:

* API requests
* Errors
* Cache hits/misses
* Database failures

Example:

```python
import logging
logging.info("Prediction request received")
```

---

## Load Testing

Tools:

* Locust
* Apache JMeter

Test:

* 100 users
* 1000 users
* Response degradation

---

## Tech Stack

* FastAPI
* Redis
* PostgreSQL
* Docker

---

## Folder Structure

```
├── app
│   ├── cache.py
│   ├── database.py
│   ├── logger.py
│   ├── main.py
│   ├── model.py
│   └── routes.py
├── tests
│   └── test_api.py
├── Readme.md
├── docker-compose.yml
└── requirements.txt
```
---

## Outcome

After completing this project:

* You understand scalable backend architecture
* You can optimize ML APIs
* You can handle traffic growth
* You’re closer to production-ready backend/ML engineering
