"""
Contains the routes for the dog profile
"""

from fastapi import Depends, APIRouter, File, Form, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from typing import Annotated, List
from woofmate.functions.my_cloudinary import upload_image_to_cloudinary
from woofmate.functions.dog_profile_service import DogServices
from woofmate.database import get_db
from woofmate.schemas.createSchema import ICreateProfile

dogProfile_router = APIRouter(
    prefix='/profile',
    tags=["Dogs"]
)

DogServices = DogServices()


@dogProfile_router.post(
    "/create_dog_profile", status_code=status.HTTP_201_CREATED
)
async def create_profile(
    dog_image_1: Annotated[bytes, File()],
    dog_image_2: Annotated[bytes, File()],
    dog_image_3: Annotated[bytes, File()],
    name: str = Form(...), age: str = Form(...), gender: str = Form(...),
    breed: str = Form(...), description: str = Form(...),
    city: str = Form(...), state: str = Form(...), country: str = Form(...),
    relationship_preferences: str = Form(...),
    db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
):
    """
    A method to create a dog profile after validating the data passed
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid authorization"
        )

    current_user = Authorize.get_jwt_subject()

    # Checks if the dogs images are uploaded succesfully and are
    # not larger than 1MB
    if not dog_image_1:
        raise HTTPException(
            status_code=400, detail="Profile picture is required"
        )

    if len(dog_image_1) > 1000000:
        raise HTTPException(
            status_code=400,
            detail="Dog Image shouldn't be greater than 1MB"
        )

    if not dog_image_2:
        raise HTTPException(
            status_code=400, detail="Profile picture is required"
        )

    if len(dog_image_2) > 1000000:
        raise HTTPException(
            status_code=400,
            detail="Dog Image shouldn't be greater than 1MB"
        )

    if not dog_image_3:
        raise HTTPException(
            status_code=400, detail="Profile picture is required"
        )

    if len(dog_image_3) > 1000000:
        raise HTTPException(
            status_code=400,
            detail="Dog Image shouldn't be greater than 1MB"
        )

    dog_image_1_url = await upload_image_to_cloudinary(
        'WOOF_MATES_DOGS', dog_image_1, current_user, 'dog_image'
    )

    if not dog_image_1_url:
        raise HTTPException(status_code=500, detail="Failed to upload Image 1")

    dog_image_2_url = await upload_image_to_cloudinary(
        'WOOF_MATES_DOGS', dog_image_2, current_user, 'dog_image'
    )

    if not dog_image_2_url:
        raise HTTPException(status_code=500, detail="Failed to upload Image 2")

    dog_image_3_url = await upload_image_to_cloudinary(
        'WOOF_MATES_DOGS', dog_image_3, current_user, 'dog_image'
    )

    if not dog_image_3_url:
        raise HTTPException(status_code=500, detail="Failed to upload Image 3")

    new_dog = await DogServices.create_dog(
        db, name, age, gender, breed, description, city, state, country,
        relationship_preferences, dog_image_1_url, dog_image_2_url,
        dog_image_3_url, current_user
    )
    return new_dog


@dogProfile_router.get(
    "/get_all_profile_by_user",
    response_model=List[ICreateProfile],
    status_code=status.HTTP_201_CREATED
)
async def get_all_dog_profile(
    db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
):
    """Gets all the dog profiles of the user"""
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid authorization"
        )

    current_user = Authorize.get_jwt_subject()
    return await DogServices.get_allProfiles_of_user(db, current_user)
