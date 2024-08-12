from celery import Celery
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Set up the Celery app
celery_app = Celery(
    "tasks",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND"),
)

@celery_app.task
def process_message(index):
    print(f"Processing message {index}")
    return index
