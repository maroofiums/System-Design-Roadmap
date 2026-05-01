# Week 5 - Database + API Integration

### Focus: ML Backend Engineering

---

# Day 1 - ORM Foundations

### Goal

Understand how Python talks to a database without raw SQL

### Concepts

* What is ORM
* Why ORM instead of SQL
* SQLAlchemy basics
* Database connection
* Tables as Python classes

### Learn

* Create database (SQLite)
* Setup SQLAlchemy engine + session
* Create a `Prediction` model

👉 Outcome:
You can create a table using Python class

---

# Day 2 - CRUD Operations

### Goal

Learn how to interact with database (core backend skill)

### Concepts

* CRUD (Create, Read, Update, Delete)
* Sessions in SQLAlchemy
* Insert vs Query

### Learn

* Insert data into DB
* Read data from DB
* Basic filtering

👉 Outcome:
You can store and retrieve data manually

---

# Day 3 - FastAPI + ML Integration

### Goal

Connect your ML model with API

### Concepts

* Request/Response flow
* Loading trained model (`.pkl`)
* API endpoint design

### Learn

* Create `/predict` endpoint
* Take input using Pydantic schema
* Return prediction

👉 Outcome:
API gives prediction from model

---

# Day 4 - Store Predictions in DB

### Goal

Make your API persistent (real-world system)

### Concepts

* Combining API + DB
* Data flow after prediction

### Learn

* After prediction → save to DB
* Store:

  * input data
  * prediction
  * timestamp

👉 Outcome:
Every API request is saved in database

---

# Day 5 - Build History API

### Goal

Retrieve stored data like real applications

### Concepts

* Querying database
* Serialization (DB → JSON)

### Learn

* Create `/history` endpoint
* Return all predictions
* Format clean JSON response

👉 Outcome:
You can see past predictions

---

# Day 6 - Query Optimization Basics

### Goal

Make your system efficient

### Concepts

* Filtering queries
* Limiting results
* Indexing basics
* Avoiding heavy queries

### Learn

* Add:

  * limit (last 10 results)
  * date filtering
* Optimize DB queries

👉 Outcome:
Efficient and scalable API

---

# Day 7 - Final Project Build

### Goal

Combine everything into a clean system

### Concepts

* Project structure
* Clean architecture
* Separation of concerns

### Learn

* Organize:

  * models
  * schemas
  * database
  * routes
* Test full system

👉 Outcome:
Production-style ML backend system

---

# Final System You Build

```
User → API → ML Model → Prediction
                    ↓
                Database
                    ↓
              History API
```

---

