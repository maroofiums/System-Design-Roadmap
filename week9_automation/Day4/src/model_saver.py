import os
import joblib

def save_model(
    model,
    model_dir="models",
    model_name="random_forest_model.joblib"
):
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, model_name)
    
    joblib.dump(model, model_path)
    
    print(f"Model saved to {model_path}")