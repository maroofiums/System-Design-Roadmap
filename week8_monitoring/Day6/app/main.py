from fastapi import FastAPI
import time
from datetime import datetime

from app.logger import (
    app_logger,
    prediction_logger,
    error_logger,
    metrics_logger
)

from app.metrics import save_metrics
from dashboards.metrics_summary import compute_request_metrics

app = FastAPI()

@app.get("/predict")
def predict(value: int):
    start = time.time()

    prediction = None
    
    try:
        
        app_logger.info(
            f"Request received: {value}, Route: /predict"
        )

        if value > 25:
            raise ValueError(f"Number {value} is Too large!..")

        prediction = (
            "positive" 
            if value > 5
            else "negative"
        )
        status = "success"

        prediction_logger.info(
            f"Input={value}, Prediction={prediction}"
        )
        
        return_data = {
            "input":value,
            "prediction":prediction
        }

    except Exception as e:
        error_logger.error(str(e))

        status = "failed"

        return_data = {
            "error":str(e)
        }

    end = time.time()

    latency = end  -  start

    save_metrics(latency,status)

    return return_data

@app.get("/summary")
def dashboard(threshold:float = 0.002):
    try:
        return_data = compute_request_metrics(threshold)

        metrics_logger.info({
            "event": "metrics_snapshot",
            "timestamp": str(datetime.now()),
            **return_data,
            "threshold": threshold
        })

        app_logger.info("Metrics endpoint called successfully")

    except Exception as e:
        error_logger.error(str(e))

        return_data = {
            "error":str(e)
        }

    return return_data