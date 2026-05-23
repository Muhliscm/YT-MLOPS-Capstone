# register model

import json
import mlflow
import logging
from src.logger import logging
import os
import dagshub

import warnings
warnings.simplefilter("ignore", UserWarning)
warnings.filterwarnings("ignore")
from src.constants import DAGS_HUB_TRACKING_URI, DAGS_HUB_REPO_NAME, DAGS_HUB_REPO_OWNER_NAME,DAGS_HUB_TOKEN


# Below code block is for production use
# -------------------------------------------------------------------------------------
# Set up DagsHub credentials for MLflow tracking
if not DAGS_HUB_TOKEN:
    raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

os.environ["MLFLOW_TRACKING_USERNAME"] = DAGS_HUB_TOKEN
os.environ["MLFLOW_TRACKING_PASSWORD"] = DAGS_HUB_TOKEN

logging.info("DagsHub credentials set for MLflow tracking.")
logging.info("MLflow tracking URI set to: %s", f'https://dagshub.com/{DAGS_HUB_REPO_OWNER_NAME}/{DAGS_HUB_REPO_NAME}.mlflow')

# Set up MLflow tracking URI
mlflow.set_tracking_uri(f'https://dagshub.com/{DAGS_HUB_REPO_OWNER_NAME}/{DAGS_HUB_REPO_NAME}.mlflow')
# -------------------------------------------------------------------------------------


# Below code block is for local use
# -------------------------------------------------------------------------------------
# mlflow.set_tracking_uri(DAGS_HUB_TRACKING_URI)
# dagshub.init(repo_owner=DAGS_HUB_REPO_OWNER_NAME, repo_name=DAGS_HUB_REPO_NAME, mlflow=True)
# --------------------------------------------------------------------------------


def load_model_info(file_path: str) -> dict:
    """Load the model info from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            model_info = json.load(file)
        logging.debug('Model info loaded from %s', file_path)
        return model_info
    except FileNotFoundError:
        logging.error('File not found: %s', file_path)
        raise
    except Exception as e:
        logging.error('Unexpected error occurred while loading the model info: %s', e)
        raise

def register_model(model_name: str, model_info: dict):
    """Register the model to the MLflow Model Registry."""
    try:
        client = mlflow.tracking.MlflowClient()

        # Get latest version
        latest_versions = client.get_registered_model(model_name).latest_versions
        if not latest_versions:
            raise RuntimeError(f"No versions found for registered model '{model_name}'")
        
        latest_version = latest_versions[-1].version

        # ✅ Set alias instead of stage transition
        client.set_registered_model_alias(
            name=model_name,
            alias="staging",
            version=latest_version
        )

        logging.info(
            'Model %s version %s aliased to staging.',
            model_name, latest_version
        )
        
    
    except Exception as e:
        logging.error('Error during model registration: %s', e)
        raise

def main():
    try:
        model_info_path = 'reports/experiment_info.json'
        model_info = load_model_info(model_info_path)
        
        model_name = "my_model"
        register_model(model_name, model_info)
    except Exception as e:
        logging.error('Failed to complete the model registration process: %s', e)
        raise

if __name__ == '__main__':
    main()

