from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime
import pickle
import numpy as np

from database import engine, Base, get_db
from models import PredictionHistory
from schemas import IrisInput

# Create tables
Base.metadata.create_all(bind=engine)

# Load trained model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

# FastAPI app
app = FastAPI(
    title="Iris Prediction API",
    description="ML API with Database Integration",
    version="1.0.0"
)

# Label mapping
species = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}


# Home route
@app.get("/")
def home():
    return {
        "message": "Iris ML API is running"
    }


# Predict endpoint
@app.post("/predict")
def predict(
    data: IrisInput,
    db: Session = Depends(get_db)
):

    input_data = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    prediction_index = model.predict(input_data)[0]
    prediction_label = species[prediction_index]

    # Store prediction in DB
    new_record = PredictionHistory(
        sepal_length=data.sepal_length,
        sepal_width=data.sepal_width,
        petal_length=data.petal_length,
        petal_width=data.petal_width,
        prediction=prediction_label
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return {
        "message": "Prediction saved successfully",
        "prediction": prediction_label
    }


# History endpoint with optimization
@app.get("/history")
def get_history(
    limit: int = Query(10, ge=1),
    species_name: str = None,
    start_date: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(PredictionHistory)

    # Filter by species
    if species_name:
        query = query.filter(
            PredictionHistory.prediction == species_name
        )

    # Filter by date
    if start_date:
        parsed_date = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        )

        query = query.filter(
            PredictionHistory.created_at >= parsed_date
        )

    # Latest records first
    records = query.order_by(
        PredictionHistory.created_at.desc()
    ).limit(limit).all()

    history = []

    for record in records:
        history.append({
            "id": record.id,
            "sepal_length": record.sepal_length,
            "sepal_width": record.sepal_width,
            "petal_length": record.petal_length,
            "petal_width": record.petal_width,
            "prediction": record.prediction,
            "created_at": record.created_at
        })

    return {
        "total_records": len(history),
        "history": history
    }