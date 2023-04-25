"""
Contains the routes for the dog profile
"""

from fastapi import Depends, APIRouter, File, Form, HTTPException, Path, status
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from typing import Annotated, List, Optional
from woofmate.functions.user_service import UserServices
from woofmate.functions.my_cloudinary import upload_image_to_cloudinary
from woofmate.functions.dog_profile_service import DogServices
from woofmate.database import get_db
from woofmate.schemas.createSchema import DogProfileResponse, Matches

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
    response_model=List[DogProfileResponse],
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


@dogProfile_router.put(
    '/update_dog_profile/{dog_id}',
    status_code=status.HTTP_200_OK
)
async def update_dog_profile(
    dog_image_1: Optional[bytes] = File(default=None),
    dog_image_2: Optional[bytes] = File(default=None),
    dog_image_3: Optional[bytes] = File(default=None),
    dog_id: int = Path(...), age: int = Form(default=None),
    description: str = Form(default=None), city: str = Form(default=None),
    state: str = Form(default=None), country: str = Form(default=None),
    relationship_preferences: str = Form(default=None),
    db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
):
    """
    Route to update a dog profile after validating that the user
    is logged in and the current user is the owner of the dog
    """
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid authorization"
        )
    current_user = Authorize.get_jwt_subject()

    if dog_image_1 and len(dog_image_1) > 1000000:
        raise HTTPException(
            status_code=400,
            detail="Dog Image shouldn't be greater than 1MB"
        )

    if dog_image_2 and len(dog_image_2) > 1000000:
        raise HTTPException(
            status_code=400,
            detail="Dog Image shouldn't be greater than 1MB"
        )

    if dog_image_2 and len(dog_image_3) > 1000000:
        raise HTTPException(
            status_code=400,
            detail="Dog Image shouldn't be greater than 1MB"
        )

    dog_image_1_url = await upload_image_to_cloudinary(
        'WOOF_MATES_DOGS', dog_image_1, current_user, 'dog_image_1'
    )

    dog_image_2_url = await upload_image_to_cloudinary(
        'WOOF_MATES_DOGS', dog_image_2, current_user, 'dog_image_2'
    )

    dog_image_3_url = await upload_image_to_cloudinary(
        'WOOF_MATES_DOGS', dog_image_3, current_user, 'dog_image_3'
    )

    update_dog_profile = await DogServices.update_dog_profile(
        db, current_user, dog_id, age, description, city, state,
        country, relationship_preferences, dog_image_1_url,
        dog_image_2_url, dog_image_3_url
    )

    return update_dog_profile


@dogProfile_router.delete(
    '/current_user/{dog_id}', status_code=status.HTTP_200_OK
)
async def delete_user_dog(
    dog_id: int, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
):
    """Route to delete a user's dog by it Id"""

    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid authorization"
        )
    current_user = Authorize.get_jwt_subject()

    return await DogServices.delete_dog_profile(
        db, current_user, dog_id
    )


@dogProfile_router.get(
    '/current_user/match_all_dogs/{dog_id}',
    status_code=status.HTTP_200_OK,
    response_model=Matches
)
async def match_all_dogs(
    dog_id: int, db: Session = Depends(get_db),
    Authorize: AuthJWT = Depends()
):
    """
    Route to get all matches for a dog profile
    """
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid authorization"
        )

    current_user = Authorize.get_jwt_subject()
    current_profile = DogServices.get_one_profile(db, id=dog_id)

    # Get all the profiles of dog matches for the current profile
    profiles = await DogServices.get_all_dog_profiles(
        db, exclude_id=dog_id
    )

    # Calculate the match score for each profile
    # and create a dictionary with the score and profile data
    each_matches = [
        {
            'score': await DogServices.match_dogs(
                db, current_profile, profile
            ), 'profile': profile
        } for profile in profiles
    ]
    # Sort the matches in descending order by score
    matches = sorted(each_matches, key=lambda m: m['score'], reverse=True)
    if len(matches) == 0:
        raise HTTPException(status_code=404, detail="No matches found")

    # Return the top 20 matches to the user
    return {'matches': matches[:20]}


@dogProfile_router.get(
    '/current_user/match_dog_by_breed/{dog_id}',
    status_code=status.HTTP_200_OK,
    response_model=Matches
)
async def match_same_breed(
    dog_id: int, db: Session = Depends(get_db),
    Authorize: AuthJWT = Depends()
):
    """
    Route to get all matches of dogs of the same breed as the dog
    """
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid authorization"
        )

    current_user = Authorize.get_jwt_subject()
    current_profile = DogServices.get_one_profile(db, id=dog_id)

    # Get all the profiles of the same breed as the current profile
    profiles = await DogServices.get_all_dog_profiles(
        db, exclude_id=dog_id, breed=current_profile.breed
    )

    # Calculate the match score for each profile
    # and create a dictionary with the score and profile data
    each_matches = [
        {
            'score': await DogServices.match_dogs(
                db, current_profile, profile
            ), 'profile': profile
        } for profile in profiles
    ]
    # Sort the matches in descending order by score
    matches = sorted(each_matches, key=lambda m: m['score'], reverse=True)
    if len(matches) == 0:
        raise HTTPException(status_code=404, detail="No matches found")

    # Return the top 20 matches to the user
    return {'matches': matches[:20]}


@dogProfile_router.get(
    '/current_user/match_dog_by_relationship/{dog_id}',
    status_code=status.HTTP_200_OK,
    response_model=Matches
)
async def match_dog_by_relationship(
    dog_id: int, db: Session = Depends(get_db),
    Authorize: AuthJWT = Depends()
):
    """
    Route to get all matches of dogs of the same relationship preference
    and if the relationship preference is breeding partner,
    the dog match should be opposite of the dog gender
    """
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid authorization"
        )

    current_user = Authorize.get_jwt_subject()
    current_profile = DogServices.get_one_profile(db, id=dog_id)

    # Get all the profiles of the relationship preference as the current dog
    profiles = await DogServices.get_all_dog_profiles(
        db, exclude_id=dog_id,
        relationship_preferences=current_profile.relationship_preferences
    )

    # Calculate the match score for each profile
    # and create a dictionary with the score and profile data
    each_matches = [
        {
            'score': await DogServices.match_dogs(
                db, current_profile, profile
            ), 'profile': profile
        } for profile in profiles
    ]
    # Sort the matches in descending order by score
    matches = sorted(each_matches, key=lambda m: m['score'], reverse=True)
    if len(matches) == 0:
        raise HTTPException(status_code=404, detail="No matches found")

    # Return the top 20 matches to the user
    return {'matches': matches[:20]}


@dogProfile_router.get(
    '/current_user/match_dogs_by_location/{dog_id}',
    status_code=status.HTTP_200_OK,
    response_model=Matches
)
async def match_dogs_by_location(
    dog_id: int, db: Session = Depends(get_db),
    Authorize: AuthJWT = Depends()
):
    """
    Route to get all matches for a dog based on location
    """
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid authorization"
        )

    current_user = Authorize.get_jwt_subject()
    current_profile = DogServices.get_one_profile(db, id=dog_id)

    # Get all the profiles of dog matches for the
    # current dog profile based on location
    profiles = await DogServices.get_all_dog_profiles(
        db, exclude_id=dog_id, city=current_profile.city,
        state=current_profile.state, country=current_profile.country
    )

    # Calculate the match score for each profile
    # and create a dictionary with the score and profile data
    each_matches = [
        {
            'score': await DogServices.match_dogs(
                db, current_profile, profile
            ), 'profile': profile
        } for profile in profiles
    ]
    # Sort the matches in descending order by score
    matches = sorted(each_matches, key=lambda m: m['score'], reverse=True)
    if len(matches) == 0:
        raise HTTPException(status_code=404, detail="No matches found")

    # Return the top 20 matches to the user
    return {'matches': matches[:20]}
