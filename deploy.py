import mlflow.sagemaker
from mlflow.deployments import get_deploy_client

endpoint_name="prod-endpoint"
model_uri="s3://rc-mlflow-artifacts/1/e9504ad2afa44c7ca86a6b821758b58e/artifacts/ElasticNet"

# Define your configuration parameters as a dictionary
config = {
    "execution_role_arn": "arn:aws:iam::211966428728:role/service-role/AmazonSageMaker-ExecutionRole-20240223T190075",
    "bucket_name": "rc-mlflow-artifacts",
    "image_url": "211966428728.dkr.ecr.us-east-1.amazonaws.com/housing-price:2.10.2",
    "region_name": "us-east-1",
    "archive": False,
    "instance_type": "ml.m5.xlarge",
    "instance_count": 1,
    "synchronous": True
}

# Initialize a deployment client for SageMaker
client = get_deploy_client("sagemaker")

# Create the deployment
client.create_deployment(
    name=endpoint_name,
    model_uri=model_uri,
    flavor="python_function",
    config=config,
)
