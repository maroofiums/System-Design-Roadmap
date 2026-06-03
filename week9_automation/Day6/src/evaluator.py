from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report
)


def _compute_metrics(y_test, y_pred):
    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, average="weighted"),
        "recall": recall_score(y_test, y_pred, average="weighted"),
        "f1_score": f1_score(y_test, y_pred, average="weighted"),
    }


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return _compute_metrics(y_test, y_pred)


def evaluate_model_with_report(model, X_test, y_test):
    y_pred = model.predict(X_test)
    metrics = _compute_metrics(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return metrics, cm, report

    