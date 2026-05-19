from dotenv import load_dotenv
import os

load_dotenv()

# dags hub repo details
DAGS_HUB_TRACKING_URI = os.getenv("DAGS_HUB_TRACKING_URI")
DAGS_HUB_REPO_NAME = os.getenv("DAGS_HUB_REPO_NAME")
DAGS_HUB_REPO_OWNER_NAME = os.getenv("DAGS_HUB_REPO_OWNER_NAME")