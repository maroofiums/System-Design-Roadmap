import csv
import os
import time

METRICS_FILE = "logs/metrics.csv"

def init_metrics_file():
    if not os.path.exists(METRICS_FILE):
        with open(METRICS_FILE, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "latency", "status_code"])

def log_api_metrics(latency: float, status_code: int):
    """Appends runtime performance metrics to metrics.csv."""
    init_metrics_file()
    with open(METRICS_FILE, mode="w+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time.time(), latency, status_code])