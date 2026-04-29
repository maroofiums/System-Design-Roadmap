from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
import joblib

app = FastAPI(
    title="Iris Prediction API",
    description="Predict Iris flower species using trained ML model",
    version="1.0.0"
)

model = joblib.load("iris_model.pkl")

flower_names = ["Setosa", "Versicolor", "Virginica"]

class IrisInput(BaseModel):
    sepal_length: float = Field(..., gt=0, example=5.1)
    sepal_width: float = Field(..., gt=0, example=3.5)
    petal_length: float = Field(..., gt=0, example=1.4)
    petal_width: float = Field(..., gt=0, example=0.2)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Iris Prediction API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "success",
        "service": "healthy"
    }

@app.get("/classes")
def classes():
    return {
        "status": "success",
        "classes": flower_names
    }

@app.post("/predict")
def predict(data: IrisInput):
    try:
        features = [[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]]

        prediction = model.predict(features)[0]

        confidence = None

        # If model supports probability
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(features)[0]
            confidence = round(float(max(probs)), 4)

        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "prediction_class": int(prediction),
                "prediction_name": flower_names[prediction],
                "confidence": confidence
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "Prediction failed",
                "details": str(e)
            }
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
