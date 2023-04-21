from pydantic import BaseSettings
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()


class Settings(BaseSettings):
    SECRET_KEY: str
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET_KEY: str
    SQLALCHEMY_DATABASE_URL: str
    AUTHJWT_SECRET_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
