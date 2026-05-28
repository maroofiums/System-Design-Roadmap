# 🚀 Day7 - Monitored ML Production System

A production-style Machine Learning monitoring system built with FastAPI that demonstrates:

* Real-time API monitoring
* Prediction tracking
* Data drift detection
* Concept drift / performance degradation alerts
* Latency & error monitoring
* Structured logging
* Lightweight observability pipeline

This project simulates how modern ML systems are monitored after deployment in real-world production environments.

---

# 📌 Project Overview

This system exposes a FastAPI prediction API and continuously monitors:

* API latency
* Error rates
* Prediction outputs
* Data drift
* Concept drift
* Rolling model accuracy

The project is designed as a lightweight MLOps portfolio project for learning production ML monitoring concepts.

---

# 🏗️ Tech Stack

* FastAPI
* Uvicorn
* Pandas
* NumPy
* SciPy
* Pydantic

---

# 📂 Project Structure

```bash
project/
│
├── app/
│   ├── main.py               # FastAPI application
│   ├── logger.py             # Logging utilities
│   ├── metrics.py            # Runtime metrics tracking
│   ├── drift.py              # Data drift detection
│   ├── performance.py        # Performance monitoring
│
├── logs/
│   ├── app.log
│   ├── prediction.log
│   ├── metrics.csv
│
├── dashboard.py              # Live monitoring dashboard
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <your-repo-url>
cd monitored-ml-system
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

## Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

API will run at:

```bash
http://127.0.0.1:8000
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoints

## POST `/predict`

Runs mock ML inference.

### Request

```json
{
  "feature1": 52.3,
  "feature2": 24.1
}
```

### Response

```json
{
  "prediction": 1,
  "status": "success"
}
```

---

## GET `/monitor/drift`

Checks for statistical data drift using the Kolmogorov-Smirnov test.

### Example Response

```json
{
  "status": "success",
  "drift_detected": false,
  "metrics": {
    "feature1": {
      "p_value": 0.42,
      "drift": false
    }
  }
}
```

---

## GET `/monitor/performance`

Monitors rolling model accuracy and concept drift.

### Example Response

```json
{
  "status": "success",
  "rolling_accuracy": 0.88,
  "performance_alarm": false
}
```

---

# 📊 Monitoring Features

## ✅ Prediction Tracking

Every inference request is logged into:

```bash
logs/prediction.log
```

Tracked fields:

* Timestamp
* Features
* Prediction output

---

## ✅ Latency Monitoring

API response latency is stored in:

```bash
logs/metrics.csv
```

Metrics include:

* Request latency
* Status codes
* Request timestamps

---

## ✅ Error Monitoring

System exceptions are logged into:

```bash
logs/app.log
```

---

## ✅ Data Drift Detection

Uses the Kolmogorov-Smirnov statistical test to compare:

* Baseline training distribution
* Recent production traffic

Drift alert triggers when:

```python
p_value < 0.05
```

---

## ✅ Performance Monitoring

Simulates downstream feedback loops by calculating:

* Rolling accuracy
* Concept drift
* Accuracy degradation alerts

Alert threshold:

```python
accuracy < 80%
```

---

# 🖥️ Live Monitoring Dashboard

Run dashboard:

```bash
python dashboard.py
```

Dashboard displays:

* Total requests
* Average latency
* P95 latency
* Error rate
* SLA breach alerts

Example:

```bash
📊 Live Performance Monitoring Dashboard

⏱️ Total Handled Requests : 250
⚡ Average API Latency     : 12.31 ms
🚀 95th Percentile Latency : 28.10 ms
❌ System Error Rate       : 0.80%
```

---

# 📈 Production Concepts Demonstrated

This project demonstrates several real-world MLOps concepts:

| Feature                 | Purpose                       |
| ----------------------- | ----------------------------- |
| Structured Logging      | Production observability      |
| Latency Monitoring      | API performance tracking      |
| Error Tracking          | Reliability monitoring        |
| Data Drift Detection    | Distribution shift monitoring |
| Concept Drift Detection | Model degradation detection   |
| Rolling Accuracy        | Online evaluation             |
| FastAPI Deployment      | Production inference serving  |

---

# 🧠 Future Improvements

Possible production upgrades:

* PostgreSQL logging backend
* Prometheus metrics integration
* Grafana dashboards
* Docker containerization
* CI/CD pipelines
* Real ML model integration
* Alerting via Slack/Email
* Kubernetes deployment
* MLflow model registry
* Redis caching

---

# 📚 Learning Outcomes

By building this project, you practice:

* Production ML system design
* ML observability
* API deployment
* Monitoring pipelines
* Drift detection
* Logging architecture
* Backend engineering
* MLOps fundamentals

---

# 📝 License

This project is open-source and available for educational purposes.

--