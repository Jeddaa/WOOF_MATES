from fastapi import Depends, APIRouter, File, HTTPException, UploadFile, status
from fastapi_jwt_auth import AuthJWT
from woofmate.functions.dog_profile_service import DogServices
from woofmate.functions.user_service import UserServices
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from woofmate.database import get_db
from ..schemas.createSchema import ICreateProfile
from woofmate.config import settings
from typing import Annotated, List
from woofmate.models import User

dogProfile_router = APIRouter(
    prefix='/profile',
    tags=["Dog Profile Routes"]
)


@dogProfile_router.post("/create_dog_profile/", status_code=status.HTTP_201_CREATED)
async def create_profile(dogProfile: ICreateProfile, db: Session = Depends(get_db), Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid authorization")
    current_user = Authorize.get_jwt_subject()
    print("trial")
    return await DogServices.createDog(db, dogProfile, current_user)

@dogProfile_router.post("/update_dog_images/{profile_id}", status_code=status.HTTP_201_CREATED)
async def create_profile(profile_id: int, dog_images: Annotated[list[bytes], File()], db: Session = Depends(get_db), Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid authorization")
    current_user = Authorize.get_jwt_subject()
    return await DogServices.upload_dog_images(db, profile_id, dog_images, current_user)

@dogProfile_router.get("/get_all_profile_by_user/", response_model= List[ICreateProfile], status_code=status.HTTP_201_CREATED)
async def get_all_dog_profile(db: Session = Depends(get_db), Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid authorization")
    current_user = Authorize.get_jwt_subject()
    print("trial")
    return await DogServices.get_allProfiles_of_user(db, current_user)
