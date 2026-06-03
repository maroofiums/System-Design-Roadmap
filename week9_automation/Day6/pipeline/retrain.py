from src.data_loader import load_data
from src.trainer import train_model
from src.model_saver import save_model
from src.evaluator import evaluate_model_with_report
from app.model_loader import reload_model


def retrain_model():
    print("Loading data...")
    X_train, X_test, y_train, y_test = load_data()

    print("Training model...")
    model, params = train_model(X_train, y_train)

    print("Evaluating model...")
    metrics, cm, report = evaluate_model_with_report(model, X_test, y_test)
    print("Evaluation Metrics:", metrics)
    print("Confusion Matrix:\n", cm)
    print("Classification Report:\n", report)

    if metrics["accuracy"] >= 0.90:

        path = save_model(model)

        print(f"Model Saved: {path}")

        reload_model()

        print("Deployment Updated")

    else:
        print("Model Rejected")


if __name__ == "__main__":
    retrain_model()