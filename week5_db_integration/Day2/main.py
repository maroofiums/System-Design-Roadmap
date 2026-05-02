from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()


class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float)
    
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def create_prediction(value):
    new_prediction = Prediction(value=value)
    session.add(new_prediction)
    session.commit()
    print(f"Prediction created with value: {value}")

def read_predictions():
    data = session.query(Prediction).all()
    print("\n Predictions in the database:")
    for prediction in data:
        print(f"Prediction ID: {prediction.id}, Value: {prediction.value}")

def update_prediction(prediction_id, new_value):
    record = session.query(Prediction).filter(
        Prediction.id == prediction_id
    ).first()

    if record:
        record.value = new_value
        session.commit()
        print(f"Prediction with ID {prediction_id} updated to new value: {new_value}")

    else:
        print(f"Prediction with ID {prediction_id} not found.")

def delete_prediction(prediction_id):
    record = session.query(Prediction).filter(
        Prediction.id == prediction_id
    ).first()

    if record:
        session.delete(record)
        session.commit()
        print(f"Prediction with ID {prediction_id} deleted.")

    else:
        print(f"Prediction with ID {prediction_id} not found.")

def filter_predictions(min_value):
    data = session.query(Prediction).filter(
        Prediction.value >= min_value
    ).all()

    print(f"\n Predictions with value greater than or equal to {min_value}:")
    for prediction in data:
        print(f"Prediction ID: {prediction.id}, Value: {prediction.value}")

if __name__ == "__main__":
    create_prediction(0.5)
    create_prediction(0.8)
    create_prediction(0.3)

    read_predictions()

    update_prediction(1, 0.6)

    delete_prediction(2)

    filter_predictions(0.4)
    
