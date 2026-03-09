from fastapi import BackgroundTasks
from src.core.config import settings
from src.core.logging import logger
import aiosmtplib
from email.mime.text import MIMEText


async def write_email(
    subject: str, body: str, email_to: str, background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email, subject, body, email_to)


async def send_email(subject: str, body: str, email_to: str):
    try:
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = settings.EMAIL
        message["To"] = email_to

        await aiosmtplib.send(
            message,
            hostname=settings.SMTP_SERVER,
            port=settings.SMTP_PORT,
            username=settings.EMAIL,
            password=settings.APP_PASSWORD,
            start_tls=True,
        )
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        raise e
