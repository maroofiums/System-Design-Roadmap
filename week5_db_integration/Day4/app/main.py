from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import joblib

from database import SessionLocal, engine
from models import Base, Prediction
from schemas import IrisInput

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# load trained model
model = joblib.load("iris_model.pkl")

species_map = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Iris Prediction API Running"}


@app.post("/predict")
def predict_flower(data: IrisInput, db: Session = Depends(get_db)):
    
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    
    pred = model.predict(features)[0]
    flower_name = species_map[pred]

    # store prediction in DB
    db_prediction = Prediction(
        sepal_length=data.sepal_length,
        sepal_width=data.sepal_width,
        petal_length=data.petal_length,
        petal_width=data.petal_width,
        prediction=flower_name
    )

    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)

    return {
        "prediction": flower_name,
        "saved_id": db_prediction.id
    }