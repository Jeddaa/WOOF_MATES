from app import schemas
from app.models import User, Dog
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import List

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    """Hashes the password so as not to store
    the user password plain"""
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str):
    """
    Verifies the user actual password against the entered password
    """
    return pwd_context.verify(password, hashed_password)


class Crud:
    """
    Class to manage the create, read, update and
    delete methods
    """

    def get_user_by(self, db: Session, **kwargs):
        """
         Returns the first row found in the users table
         as filtered by the input arguments
        """
        user = db.query(User).filter_by(**kwargs).first()
        return user

    def get_users(self, db: Session, skip: int, limit: int = 20):
        """
        Return the users present in the database and pagination
        implemented
        """
        users = db.query(User).offset(skip).limit(limit).all()
        return users

    def create_user(
        self, db: Session, username: str,
        email: str, password: str, profile_picture_url: str
    ):
        """
        A method to create and store a new user to database
        with the required fields
        """
        if not profile_picture_url:
            raise ValueError("Profile picture URL is required")

        hashed_password = hash_password(password)
        new_user = User(
            username=username,
            email=email,
            password=hashed_password,
            profile_picture_url=profile_picture_url
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_dogs(self, db: Session, skip: int = 0, limit: int = 20):
        """gets the dog related to a user, it's owner"""
        return db.query(Dog).offset(skip).limit(limit).all()

    def create_user_dogs(
        self, db: Session, name: str, age: int, gender: str, breed: str,
        city: str, state: str, country: str, description: str,
        relationship_preferences: str, pictures_url: List[str], user_id: int
    ):
        """
        Create the dog and assign it to the user since it's a
        one to many relationship(One User -> Many dogs)
        """
        if not pictures_url:
            raise ValueError("Profile picture URL is required")
        new_dog = Dog(
            name, age, gender, breed, city, state, country, description,
            relationship_preferences, pictures_url, user_id
        )
        db.add(new_dog)
        db.commit()
        db.refresh(new_dog)
        return new_dog
