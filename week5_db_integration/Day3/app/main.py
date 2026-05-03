from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import IrisData
from schemas import IrisRequest, PredictionResponse
from services.ml_service import load_model, predict_flower

app = FastAPI()


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    load_model()


@app.get("/")
def root():
    return {"message": "Welcome to Iris Prediction API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict/", response_model=PredictionResponse)
def predict(data: IrisRequest, db: Session = Depends(get_db)):
    features = [
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]

    prediction, flower_name = predict_flower(features)

    record = IrisData(
        sepal_length=data.sepal_length,
        sepal_width=data.sepal_width,
        petal_length=data.petal_length,
        petal_width=data.petal_width,
        prediction=prediction
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "prediction": prediction,
        "flower_name": flower_name,
        "record_id": record.id
    }


@app.get("/data/")
def get_all_predictions(db: Session = Depends(get_db)):
    records = db.query(IrisData).all()

    return [
        {
            "id": record.id,
            "sepal_length": record.sepal_length,
            "sepal_width": record.sepal_width,
            "petal_length": record.petal_length,
            "petal_width": record.petal_width,
            "prediction": record.prediction
        }
        for record in records
    ]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )