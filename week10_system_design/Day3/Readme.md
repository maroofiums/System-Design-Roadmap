# Day 3 - Recommendation System Design

## Goal

Understand how companies like Netflix and YouTube build recommendation systems that serve millions of users.

---

# Step 1: Understand the Recommendation Pipeline

Recommendation systems usually have two parts:

## Offline Layer (Training)

Runs every few hours or daily.

Purpose:

* Collect user activity
* Train recommendation models
* Generate embeddings/features

---

## Online Layer (Serving)

Runs in real time.

Purpose:

* Serve recommendations instantly
* Handle millions of users
* Keep latency low

---

# Movie Recommendation System Architecture

```text
                 ┌──────────────────┐
                 │      Users       │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ User Interactions│
                 │ Clicks, Ratings  │
                 │ Watch History    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   Data Storage   │
                 │ PostgreSQL/S3    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  Feature Store   │
                 │ User Features    │
                 │ Movie Features   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Training Pipeline│
                 │ Feature Engg.    │
                 │ Model Training   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Recommendation   │
                 │      Model       │
                 └────────┬─────────┘
                          │
                Deploy Model
                          │
                          ▼
                 ┌──────────────────┐
                 │ FastAPI Service  │
                 └────────┬─────────┘
                          │
                Check Cache First
                          │
                          ▼
                 ┌──────────────────┐
                 │      Redis       │
                 │ Top Suggestions  │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Recommended      │
                 │ Movies Returned  │
                 └──────────────────┘
```

---

# Component Explanation

## 1. Users

Users interact with the platform.

Examples:

* Watch movie
* Like movie
* Search movie
* Rate movie

Input:

```text
User actions
```

Output:

```text
Interaction logs
```

---

## 2. Interaction Logs

Stores user behavior.

Example:

```json
{
  "user_id": 101,
  "movie_id": 45,
  "action": "watch",
  "watch_time": 120
}
```

Why important?

Recommendations are based on behavior.

---

## 3. Data Storage

Possible choices:

* PostgreSQL
* MongoDB
* S3

Stores:

* User data
* Movie data
* Interaction logs

---

## 4. Feature Store

Stores processed features.

### User Features

```text
Favorite Genre = Action
Average Watch Time = 90 min
```

### Movie Features

```text
Genre = Action
Year = 2025
Rating = 8.5
```

Purpose:

Avoid recomputing features repeatedly.

---

## 5. Training Pipeline

Tasks:

### Data Cleaning

Remove bad data.

### Feature Engineering

Create useful features.

Example:

```text
Movies watched in last 7 days
```

### Model Training

Possible algorithms:

* Collaborative Filtering
* Matrix Factorization
* Neural Recommendation Systems

Output:

```text
Trained recommendation model
```

---

## 6. Recommendation Model

Learns patterns like:

```text
Users who watched
Avengers

also watched

Iron Man
Captain America
Thor
```

Produces:

```text
Top N recommendations
```

---

## 7. FastAPI Service

Exposes model to users.

Example:

```python
POST /recommend
```

Request:

```json
{
  "user_id": 101
}
```

Response:

```json
{
  "movies": [
    "Interstellar",
    "Inception",
    "Tenet"
  ]
}
```

---

## 8. Redis Cache

Most requested recommendations stored here.

Example:

```text
User 101
→ Cached Recommendations
```

Without Redis:

```text
Model runs every request
```

With Redis:

```text
Return instantly
```

Benefits:

* Lower latency
* Lower compute cost
* Higher throughput

---

# Offline vs Online Workflow

## Offline Training

Runs daily.

```text
Logs
 ↓
Feature Engineering
 ↓
Training
 ↓
Evaluation
 ↓
Deploy Model
```

---

## Online Serving

Runs continuously.

```text
User Request
 ↓
Redis
 ↓
FastAPI
 ↓
Recommendation Model
 ↓
Recommendations
```

---

# Major Bottlenecks

## 1. Huge User Base

Problem:

```text
100 Million Users
```

Millions of recommendation requests.

Solution:

```text
Load Balancer
Horizontal Scaling
```

---

## 2. Expensive Ranking Models

Problem:

Deep learning recommenders can be slow.

Solution:

Two-stage retrieval:

```text
Candidate Generation
 ↓
Ranking Model
```

Instead of ranking every movie.

---

## 3. Cold Start Problem

Problem:

New user has no history.

Example:

```text
User signs up today
```

No data available.

Solution:

Use:

* Popular movies
* Trending movies
* Ask onboarding questions

Example:

```text
Which genres do you like?
```

---

# System Design Trade-offs

| Choice              | Advantage              | Disadvantage        |
| ------------------- | ---------------------- | ------------------- |
| Bigger Model        | Better accuracy        | Higher latency      |
| Redis Cache         | Faster responses       | Extra memory cost   |
| Frequent Retraining | Better recommendations | Higher compute cost |
| More Features       | Better personalization | More complexity     |

---

# Interview Questions

1. Why use Redis in recommendation systems?
2. What is the cold start problem?
3. Why separate offline training from online serving?
4. Why not retrain on every request?
5. What is candidate generation?
6. Why use a feature store?
7. How would you scale to 100 million users?
8. What is the biggest bottleneck in recommendation systems?

---

# Deliverable

Create a 2–3 page System Design Document containing:

1. Architecture Diagram
2. Component Explanations
3. Offline Training Flow
4. Online Serving Flow
5. Bottlenecks
6. Solutions
7. Trade-offs
8. Answers to the 8 interview questions