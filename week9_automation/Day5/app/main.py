from fastapi import FastAPI
from pydantic import BaseModel

from app.model_loader import get_model

app = FastAPI()

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Prediction API!"}

@app.post("/predict")
def predict(iris: IrisFeatures):
    model = get_model()
    features = [[
        iris.sepal_length,
        iris.sepal_width,
        iris.petal_length,
        iris.petal_width
    ]]
    prediction = model.predict(features)
    return {"predicted_class": int(prediction[0])}

