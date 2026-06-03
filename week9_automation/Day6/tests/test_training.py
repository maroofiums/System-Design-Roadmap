from src.data_loader import load_data
from src.evaluator import evaluate_model
from src.trainer import train_model

def test_model_training():
    X_train, X_test, y_train, y_test = load_data()
    
    model,parameters = train_model(X_train, y_train)

    metrics = evaluate_model(model, X_test, y_test)

    assert metrics['accuracy'] >= 0.9

    assert "accuracy" in metrics, "Metrics should include accuracy"
    assert "precision" in metrics, "Metrics should include precision"
    assert "recall" in metrics, "Metrics should include recall"
    assert "f1_score" in metrics, "Metrics should include f1_score"

    