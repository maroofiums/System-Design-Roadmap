from pydantic import BaseModel
from datetime import datetime


# Input schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Response schema
class PredictionResponse(BaseModel):
    prediction: str


# History response schema
class HistoryResponse(BaseModel):
    id: int
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    prediction: str
    created_at: datetime

    class Config:
        from_attributes = True