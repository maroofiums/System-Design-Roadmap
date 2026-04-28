from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
from pathlib import Path
import uvicorn

app = FastAPI(
    title="Iris Prediction API",
    description="FastAPI service for predicting Iris flower species",
    version="1.0.0"
)

# Load model safely using absolute path
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "iris_model.pkl"

model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Iris Prediction API!"
    }


# Request Schema
class Iris(BaseModel):
    sepal_length: float = Field(
        ...,
        example=5.1,
        gt=0,
        description="Length of sepal in cm"
    )
    sepal_width: float = Field(
        ...,
        example=3.5,
        gt=0,
        description="Width of sepal in cm"
    )
    petal_length: float = Field(
        ...,
        example=1.4,
        gt=0,
        description="Length of petal in cm"
    )
    petal_width: float = Field(
        ...,
        example=0.2,
        gt=0,
        description="Width of petal in cm"
    )


def prepare_data(iris: Iris):
    return [[
        iris.sepal_length,
        iris.sepal_width,
        iris.petal_length,
        iris.petal_width
    ]]


@app.post("/predict")
def predict_iris(iris: Iris):
    try:
        data = prepare_data(iris)
        prediction = model.predict(data)[0]

        return {
            "prediction": str(prediction)
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


@app.post("/predict/probability")
def predict_probability(iris: Iris):
    try:
        data = prepare_data(iris)
        probabilities = model.predict_proba(data)[0].tolist()

        return {
            "probabilities": probabilities
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# Local test
def test():
    sample = Iris(
        sepal_length=5.1,
        sepal_width=3.5,
        petal_length=1.4,
        petal_width=0.2
    )

    print("Prediction:", model.predict(prepare_data(sample))[0])
    print("Probabilities:", model.predict_proba(prepare_data(sample))[0].tolist())


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8100, reload=True)