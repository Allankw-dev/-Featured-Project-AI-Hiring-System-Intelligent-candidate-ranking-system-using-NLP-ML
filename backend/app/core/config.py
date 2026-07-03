from functools import lru_cache
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "fallback-local-key-only")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DATABASE_URL: str = os.environ.get("DATABASE_URL", "")

    ADMIN_EMAIL: str = os.environ.get("ADMIN_EMAIL", "")
    ADMIN_EMAIL_PASSWORD: str = os.environ.get("ADMIN_EMAIL_PASSWORD", "")
    ADMIN_EMAILS: str = os.environ.get("ADMIN_EMAILS", "")

    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587

    RESEND_API_KEY: str = os.environ.get("RESEND_API_KEY", "")

    UPLOAD_DIR: str = "uploads"

    FRONTEND_URL: str = os.environ.get("FRONTEND_URL", "https://ai-powered-hiring-system.streamlit.app")

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()