from fastapi import APIRouter
from app.model import predict_price
from app.cache import get_cache, set_cache
from app.logger import logger
import time

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    start = time.time()

    key = str(data)

    cached_result = get_cache(key)

    if cached_result:
        logger.info("Cache Hit")
        return {
            "prediction": cached_result,
            "source":"cache"
        }
    
    result = predict_price(data)
    set_cache(key,result)

    end = time.time()

    logger.info("Model Prediction Executed")

    return {
        "prediction":result,
        "source":"model",
        "response_time": end - start
    }

