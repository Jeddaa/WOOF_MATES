from fastapi import HTTPException
from sqlalchemy.orm import Session
from woofmate.schemas.createSchema import (
    ICreateProfile, ICreateUser, LoginUser, PasswordReset
)
from woofmate.models import DogProfile
from woofmate.functions.user_service import UserServices

UserServices = UserServices()


class DogServices:
    """
    Contains the methods to handle any services related to the dogs
    and the database
    """

    def get_one_profile(self, db: Session, **kwargs):
        """
        Method to get one profile from the database depending
        on the search criteria e.g id, email, etc
        """
        profile = db.query(DogProfile).filter_by(**kwargs).first()
        return profile

    async def create_dog(
        self, db: Session, name: str, age: int, gender: str, breed: str,
        description: str, city: str, state: str, country: str,
        relationship_preferences: str, dog_image_1_url: str,
        dog_image_2_url: str, dog_image_3_url: str, current_user: str
    ):
        """
        Method to create a new dog profile and save it to the database
        only if the user is logged in.
        """
        get_user = UserServices.get_one_user(db, email=current_user)
        if not get_user:
            raise HTTPException(
                status_code=400,
                detail="Please Log in to your account"
            )

        new_dog_profile = DogProfile(
            name=name, age=age, gender=gender, breed=breed,
            description=description, city=city, state=state,
            country=country, relationship_preferences=relationship_preferences,
            dog_image_1=dog_image_1_url, dog_image_2=dog_image_2_url,
            dog_image_3=dog_image_3_url, user_id=f'{get_user.id}'
        )

        db.add(new_dog_profile)
        db.commit()
        db.refresh(new_dog_profile)

        return ({"message": "New dog created successfully"})

    async def get_allProfiles_of_user(
        self, db: Session, current_user, skip: int, limit: int = 20
    ):
        """
        Method to get all the profiles of a user after validating that
        the user is logged in and the current user is the owner of the dog
        """
        get_user = UserServices.get_one_user(db, email=current_user)
        get_all_profiles = (
            db.query(DogProfile).filter_by(
                user_id=get_user.id
            ).offset(skip).limit(limit).all()
        )
        return get_all_profiles
