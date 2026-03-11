from pydantic_settings import BaseSettings
import dotenv
import os

dotenv.load_dotenv()


class Settings(BaseSettings):
    EMAIL: str = os.getenv("EMAIL")
    APP_PASSWORD: str = os.getenv("APP_PASSWORD")
    SMTP_SERVER: str = os.getenv("SMTP_SERVER")
    SMTP_PORT: int = os.getenv("SMTP_PORT")
    MAIL_STARTTLS: bool = os.getenv("MAIL_STARTTLS")

    class Config:
        env_file = ".env"


settings = Settings()
