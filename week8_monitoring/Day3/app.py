import os
import time
import pandas as pd

from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

PREDICTION_FILE = "prediction_logs.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(PREDICTION_FILE):

    df = pd.DataFrame(columns=[
        "timestamp",
        "latency",
        "value",
        "prediction",
        "status"
    ])

    df.to_csv(PREDICTION_FILE, index=False)


@app.get("/predict")
def predict(value: int):

    start = time.time()

    prediction = None

    try:
        prediction = "positive" if value > 5 else "negative"

        status = "success"

        return_data = {
            "input": value,
            "prediction": prediction
        }

    except Exception as e:

        status = "failed"

        return_data = {
            "error": str(e)
        }

    end = time.time()

    latency = end - start

    metric = {
        "timestamp": str(datetime.now()),
        "latency": latency,
        "value": value,
        "prediction": prediction,
        "status": status
    }

    df = pd.DataFrame([metric])

    df.to_csv(
        PREDICTION_FILE,
        mode="a",
        index=False,
        header=False
    )

    return return_data