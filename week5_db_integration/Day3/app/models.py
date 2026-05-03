from sqlalchemy import Column, Integer, Float
from database import Base


class IrisData(Base):
    __tablename__ = "iris_data"

    id = Column(Integer, primary_key=True, index=True)
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)
    prediction = Column(Integer)