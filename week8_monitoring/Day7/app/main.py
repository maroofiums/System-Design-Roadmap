import time
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field
from app.logger import logger, log_prediction
from app.metrics import log_api_metrics
from app.drift import check_data_drift
from app.performance import evaluate_performance

app = FastAPI(title="Monitored ML Production System", version="1.0.0")

class PredictionRequest(BaseModel):
    feature1: float = Field(..., description="Continuous variable 1", example=52.3)
    feature2: float = Field(..., description="Continuous variable 2", example=24.1)

# Mock model weights for production inference
MOCK_WEIGHTS = [0.6, 0.4]
THRESHOLD = 42.0

@app.post("/predict")
async def predict(payload: PredictionRequest, response: Response):
    start_time = time.time()
    logger.info("Received incoming inference request.")
    
    try:
        # Business logic inference rule
        score = (payload.feature1 * MOCK_WEIGHTS[0]) + (payload.feature2 * MOCK_WEIGHTS[1])
        prediction = 1 if score > THRESHOLD else 0
        
        # Log to structured system files
        log_prediction(start_time, [payload.feature1, payload.feature2], prediction)
        
        latency = time.time() - start_time
        log_api_metrics(latency, 200)
        return {"prediction": prediction, "status": "success"}
        
    except Exception as e:
        latency = time.time() - start_time
        log_api_metrics(latency, 500)
        logger.error(f"Inference pipeline exception: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal inference failure.")

@app.get("/monitor/drift")
async def monitor_drift():
    """Endpoint for checking distribution data drift over time."""
    return check_data_drift()

@app.get("/monitor/performance")
async def monitor_performance():
    """Endpoint for downstream performance tracking and concept changes."""
    return evaluate_performance()