from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from database import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)

    prediction = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)