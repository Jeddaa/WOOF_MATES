from fastapi import Depends, APIRouter, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from woofmate.functions.user_service import UserServices
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from woofmate.database import get_db
from ..schemas.createSchema import ICreateUser, IUser, LoginUser
from woofmate.config import settings
from typing import List
from woofmate.models import User

auth_router = APIRouter(prefix='/auth',
                        tags=["User Routes"])

# authjwt_secret_key = settings.AUTHJWT_SECRET_KEY

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@auth_router.post("/signup/", status_code=status.HTTP_201_CREATED)
async def create_user(newUser: ICreateUser, db: Session = Depends(get_db)):
    return await UserServices.createUser(db, newUser)

@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(user:LoginUser, db:Session=Depends(get_db), Authorize:AuthJWT=Depends()):
    user_to_login = await UserServices.login(db, user)
    if user_to_login.email == user.email:
        access_token = Authorize.create_access_token(subject=user_to_login.email)
        refresh_token = Authorize.create_refresh_token(subject=user_to_login.email)
        response = {
            "access_token":f"Bearer {access_token}",
            "refresh_token":f"Bearer {refresh_token}"
        }

        return jsonable_encoder(response)
        # return response

@auth_router.post('/forgotpassword', status_code=status.HTTP_200_OK)
async def forgotpassword(email:str,  db:Session=Depends(get_db)):
    pass

@auth_router.get('/get_users',  response_model=List[IUser], status_code=status.HTTP_200_OK)
async def get_users(db:Session=Depends(get_db)):
    users= UserServices.get_all_user(db)
    return users
    # return db.query(User).all()

@auth_router.get('/get_one_user/{user_id}',  response_model=IUser, status_code=status.HTTP_200_OK)
async def get_one_user(user_id:int, db:Session=Depends(get_db)):
    user= UserServices.get_one_user(db, id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
