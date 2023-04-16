from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, Depends
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from woofmate.schemas.createSchema import ICreateUser, LoginUser, PasswordReset
from woofmate.models import User, DogProfile




class UserServices:
    async def createUser(db, user: ICreateUser):
        check_email = db.query(User).filter(User.email == user.email).first()
        if check_email is not None:
            raise HTTPException(status_code=400, detail="Email address already in use")
        password = generate_password_hash(user.password)
        new_user = User(email=user.email, hashed_password=password, firstName=user.firstName, lastName=user.lastName)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return jsonable_encoder({"message": "New account created successfully"})

    async def login(db, user: LoginUser):
        check_email = db.query(User).filter(User.email == user.email).first()
        if check_email is None:
            raise HTTPException(status_code=400, detail="Invalid email address")
        password = check_password_hash(check_email.hashed_password,user.password)
        if password is False:
            raise HTTPException(status_code=400, detail="Invalid password")
        return check_email

    # async def forgotPassword(db, user_email:PasswordReset):
    #     user = db.query(User).filter(User.email == user_email).first()
    #     if user is not None:
    #         token =

    def get_all_user(db):
        user = db.query(User).all()
        return user

    def get_one_user(db, **kwargs):
        user = db.query(User).filter_by(**kwargs).first()
        return user

