from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report
)

def evaluate_model(model, X_test, y_test):
    metrics = {
        "accuracy": accuracy_score(y_test, model.predict(X_test)),
        "precision": precision_score(y_test, model.predict(X_test), average="weighted"),
        "recall": recall_score(y_test, model.predict(X_test), average="weighted"),
        "f1_score": f1_score(y_test, model.predict(X_test), average="weighted"),
    }

    cm = confusion_matrix(y_test, model.predict(X_test))

    report = classification_report(y_test, model.predict(X_test))
    
    return metrics, cm, report
