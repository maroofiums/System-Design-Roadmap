import os
import joblib


def save_model(model):
    model_dir = "models"

    os.makedirs(model_dir, exist_ok=True)

    existing_models = [
        f for f in os.listdir(model_dir)
        if f.startswith("iris_model_") and f.endswith(".pkl")
    ]

    version = len(existing_models) + 1

    model_path = os.path.join(
        model_dir,
        f"iris_model_{version}.pkl"
    )

    joblib.dump(model, model_path)

    return model_path