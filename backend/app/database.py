import logging
from app.config import settings
from app.models import User, Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError, InvalidRequestError

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class DB:
    """
    DB class which contains the necessary methods
    and connections.
    """

    def get_db(self):
        """
        Creates a new database session for each incoming request
        to the application using FastAPI dependency.
        """
        try:
            db = self.SessionLocal()
            yield db

        except SQLAlchemyError as e:
            logging.exception("Database error: %s", str(e))
            db.rollback()
            raise

        finally:
            db.close()

