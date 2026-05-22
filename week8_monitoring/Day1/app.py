from fastapi import FastAPI
import pandas as pd
from datetime import datetime
import os

app = FastAPI()

LOG_FILE = "prediction_logs.csv"

if not os.path.exists(LOG_FILE):
    df = pd.DataFrame(columns=[
        "timestamp",
        "input",
        "prediction",
    ])

    df.to_csv(LOG_FILE,index=False)

@app.get("/predict")
def predict(value: int):
    prediction = "positive" if value > 5 else "negative"

    log = {
        "timestamp":datetime.now(),
        "input": value,
        "prediction":prediction
    }

    df = pd.DataFrame([log])

    df.to_csv(
        LOG_FILE,
        mode="a",
        header=False,
        index=False,
    )

    return {
        "input":value,
        "prediction":prediction
    }