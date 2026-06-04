import joblib
import os

def save_model(model):
    os.makedirs("models",exist_ok=True)

    path = os.path.join("models","iris_model.pkl")

    joblib.dump(model,path)

    return path