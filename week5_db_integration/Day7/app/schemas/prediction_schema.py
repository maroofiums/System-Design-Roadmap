from pydantic import BaseModel
from datetime import datetime


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class HistoryResponse(BaseModel):
    id: int
    prediction: str
    created_at: datetime

    class Config:
        from_attributes = True