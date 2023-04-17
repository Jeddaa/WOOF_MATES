from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, Depends
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from woofmate.schemas.createSchema import ICreateUser, LoginUser, PasswordReset
from woofmate.models import User, DogProfile


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
        user = db.query(User).filter_by(**kwargs).first()
        return user

    async def createUser(self, db: Session, user: ICreateUser):
        check_email = self.get_one_user(db, email=user.email)
        if check_email is not None:
            raise HTTPException(status_code=400, detail="Email address already in use")
        password = generate_password_hash(user.password)
        new_user = User(
            email=user.email,
            hashed_password=password,
            firstName=user.firstName,
            lastName=user.lastName
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return jsonable_encoder({"message": "New account created successfully"})

    async def login(self, db: Session, user: LoginUser):
        check_email = db.query(User).filter(User.email == user.email).first()
        if check_email is None:
            raise HTTPException(status_code=400, detail="Invalid email address")
        password = check_password_hash(check_email.hashed_password, user.password)
        if password is False:
            raise HTTPException(status_code=400, detail="Invalid password")
        return check_email

    # async def forgotPassword(self, db: Session, user_email:PasswordReset):
    #     user = db.query(User).filter(User.email == user_email).first()
    #     if user is not None:
    #         token =
