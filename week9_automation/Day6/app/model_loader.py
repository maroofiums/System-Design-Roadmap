import os
import joblib

BASE_DIR = "models"

MODEL_PATH = os.path.join(BASE_DIR, "iris_model.pkl")

current_model = None

def load_model(path=MODEL_PATH):

    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at {path}. Please train the model first.")
    
    return joblib.load(path)

def get_model():
    global current_model

    if current_model is None:
        current_model = load_model()
    
    return current_model

def reload_model():
    global current_model
    try:
       current_model = load_model()
       print("Model reloaded successfully.")
    except FileNotFoundError as e:
        print(e)
        current_model = None
