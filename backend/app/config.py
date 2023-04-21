from pydantic import BaseSettings, PostgresDsn
from dotenv import load_dotenv
from functools import lru_cache
load_dotenv()


class Settings(BaseSettings):
    """Configuration for the application"""
    DATABASE_URL: PostgresDsn
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET_KEY: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
