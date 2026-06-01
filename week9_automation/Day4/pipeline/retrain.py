from src.data_loader import load_data
from src.model_saver import save_model
from src.trainer import train_model
from src.mlflow_tracker import log_experiment
from src.evaluator import evaluate_model

def retrain_model():

    print("Loading data...")

    X_train, X_test, y_train, y_test = load_data()

    print("Training model...")

    model,params = train_model(X_train, y_train)

    print("Evaluating model...")

    metrics, cm, report = evaluate_model(model, X_test, y_test)

    print("\nMetrics")

    print("-"*30)

    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

    print("\nLogging experiment...")

    log_experiment(model, metrics, params, cm, report)

    if metrics["accuracy"] > 0.9:
        print("\nSaving model...")

        path = save_model(model)   

        print(f"Model saved: {path}")

    else:
        print("\nModel did not meet the accuracy threshold. Not saving.")

if __name__ == "__main__":
    retrain_model()
