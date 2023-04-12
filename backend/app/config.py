from pydantic import BaseSettings, PostgresDsn
from dotenv import load_dotenv
load_dotenv()
from functools import lru_cache


class Settings(BaseSettings):
    """Configuration for the application"""
    DATABASE_URL: PostgresDsn

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
