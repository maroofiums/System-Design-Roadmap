from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

@app.get('/')  
def home():
    return {'message': 'Welcome to the Iris Prediction API!'}

class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

model = joblib.load('iris_model.pkl')

def predict(iris: Iris):
    data = [[
        iris.sepal_length,
        iris.sepal_width,
        iris.petal_length,
        iris.petal_width
    ]]
    prediction = model.predict(data)
    return prediction[0]

def predict_probability(iris: Iris):
    data = [[
        iris.sepal_length,
        iris.sepal_width,
        iris.petal_length,
        iris.petal_width
    ]]
    probabilities = model.predict_proba(data)
    return probabilities[0]

@app.post('/predict')
def predict_iris(iris: Iris):
    result = predict(iris)
    return {'prediction': result}

@app.post('/predict/probability')
def predict_iris_probability(iris: Iris):
    probabilities = predict_probability(iris)
    return {'probabilities': probabilities}

def test():
    test_iris = Iris(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2)
    print(predict(test_iris))
    print(predict_probability(test_iris))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8100)

    