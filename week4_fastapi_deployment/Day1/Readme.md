# Day 1 - API Basics + FastAPI Intro

## Goal

Understand how APIs work and build your first backend service using FastAPI.

---

# 1. What is an API?

API = **Application Programming Interface**

Simple meaning:

An API lets **two software systems communicate**.

Example:

* Mobile app asks server: "Give user profile"
* Server returns data
* Website asks weather API for forecast
* ML frontend asks backend for prediction

Think of API like a **waiter in a restaurant**:

* Client = customer
* API = waiter
* Server = kitchen

You request food, waiter delivers it.

---

# 2. Client → Server → Response Flow

## Real Flow:

```text
Browser / App / Frontend
        ↓ Request
      Server (FastAPI)
        ↓ Response
Browser gets data
```

## Example:

Client sends:

```http
GET /
```

Server responds:

```json
{
  "message": "Hello"
}
```

---

# 3. HTTP Methods

These define what action client wants.

## GET

Used to **fetch data**

Example:

```http
GET /users
```

Meaning: give me users.

---

## POST

Used to **send data**

Example:

```http
POST /predict
```

With JSON:

```json
{
  "age": 22,
  "income": 50000
}
```

Meaning: use this data.

---

## Common Future Methods

* PUT = update
* DELETE = remove

For now focus GET + POST.

---

# 4. What is JSON?

JSON = JavaScript Object Notation

Used for sending data between systems.

Example:

```json
{
  "name": "Maroof",
  "age": 19
}
```

Python dictionary looks similar:

```python
{
    "name": "Maroof",
    "age": 19
}
```

That’s why Python backend uses JSON easily.

---

# 5. Your First FastAPI App

Install:

```bash
pip install fastapi uvicorn
```

Create file:

```bash
main.py
```

Write:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello"}
```

---

# 6. Code Explanation

## Create App

```python
app = FastAPI()
```

Creates your web application.

---

## Route

```python
@app.get("/")
```

Means:

When user visits `/`

using GET request

run function below.

---

## Function

```python
def home():
```

Runs when route called.

---

## Return Response

```python
return {"message": "Hello"}
```

FastAPI automatically converts it to JSON.

---

# 7. Run Server

```bash
uvicorn main:app --reload
```

## Meaning:

* `main` = filename
* `app` = FastAPI object
* `--reload` = auto restart when code changes

---

# 8. Open Browser

Visit:

```text
http://127.0.0.1:8000/
```

You’ll see:

```json
{"message":"Hello"}
```

---

# 9. Auto Docs (Amazing Feature)

Visit:

```text
http://127.0.0.1:8000/docs
```

FastAPI gives Swagger docs automatically.

You can test APIs there.

---

# 10. Request / Response Lifecycle

```text
1. Browser sends request
2. FastAPI receives request
3. Matching route found
4. Function executes
5. JSON response returned
6. Browser receives result
```

---

# 11. Mini Practice Tasks

## Task 1

Change message:

```python
{"message":"Welcome Maroof"}
```

---

## Task 2

Add new route:

```python
@app.get("/about")
def about():
    return {"about":"My first API"}
```

Visit:

```text
/about
```

---

## Task 3

Add health route:

```python
@app.get("/health")
def health():
    return {"status":"running"}
```

---

# 12. Folder Structure

```text
Day1/
 ├── main.py
```

---

# 13. Common Errors

## Error:

```text
ModuleNotFoundError: fastapi
```

Fix:

```bash
pip install fastapi uvicorn
```

---

## Error:

```text
Could not import module main
```

Fix:

Check filename is `main.py`

---

# 14. Outcome Today

After Day 1 you understand:

* What API is
* How client/server works
* GET request
* JSON response
* FastAPI basics
* Running server

---

# 15. Homework (Important)

Build this:

```python
@app.get("/name")
def name():
    return {"name":"Maroof"}

@app.get("/goal")
def goal():
    return {"goal":"Become ML Engineer"}
```

---