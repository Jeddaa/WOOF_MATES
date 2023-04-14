from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, Depends
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from woofmate.schemas.createSchema import ICreateUser, LoginUser, PasswordReset
from woofmate.models import User, Profile
from woofmate.database import get_db

# db:Session=Depends(get_db)



class Services:
    async def createUser(db, user: ICreateUser):
        check_email = await db.query(User).filter(User.email == user.email).first()
        if check_email is not None:
            raise HTTPException(status_code=400, detail="Email address already in use")
        password = await generate_password_hash(user.password)
        new_user = await User(email=user.email, hashed_password=password, firstName=user.firstName, lastName=user.lastName)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return jsonable_encoder({"message": "New account created successfully"})

    async def login(db, user: LoginUser):
        check_email = await db.query(User).filter(User.email == user.email).first()
        if check_email is None:
            raise HTTPException(status_code=400, detail="Invalid email address")
        password = await check_password_hash(check_email.hashed_password,user.password)
        if password is False:
            raise HTTPException(status_code=400, detail="Invalid password")
        return check_email

    # async def forgotPassword(db, user_email:PasswordReset):
    #     user = db.query(User).filter(User.email == user_email).first()
    #     if user is not None:
    #         token =
