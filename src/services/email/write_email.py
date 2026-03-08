from fastapi import BackgroundTasks
from src.core.config import settings 
from src.core.logging import logger

async def write_email(subject: str, message: str,
background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, subject, message)

def send_email(subject: str, message: str):
    logger.info(f"Sending email to {settings.EMAIL_TO} with subject {subject} and message {message}")