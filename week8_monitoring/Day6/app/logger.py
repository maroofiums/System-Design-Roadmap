import logging
import os

os.makedirs("logs", exist_ok=True)

app_logger = logging.getLogger("app_logger")
app_logger.setLevel(logging.INFO)
app_handler = logging.FileHandler(
    "logs/app.log"
)
app_logger.addHandler(app_handler)

prediction_logger = logging.getLogger("prediction_logger")
prediction_logger.setLevel(logging.INFO)
prediction_handler = logging.FileHandler(
    "logs/prediction.log"
)
prediction_logger.addHandler(prediction_handler)

metrics_logger = logging.getLogger("metrics_logger")
metrics_logger.setLevel(logging.INFO)
metrics_handler = logging.FileHandler(
    "logs/metrics.log"
)
metrics_logger.addHandler(metrics_handler)

error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.INFO)
error_handler = logging.FileHandler(
    "logs/error.log"
)
error_logger.addHandler(error_handler)
