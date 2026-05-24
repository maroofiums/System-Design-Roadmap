# Day 3 - Monitoring API Performance

## Overview

This project demonstrates how to monitor API performance in a Machine Learning system using FastAPI.

The API tracks:

* Prediction latency
* Request status
* Input values
* Predictions
* Timestamps

All monitoring metrics are stored inside a CSV file for analysis.

---

# Concepts Learned

## API Monitoring

Monitoring helps ensure that deployed ML systems are:

* Fast
* Stable
* Reliable

---

## Important Production Metrics

### Response Time / Latency

Time taken to return prediction.

Latency = t_{response} - t_{request}

---

### Throughput

Number of requests handled per second.

---

### Failure Rate

Percentage of failed requests.

Failure\ Rate = \frac{Failed\ Requests}{Total\ Requests}

---

### Uptime

Amount of time the API remains available.

---

# Technologies Used

* Python
* FastAPI
* Pandas

---

# Project Structure

```text
ml_monitoring/
│
├── app.py
├── prediction_logs.csv
```

---

# Features

* FastAPI prediction endpoint
* Latency tracking
* CSV metric storage
* Timestamp logging
* Success/failure tracking

---

# API Endpoint

## Predict Endpoint

```text
/predict?value=10
```

### Example Response

```json
{
    "input": 10,
    "prediction": "positive"
}
```

---

# Logging Format

The API stores metrics inside:

```text
prediction_logs.csv
```

## Columns

```text
timestamp
latency
value
prediction
status
```

---

# Example CSV Output

```csv
timestamp,latency,value,prediction,status
2026-05-23 12:01:10,0.0012,10,positive,success
2026-05-23 12:01:15,0.0015,2,negative,success
```

---

# Implementation Details

## Latency Tracking

The API measures request processing time using:

```python
start = time.time()

# prediction logic

end = time.time()

latency = end - start
```

---

## Prediction Logic

```python
prediction = (
    "positive"
    if value > 5
    else "negative"
)
```

---

## CSV Monitoring Pipeline

Metrics are appended continuously:

```python
df.to_csv(
    PREDICTION_FILE,
    mode="a",
    index=False,
    header=False
)
```

---

# Run the Project

## Install Requirements

```bash
pip install fastapi uvicorn pandas
```

---

## Start Server

```bash
uvicorn app:app --reload
```

---

# Test API

Open in browser:

```text
http://127.0.0.1:8000/predict?value=10
```

---

# What This Project Demonstrates

* API performance monitoring
* Basic ML observability
* Latency measurement
* Monitoring pipeline design
* Real-world production concepts

---

# Future Improvements

Possible upgrades:

* Logging system
* Error monitoring
* Drift detection
* Prometheus integration
* Grafana dashboard
* Real-time monitoring
* Database storage
* Docker deployment

---

# Learning Outcome

After completing this project, you understand:

* How production APIs are monitored
* How latency is measured
* How metrics are stored
* How monitoring pipelines work in ML systems
