import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure main application logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("ml_app")

# Configure a dedicated logger for structured prediction tracking
pred_logger = logging.getLogger("prediction_tracker")
pred_handler = logging.FileHandler("logs/prediction.log")
pred_handler.setFormatter(logging.Formatter("%(message)s"))
pred_logger.addHandler(pred_handler)
pred_logger.setLevel(logging.INFO)

def log_prediction(timestamp: float, inputs: list, prediction: int):
    """Logs structured prediction events as CSV lines."""
    input_str = ",".join(map(str, inputs))
    pred_logger.info(f"{timestamp},{input_str},{prediction}")

    