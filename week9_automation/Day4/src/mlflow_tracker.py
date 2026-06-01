import tempfile

import mlflow
import mlflow.sklearn

def log_experiment(
    model,
    metrics,
    params,
    cm,
    report
):
    
    mlflow.set_experiment("Iris Random Forest Experiment")

    with mlflow.start_run():

        for key, value in params.items():
            mlflow.log_param(key, value)

        for key, value in metrics.items():
            mlflow.log_metric(key, value)

        mlflow.sklearn.log_model(model, "model")

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".txt",
            delete=False
        ) as f:
            f.write(str(cm))

            mlflow.log_artifact(f.name, artifact_path="confusion_matrix")
        
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".txt",
            delete=False
        ) as f:
            f.write(report)

            mlflow.log_artifact(f.name, artifact_path="classification_report")

    print("Experiment logged to MLflow")
    