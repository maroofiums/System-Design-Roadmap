import joblib 
import os

def save_model(model,path="model/iris_model.pkl"):
    os.makedirs("model",exist_ok=True)

    joblib.dump(model,path)
