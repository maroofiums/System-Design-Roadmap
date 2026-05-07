import pickle
import numpy as np


with open("app/ml_model/iris_model.pkl", "rb") as file:
    model = pickle.load(file)


species = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}


def predict_flower(data):
    input_data = np.array([
        [
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]
    ])

    prediction_index = model.predict(input_data)[0]

    return species[prediction_index]