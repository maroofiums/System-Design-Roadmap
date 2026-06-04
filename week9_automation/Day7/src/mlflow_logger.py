import mlflow
import mlflow.sklearn


def log_experiment(model, params, metrics):

    with mlflow.start_run():

        for key, value in params.items():
            mlflow.log_param(key, value)

        for key, value in metrics.items():
            mlflow.log_metric(key, value)

        mlflow.sklearn.log_model(
            model,
            artifact_path="model"
        )