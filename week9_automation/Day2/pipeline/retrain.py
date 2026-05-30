from src.data_loader import load_data
from src.trainer import train_model
from src.evaluator import evaluate_model
from src.model_saver import save_model

def retrain():
    print("Data Loading...")

    X_train,X_test,y_train,y_test = load_data()

    print("Model Training...")

    model = train_model(X_train,y_train)

    print("Evaluating Model...")

    metrics = evaluate_model(
        model,
        X_test,
        y_test
    )

    print(metrics)

    if metrics["accuracy"] >= 0.90:
        print("Model Saving...")
        save_model(model)
        print("Model Saved...")

    else:
        print("Model Rejected...")


if __name__ == "__main__":
    retrain()