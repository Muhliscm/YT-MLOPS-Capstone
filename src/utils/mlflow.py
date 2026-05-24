from src.constants import DAGS_HUB_REPO_NAME, DAGS_HUB_REPO_OWNER_NAME,DAGS_HUB_TOKEN,DAGS_HUB_TRACKING_URI
import os
import mlflow
import dagshub
from src.logger import logging


def setup_mlflow_tracking():
    """ Below code block is for production use """ 
    if not DAGS_HUB_TOKEN:
        raise EnvironmentError("CAPSTONE_TEST environment variable is not set")
    
    if not DAGS_HUB_REPO_OWNER_NAME:
        raise EnvironmentError("DAGS_HUB_REPO_OWNER_NAME environment variable is not set") 
     
    if not DAGS_HUB_REPO_NAME:
        raise EnvironmentError("DAGS_HUB_REPO_NAME environment variable is not set")

    os.environ["MLFLOW_TRACKING_USERNAME"] = DAGS_HUB_TOKEN
    os.environ["MLFLOW_TRACKING_PASSWORD"] = DAGS_HUB_TOKEN

    logging.info("MLflow tracking environment variables set for DagsHub")

    logging.info("MLflow tracking URI:%s", f'https://dagshub.com/{DAGS_HUB_REPO_OWNER_NAME}/{DAGS_HUB_REPO_NAME}.mlflow')

    # Set up MLflow tracking URI
    mlflow.set_tracking_uri(f'https://dagshub.com/{DAGS_HUB_REPO_OWNER_NAME}/{DAGS_HUB_REPO_NAME}.mlflow')


    """ Below code block is for local use """
    # logging.info("MLflow tracking URI:%s", DAGS_HUB_TRACKING_URI)
    # mlflow.set_tracking_uri(DAGS_HUB_TRACKING_URI)
    # dagshub.init(repo_owner=DAGS_HUB_REPO_OWNER_NAME, repo_name=DAGS_HUB_REPO_NAME, mlflow=True)
   





