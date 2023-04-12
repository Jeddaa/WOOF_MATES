"""
Database module
contains the database methods and necessary setups
"""

import logging
from app.config import settings
from app.models import User, Dog
from app import schemas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
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

    def create_user(self, db: Session, user: schemas.UserCreate):
        """A method to save the new user to the database"""
        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=user.hashed_password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def create_dog(self, db: Session, dog: schemas.DogCreate, owner_id: int):
        """
        Creates a new dog and assigns it to the owner with
        the given owner_id
        """
        new_dog = Dog(
            name=dog.name,
            age=dog.age,
            gender=dog.gender,
            breed=dog.breed,
            city=dog.city,
            state=dog.state,
            country=dog.country,
            description=dog.description,
            relationshipPreferences=dog.relationshipPreferences,
            pictureFilename=dog.pictureFilename,
            picture=dog.picture,
            owner_id=owner_id
        )
        db.add(new_dog)
        db.commit()
        db.refresh(new_dog)
        return new_dog

    def find_user_by(self, db: Session, **kwargs):
        """
         Returns the first row found in the users table
         as filtered by the input arguments
        """
        try:
            users = db.query(User).filter_by(**kwargs).one()
            return users
        except NoResultFound:
            raise
        except InvalidRequestError:
            raise

    def update_user(self, db: Session, user_id: int, **kwargs):
        """
         Updates the user's attribute from the find_user_by method
        """
        user = self.find_user_by(db, id=user_id)
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError

        db.commit()

    def profile(self, db: Session, username: str) -> dict:
        """
        Return the profile of the user along with the
        dog joined together.
        """
        user = self.find_user_by(db, username=username)
        dogs = db.query(Dog).filter_by(owner_id=user.id).all()
        dog_data = [schemas.Dog.from_orm(dog) for dog in dogs]
        profile = {
            "username": user.username,
            "email": user.email,
            "dogs": dog_data
        }
        return profile
