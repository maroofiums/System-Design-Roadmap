from fastapi import FastAPI
from pydantic import BaseModel

from app.model_loader import get_model

app = FastAPI()

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def home():
    return {
        "status": "running"
    }


@app.post("/predict")
def predict(data: IrisInput):

    model = get_model()

    prediction = model.predict([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    return {
        "prediction": int(prediction[0])
    }