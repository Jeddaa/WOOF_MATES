"""
User services models:
contains all the methods related to the users
"""

from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
from woofmate.models import User


class UserServices:
    """
    Contains the methods to handle any services related to the users
    and the database
    """

    def get_all_user(self, db: Session, skip: int, limit: int = 20):
        """
        Return the users present in the database and pagination
        implemented
        """
        users = db.query(User).offset(skip).limit(limit).all()
        return users

    def get_one_user(self, db, **kwargs):
        """
        Get a single user from the database
        """
        user = db.query(User).filter_by(**kwargs).first()
        return user

    async def createUser(
        self, db: Session, firstName: str, lastName: str,
        email: EmailStr, password: str, profile_picture_url: str
    ):
        """
        A method to create and store a new user to database
        with the required fields
        """
        check_email = self.get_one_user(db, email=email)
        if check_email:
            raise HTTPException(
                status_code=400, detail="Email address already in use"
            )

        password = generate_password_hash(password)
        new_user = User(
            firstName=firstName,
            lastName=lastName,
            email=email,
            hashed_password=password,
            profile_picture=profile_picture_url
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {'message': 'User created successfully'}

    async def login(self, db: Session, email: EmailStr, password: str):
        """
        Method to login a user and check if the email and password
        are valid
        """
        check_email = self.get_one_user(db, email=email)

        if check_email is None:
            raise HTTPException(
                status_code=400, detail="Invalid email address"
                )

        password = check_password_hash(
            check_email.hashed_password, password
        )

        if password is False:
            raise HTTPException(status_code=400, detail="Invalid password")
        return check_email

    async def get_full_profiles(self, db: Session, current_user: str):
        """
        Method to get all the profiles of a user
        """
        user = self.get_one_user(db, email=current_user)
        if user is not None:
            return {"user": user, "dogProfiles": user.dogProfiles}
        else:
            return {'message': 'No profiles found'}

    async def update_user(
        self, db: Session, current_user: str, image_url: str
    ):
        """Method to the update the current user profile"""

        try:
            user = self.get_one_user(db, email=current_user)
            if image_url:
                user.profile_picture = image_url
            db.commit()
            db.refresh(user)
            return {'detail': 'Successsfully updated'}

        except Exception as e:
            raise HTTPException(
                status_code=400, detail=str(e)
            )

    async def get_other_user_profile(self, db: Session, user_id: int):
        """Method to get the other user profile"""
        user = self.get_one_user(db, id=user_id)
        if user is not None:
            return user
        else:
            return {'message': 'No profiles found'}

    # async def forgotPassword(self, db: Session, user_email:PasswordReset):
    #     user = db.query(User).filter(User.email == user_email).first()
    #     if user is not None:
    #         token =
