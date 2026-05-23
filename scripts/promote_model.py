# promote model

from http import client
import os
from dvc import log
import mlflow
from src.logger import logging
from src.utils.mlflow import setup_mlflow_tracking

def promote_model():
    setup_mlflow_tracking()
 
    model_name = "my_model"
    client = mlflow.MlflowClient()

    # ✅ Get latest version with "staging" alias instead of stage
    staging_version = client.get_model_version_by_alias(model_name, "staging").version

    # ✅ Promote to production by setting alias
    client.set_registered_model_alias(
        name=model_name,
        alias="production",
        version=staging_version
    )

    # ✅ Remove staging alias after promotion
    client.delete_registered_model_alias(
        name=model_name,
        alias="staging"
    )

    logging.info("Model version %s promoted to production.", staging_version)
    print(f"Model version {staging_version} promoted to production")

if __name__ == "__main__":
    promote_model()
