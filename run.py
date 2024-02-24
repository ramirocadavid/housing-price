import mlflow

experiment_name = "ElasticNet"
entry_point = "Training"

mlflow.set_tracking_uri("http://ec2-184-73-53-253.compute-1.amazonaws.com:5000")

mlflow.projects.run(
    uri=".",
    entry_point=entry_point,
    experiment_name=experiment_name,
    env_manager="conda"
)