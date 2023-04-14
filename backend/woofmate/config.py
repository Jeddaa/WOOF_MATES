from pydantic import BaseSettings
# from pydantic.utils import env_file
from functools import lru_cache

class Settings(BaseSettings):
    SECRET_KEY: str
    # authjwt_secret_key: str
    SQLALCHEMY_DATABASE_URL:str
    AUTHJWT_SECRET_KEY:str

    class Config:
        env_file = ".env"


@lru_cache
def get_setings():
    return Settings()

settings = get_setings()
