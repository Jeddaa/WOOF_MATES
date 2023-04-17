from pydantic import BaseSettings
# from pydantic.utils import env_file
from functools import lru_cache

class Settings(BaseSettings):
    SECRET_KEY: str
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET_KEY: str
    SQLALCHEMY_DATABASE_URL:str
    AUTHJWT_SECRET_KEY:str

    class Config:
        env_file = ".env"


@lru_cache
def get_setings():
    return Settings()

settings = get_setings()
