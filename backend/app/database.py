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


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# class DB:
#     """
#     DB class which contains the necessary methods
#     and connections.
#     """

    # def __init__(self):
    #     self.__session = None

    # @property
    # def _db(self):
    #     """Memoized session object"""
    #     if self.__session is None:
    #         SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    #         self.__session = SessionLocal()
    #     return self.__session

    # def get_db(self):
    #     """
    #     Creates a new database session for each incoming request
    #     to the application using FastAPI dependency.
    #     """
    #     try:
    #         db = self._db
    #         yield db

    #     finally:
    #         db.close()
        
    # def create_user(self, user: schemas.UserCreate):
    #     new_user = User(
    #         username=user.username,
    #         email=user.email,
    #         password=user.password
    #     )
    #     self._db.add(new_user)
    #     self._db.commit()
    #     self._db.refresh(new_user)
    #     return new_user

    # def create_dog(self, dog: schemas.DogCreate, owner_id: int):
    #     """
    #     Creates a new dog and assigns it to the owner with
    #     the given owner_id
    #     """
    #     new_dog = Dog(
    #         name=dog.name,
    #         age=dog.age,
    #         gender=dog.gender,
    #         breed=dog.breed,
    #         city=dog.city,
    #         state=dog.state,
    #         country=dog.country,
    #         description=dog.description,
    #         relationshipPreferences=dog.relationshipPreferences,
    #         pictureFilename=dog.pictureFilename,
    #         picture=dog.picture,
    #         owner_id=owner_id
    #     )
    #     self._db.add(new_dog)
    #     self._db.commit()
    #     self._db.refresh(new_dog)
    #     return new_dog

    # def find_user_by(self, **kwargs):
    #     """
    #     Returns the first row found in the users table
    #     as filtered by the input arguments
    #     """
    #     try:
    #         user = self._db.query(User).filter_by(**kwargs).one()
    #         return user
    #     except NoResultFound:
    #         raise
    #     except InvalidRequestError:
    #         raise


    # def update_user(self, user_id: int, **kwargs):
    #     """
    #      Updates the user's attribute from the find_user_by method
    #     """
    #     user = self.find_user_by(id=user_id)
    #     for key, value in kwargs.items():
    #         if hasattr(user, key):
    #             setattr(user, key, value)
    #         else:
    #             raise ValueError

    #     self._db.commit()

    # def profile(self, username: str) -> dict:
    #     """
    #     Return the profile of the user along with the
    #     dog joined together.
    #     """
    #     user = self.find_user_by(username=username)
    #     dogs = self._db.query(Dog).filter_by(owner_id=user.id).all()
    #     dog_data = [schemas.Dog.from_orm(dog) for dog in dogs]
    #     profile = {
    #         "username": user.username,
    #         "email": user.email,
    #         "dogs": dog_data
    #     }
    #     return profile
