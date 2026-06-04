import joblib
import os

MODEL_PATH = "models/iris_model.pkl"

current_model = None

def load_model():
    return joblib.load(MODEL_PATH)

def get_model():
    global current_model

    if current_model is None:
        current_model = load_model()

    return current_model

def reload_model():
    global current_model

    current_model = load_model()

    print("Model reloaded")
    