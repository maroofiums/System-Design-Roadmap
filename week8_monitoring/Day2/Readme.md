# Day 2 - Logging in ML Systems

# What is Logging?

Logging means recording important events happening inside an application.

Logs help developers:

* Debug failures
* Track system behavior
* Monitor APIs
* Detect crashes
* Understand model predictions

Without logs, debugging production systems becomes extremely difficult.

---

# Example

Suppose your prediction API suddenly crashes.

Without logs:

```text
Something failed.
```

With logs:

```text
ERROR: Model file not found
```

Now debugging becomes easy.

---

# Types of Logs

# 1. Application Logs

Track normal system activity.

Examples:

* Server started
* Request received
* Prediction completed

---

# 2. Error Logs

Track failures and exceptions.

Examples:

* File missing
* API crash
* Database connection failed

---

# 3. Prediction Logs

Track ML model predictions.

Examples:

* User input
* Model output
* Timestamp

Useful for:

* Monitoring predictions
* Detecting drift
* Auditing model behavior

---

# Python Logging Module

Python provides a built-in module:

```python
logging
```

---

# Basic Logging Example

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Prediction generated")
```

---

# Explanation

| Part           | Meaning            |
| -------------- | ------------------ |
| filename       | File to store logs |
| level          | Minimum log level  |
| logging.info() | Write INFO message |

---

# Log Levels

| Level    | Meaning             |
| -------- | ------------------- |
| DEBUG    | Detailed debugging  |
| INFO     | Normal events       |
| WARNING  | Suspicious behavior |
| ERROR    | Failure occurred    |
| CRITICAL | System crash        |

---

# Example of Each Log Level

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debugging info")

logging.info("API started")

logging.warning("High latency detected")

logging.error("Prediction failed")

logging.critical("Server crashed")
```

---

# Practice Project

Goal:

Add logging to FastAPI app.

Log:

* Request received
* Prediction completed
* Errors

---

# Project Structure

```text
Day2/
│
├── app.py
│
├── logs/
│   ├── app.log
│   ├── prediction.log
│   └── error.log
```

---

# Step 1 - Create logs Folder

```bash
mkdir logs
```

---

# Step 2 - Build Logging System

## app.py

```python
from fastapi import FastAPI
import logging
from datetime import datetime

app = FastAPI()

# Application logger
app_logger = logging.getLogger("app_logger")

app_logger.setLevel(logging.INFO)

app_handler = logging.FileHandler("logs/app.log")

app_logger.addHandler(app_handler)


# Prediction logger
prediction_logger = logging.getLogger("prediction_logger")

prediction_logger.setLevel(logging.INFO)

prediction_handler = logging.FileHandler(
    "logs/prediction.log"
)

prediction_logger.addHandler(prediction_handler)


# Error logger
error_logger = logging.getLogger("error_logger")

error_logger.setLevel(logging.ERROR)

error_handler = logging.FileHandler(
    "logs/error.log"
)

error_logger.addHandler(error_handler)


@app.get("/predict")

def predict(value: int):

    try:

        # Log request
        app_logger.info(
            f"Request received at {datetime.now()}"
        )

        # Dummy prediction logic
        prediction = (
            "positive"
            if value > 5
            else "negative"
        )

        # Log prediction
        prediction_logger.info(
            f"Input={value}, Prediction={prediction}"
        )

        # Log success
        app_logger.info(
            "Prediction completed successfully"
        )

        return {
            "input": value,
            "prediction": prediction
        }

    except Exception as e:

        # Log error
        error_logger.error(str(e))

        return {
            "error": "Prediction failed"
        }
```

---

# Step 3 - Run Server

```bash
uvicorn app:app --reload
```

---

# Step 4 - Test API

Open:

```text
http://127.0.0.1:8000/predict?value=10
```

---

# Example app.log

```text
Request received at 2026-05-22 12:10:01
Prediction completed successfully
```

---

# Example prediction.log

```text
Input=10, Prediction=positive
Input=2, Prediction=negative
```

---

# Example error.log

```text
ValueError: invalid input
```

---

# Why Logging is Important in ML

# 1. Debugging

Find exact cause of failure.

---

# 2. Monitoring Predictions

Track model behavior over time.

---

# 3. Drift Detection

Analyze changing prediction patterns.

---

# 4. Auditing

Understand what predictions were made.

---

# 5. Production Reliability

Logs are essential for real-world ML systems.

Companies use logging systems heavily in production.

---

# What You Learned Today

## Concepts

* Logging
* Log types
* Log levels
* Error tracking

---

## Practical Skills

* Python logging module
* Multiple log files
* FastAPI logging
* Error handling

---

# Homework

Improve logging system:

Add:

* Request timestamps
* API latency
* User IP
* Response status

---

