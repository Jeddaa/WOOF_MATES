"""
Contains the routes for the dog profile
"""

from fastapi import Depends, APIRouter, File, Form, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from typing import Annotated, List
from woofmate.functions.user_service import UserServices
from woofmate.functions.my_cloudinary import upload_image_to_cloudinary
from woofmate.functions.dog_profile_service import DogServices
from woofmate.database import get_db
from woofmate.schemas.createSchema import ICreateProfile

dogProfile_router = APIRouter(
    prefix='/profile',
    tags=["Dogs"]
)

UserServices = UserServices()
DogServices = DogServices()


@dogProfile_router.post(
    "/create_dog_profile", status_code=status.HTTP_201_CREATED
)
async def create_profile(
    dog_image_1: Annotated[bytes, File()],
    dog_image_2: Annotated[bytes, File()],
    dog_image_3: Annotated[bytes, File()],
    name: str = Form(...), age: str = Form(...), gender: str = Form(...),
    breed: str = Form(...), description: str = Form(default=None),
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
            status_code=400, detail="Dog image 1 is required"
        )

    if len(dog_image_1) > 1000000:
        raise HTTPException(
            status_code=400,
            detail="Dog Image shouldn't be greater than 1MB"
        )

    if not dog_image_2:
        raise HTTPException(
            status_code=400, detail="Dog image 2 is required"
        )

    if len(dog_image_2) > 1000000:
        raise HTTPException(
            status_code=400,
            detail="Dog Image shouldn't be greater than 1MB"
        )

    if not dog_image_3:
        raise HTTPException(
            status_code=400, detail="Dog image 3 is required"
        )

    if len(dog_image_3) > 1000000:
        raise HTTPException(
            status_code=400,
            detail="Dog Image shouldn't be greater than 1MB"
        )

    dog_image_1_url = await upload_image_to_cloudinary(
        'WOOF_MATES_DOGS', dog_image_1, current_user, 'dog_image_1'
    )

    if not dog_image_1_url:
        raise HTTPException(status_code=500, detail="Failed to upload Image 1")

    dog_image_2_url = await upload_image_to_cloudinary(
        'WOOF_MATES_DOGS', dog_image_2, current_user, 'dog_image_2'
    )

    if not dog_image_2_url:
        raise HTTPException(status_code=500, detail="Failed to upload Image 2")

    dog_image_3_url = await upload_image_to_cloudinary(
        'WOOF_MATES_DOGS', dog_image_3, current_user, 'dog_image_3'
    )

    if not dog_image_3_url:
        raise HTTPException(status_code=500, detail="Failed to upload Image 3")

    currentUser = UserServices.get_one_user(db, email=current_user)
    dog = DogServices.get_one_profile(
        db, name=name, owner_id=currentUser.id,
        description=description, city=city, state=state
        )
    if dog:
        raise HTTPException(
            status_code=400,
            detail="Dog profile already exists"
        )

    new_dog = await DogServices.create_dog(
        db, name, age, gender, breed, description, city, state, country,
        relationship_preferences, dog_image_1_url, dog_image_2_url,
        dog_image_3_url, current_user
    )
    return new_dog


@dogProfile_router.get(
    "/current_user_dogs",
    response_model=List[ICreateProfile],
    status_code=status.HTTP_200_OK
)
async def current_user_dogs(
    skip: int = 0, limit: int = 20,
    db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
):
    """
    Gets all the dog profiles of the user characterised by the
    skip and limit parameters to paginate the data
    """
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid authorization"
        )

    current_user = Authorize.get_jwt_subject()
    dog_profiles = await DogServices.get_dog_profiles_of_user(
        db, current_user, skip=skip, limit=limit
    )
    return dog_profiles