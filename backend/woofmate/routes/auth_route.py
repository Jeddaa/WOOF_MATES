from fastapi import Depends, APIRouter, status
from fastapi_jwt_auth import AuthJWT
from woofmate.functions.service import Services
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from woofmate.database import get_db
from ..schemas.createSchema import ICreateUser, IUser, LoginUser
from woofmate.config import settings

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
    return await Services.createUser(db, newUser)

@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(user:LoginUser, db:Session=Depends(get_db), Authorize:AuthJWT=Depends()):
    user_to_login = await Services.login(db, user)
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
