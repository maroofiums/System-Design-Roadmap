from sklearn.metrics import accuracy_score,f1_score,recall_score,precision_score
from src.trainer import train_model

def evaluate_model(model,X_test,y_test):
    y_pred = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test,y_pred),
        "f1": f1_score(y_test,y_pred,average="weighted"),
        "recall": recall_score(y_test,y_pred,average="weighted"),
        "precision": precision_score(y_test,y_pred,average="weighted"),
    }

    return metrics