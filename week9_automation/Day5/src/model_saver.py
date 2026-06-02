import joblib
import os

def save_model(model, base_dir="models",path_file="iris_model.pkl"):

    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    path = os.path.join(base_dir, path_file)
    joblib.dump(model, path)
    print(f"Model saved to {path}")

    return path
