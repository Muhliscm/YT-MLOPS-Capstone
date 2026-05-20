# promote model

from http import client
import os
from dvc import log
import mlflow
from src.constants import DAGS_HUB_TRACKING_URI, DAGS_HUB_REPO_NAME, DAGS_HUB_REPO_OWNER_NAME,DAGS_HUB_TOKEN
import dagshub
from src.logger import logging

def promote_model():
    logging.info("Starting model promotion process...")
    # Set up DagsHub credentials for MLflow tracking

        # Below code block is for local use
    # -------------------------------------------------------------------------------------
    # mlflow.set_tracking_uri(DAGS_HUB_TRACKING_URI)
    # dagshub.init(repo_owner=DAGS_HUB_REPO_OWNER_NAME, repo_name=DAGS_HUB_REPO_NAME, mlflow=True)
    # -------------------------------------------------------------------------------------

    # Below code block is for production use    
    if not DAGS_HUB_TOKEN:
        raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

    os.environ["MLFLOW_TRACKING_USERNAME"] = DAGS_HUB_TOKEN
    os.environ["MLFLOW_TRACKING_PASSWORD"] = DAGS_HUB_TOKEN

    # Set up MLflow tracking URI

    mlflow.set_tracking_uri(f'{DAGS_HUB_TRACKING_URI}/{DAGS_HUB_REPO_OWNER_NAME}/{DAGS_HUB_REPO_NAME}.mlflow')
# -------------------------------------------------------------------------------------
 
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
