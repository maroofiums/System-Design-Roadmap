from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("iris_model.pkl")

flower_names = ["Setosa", "Versicolor", "Virginica"]

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"status": "success", "message": "API Running"}

@app.post("/predict")
def predict(data: IrisInput):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    pred = model.predict(features)[0]

    return {
        "status": "success",
        "prediction_class": int(pred),
        "prediction_name": flower_names[pred]
    }