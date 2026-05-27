import pandas as pd
import os
from datetime import datetime

os.makedirs("data",exist_ok=True)

METRICS_FILES = "data/metrics.csv"

if (
    not os.path.exists(METRICS_FILES)
    or
    os.path.getsize(METRICS_FILES) == 0
):
    df = pd.DataFrame(columns=[
        "timestamp",
        "latency",
        "status"
    ])

    df.to_csv(METRICS_FILES,index=False)

def save_metrics(latency,status):

    metrics ={
        "timestamp":datetime.now(),
        "latency": latency,
        "status": status
    }

    df = pd.DataFrame([metrics])

    df.to_csv(
        METRICS_FILES,
        mode='a',
        header=False,
        index=False
    )