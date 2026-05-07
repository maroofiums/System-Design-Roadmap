from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from app.core.database import Base


class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)
    prediction = Column(String, index=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        index=True
    )