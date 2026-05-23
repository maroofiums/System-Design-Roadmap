from fastapi import FastAPI
import logging
from datetime import datetime
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

app = FastAPI()

# App logger
app_logger = logging.getLogger("app_logger")
app_logger.setLevel(logging.INFO)
app_handle = logging.FileHandler("logs/app.log")
app_logger.addHandler(app_handle)

# Prediction logger
prediction_logger = logging.getLogger("prediction_logger")
prediction_logger.setLevel(logging.INFO)
prediction_handle = logging.FileHandler("logs/prediction.log")
prediction_logger.addHandler(prediction_handle)

# Error logger
error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)
error_handle = logging.FileHandler("logs/error.log")
error_logger.addHandler(error_handle)

@app.get("/predict")
def predict(value: int):
    try:
        app_logger.info(
            f"Request received at {datetime.now()}"
        )

        prediction = "positive" if value > 5 else "negative"

        prediction_logger.info(
            f"Input: {value}, Prediction: {prediction}"
        )

        if value == 999:
            raise ValueError(f"{datetime.now()} Test error")

        app_logger.info(
            "Prediction completed successfully"
        )

        return {
            "input": value,
            "prediction": prediction,
        }

    except Exception as e:

        error_logger.error(str(e))

        return {
            "error": "Prediction failed"
        }