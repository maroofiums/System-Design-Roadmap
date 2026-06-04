from src.data_loader import load_data
from src.trainer import train_model
from src.evaluator import evaluate_model
from src.model_saver import save_model
from src.mlflow_logger import log_experiment

from app.model_loader import reload_model

def retrain_model():
    print("Data Loading...")

    X_train,X_test,y_train,y_test = load_data()

    print("Data Loaded Sucessfully!!!")
    
    print("Model Training...")

    model, params = train_model(X_train,y_train)

    print("Model Trained Sucessfully!!!")
    
    print("Model Evaluating...")

    metrics = evaluate_model(model,X_test,y_test)

    print("Model Evaluated Sucessfully!!!")

    print("Add Logging in MLFlow...")

    log_experiment(
        model,
        params,
        metrics
    )

    print("Add Logged in MLFlow!!!")

    print("Model Selection...")


    if metrics["accuracy"] >= 0.85:
        save_model(model)
        reload_model()

        print(
            "Model Selected!!!"
        )
    else:
        print("Model Rejected!!!")


    return metrics


if __name__ == "__main__":
    retrain_model()
