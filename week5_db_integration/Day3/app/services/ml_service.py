import joblib
import os

model = None


def load_model():
    global model

    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(current_dir, "iris_model.pkl")

    print(f"Loading model from: {model_path}")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    model = joblib.load(model_path)
    print("Model loaded successfully")


def predict_flower(features):
    prediction = int(model.predict([features])[0])

    flower_map = {
        0: "setosa",
        1: "versicolor",
        2: "virginica"
    }

    return prediction, flower_map[prediction]