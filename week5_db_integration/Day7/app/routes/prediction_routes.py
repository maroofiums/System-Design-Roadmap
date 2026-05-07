from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.database import get_db
from app.models.prediction import PredictionHistory
from app.schemas.prediction_schema import IrisInput
from app.services.model_service import predict_flower

router = APIRouter()


@router.post("/predict")
def predict(data: IrisInput, db: Session = Depends(get_db)):
    prediction_label = predict_flower(data)

    new_record = PredictionHistory(
        sepal_length=data.sepal_length,
        sepal_width=data.sepal_width,
        petal_length=data.petal_length,
        petal_width=data.petal_width,
        prediction=prediction_label
    )

    db.add(new_record)
    db.commit()

    return {
        "prediction": prediction_label
    }


@router.get("/history")
def get_history(
    limit: int = Query(10, ge=1),
    species_name: str = None,
    start_date: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(PredictionHistory)

    if species_name:
        query = query.filter(
            PredictionHistory.prediction == species_name
        )

    if start_date:
        parsed_date = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        )

        query = query.filter(
            PredictionHistory.created_at >= parsed_date
        )

    records = query.order_by(
        PredictionHistory.created_at.desc()
    ).limit(limit).all()

    return records