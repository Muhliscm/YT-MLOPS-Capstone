from dotenv import load_dotenv
import os

load_dotenv(override=False)

# dags hub repo details
DAGS_HUB_TRACKING_URI = os.getenv("DAGS_HUB_TRACKING_URI")
DAGS_HUB_REPO_NAME = os.getenv("DAGS_HUB_REPO_NAME")
DAGS_HUB_REPO_OWNER_NAME = os.getenv("DAGS_HUB_REPO_OWNER_NAME")
DAGS_HUB_TOKEN = os.getenv("CAPSTONE_TEST")

# AWS S3 credentials
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION_NAME = os.getenv("AWS_REGION_NAME")