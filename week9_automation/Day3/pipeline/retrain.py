from src.data_loader import load_data
from src.trainer import train_model
from src.evaluator import evaluate_model
from src.model_saver import save_model


def retrain_model():
    print("Data Loading...")

    X_train, X_test, y_train, y_test = load_data()

    print("Model Training...")

    model = train_model(
        X_train,
        y_train
    )

    print("Evaluating Model...")

    metrics = evaluate_model(
        model,
        X_test,
        y_test
    )

    print("\nMetrics:")
    print("-" * 30)

    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

    print()

    # Save only if model meets threshold
    if metrics["accuracy"] >= 0.90:

        model_path = save_model(model)

        print(f"Model Saved: {model_path}")

    else:
        print("Model Rejected")

    return metrics


if __name__ == "__main__":
    retrain_model()