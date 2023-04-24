from typing import Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
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
        currentUser = UserServices.get_one_user(db, email=current_user)
        if not currentUser:
            raise HTTPException(
                status_code=400,
                detail="Please Log in to your account"
            )

        new_dog_profile = DogProfile(
            name=name, age=age, gender=gender, breed=breed,
            description=description, city=city, state=state,
            country=country, relationship_preferences=relationship_preferences,
            dog_image_1=dog_image_1_url, dog_image_2=dog_image_2_url,
            dog_image_3=dog_image_3_url, owner_id=f'{currentUser.id}'
        )

        db.add(new_dog_profile)
        db.commit()
        currentUser.dogProfiles.append(new_dog_profile)
        db.refresh(new_dog_profile)

        return ({"message": "New dog created successfully"})

    async def get_all_dog_profiles(
        self, db: Session, exclude_id: Optional[int] = None, **kwargs
    ):
        """
        Method to get all the profiles of the dogs in the database,
        filtered by the provided keyword arguments and excluding
        the dog profile with the given ID if provided
        """
        query = db.query(DogProfile)
        if exclude_id:
            query = query.filter(id != exclude_id)

        for key, value in kwargs.items():
            if hasattr(DogProfile, key):
                query = query.filter(getattr(DogProfile, key) == value)
        profiles = query.all()

        if not profiles:
            raise HTTPException(
                status_code=404,
                detail="No dog profiles found for this user"
            )
        return profiles

    async def get_dog_profiles_of_user(
        self, db: Session, current_user, skip: int, limit: int = 20
    ):
        """
        Method to get all the profiles of a user after validating that
        the user is logged in and the current user is the owner of the dog
        """
        get_user = UserServices.get_one_user(db, email=current_user)

        get_all_profiles = (
            db.query(DogProfile).filter_by(
                owner_id=get_user.id
            ).offset(skip).limit(limit).all()
        )

        if get_all_profiles == []:
            raise HTTPException(
                status_code=404,
                detail="No dog profiles found for this user"
            )
        return get_all_profiles

    async def update_dog_profile(
        self, db: Session, current_user: str, dog_id: int, age: int,
        description: str, city: str, state: str, country: str,
        relationship_preferences: str, dog_image_1_url: str,
        dog_image_2_url: str, dog_image_3_url: str
    ):
        """
        Method to update a dog profile after validating that the user
        is logged in and the current user is the owner of the dog
        """
        user = UserServices.get_one_user(db, email=current_user)
        dog = self.get_one_profile(db, id=dog_id)

        if not user:
            raise HTTPException(
                status_code=400,
                detail="Please Log in to your account"
            )

        if not dog:
            raise HTTPException(
                status_code=404,
                detail="Dog profile not found"
            )

        if user.id != dog.owner_id:
            raise HTTPException(
                status_code=401,
                detail="You are not authorized to update this profile"
            )

        # Checks if values are sent for the attributes, and if not
        # does nothing, i.e defaults to the original/former value

        if age:
            dog.age = age
        if description:
            dog.description = description
        if city:
            dog.city = city
        if state:
            dog.state = state
        if country:
            dog.country = country
        if relationship_preferences:
            dog.relationship_preferences = relationship_preferences
        if dog_image_1_url:
            dog.dog_image_1 = dog_image_1_url
        if dog_image_2_url:
            dog.dog_image_2 = dog_image_2_url
        if dog_image_3_url:
            dog.dog_image_3 = dog_image_3_url

        db.commit()
        db.refresh(dog)
        return ({"message": "Dog profile updated successfully"})


    async def delete_dog_profile(
        self, db: Session, current_user: str, dog_id: int
    ):
        """A method to delete a user's dog profile"""

        user = UserServices.get_one_user(db, email=current_user)
        dog = self.get_one_profile(db, id=dog_id)

        if not user:
            raise HTTPException(
                status_code=400,
                detail="Please Log in to your account"
            )

        if not dog:
            raise HTTPException(
                status_code=404,
                detail="Dog profile not found"
            )

        if user.id != dog.owner_id:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized"
            )

        db.delete(dog)
        db.commit()
        return {"detail": "Deleted Dog profile successfully"}

    async def match_dog_of_same_breed(self, db: Session, profile1, profile2):
        """ a matching function to compare two dogprofiles"""
        score = 0
        if profile1.breed == profile2.breed:
            score += 10
        if abs(profile1.age - profile2.age) <= 2:
            score += 5
        if profile1.gender != profile2.gender:
            score += 5
        if profile1.city == profile2.city:
            score += 5
        if profile1.state == profile2.state:
            score += 5
        if profile1.relationship_preferences == profile2.relationship_preferences:
            score += 5
        return score

    async def match_dog_of_diff_breed(self, db: Session, profile1, profile2):
        """ a matching function to compare two dogprofiles"""
        score = 0
        if abs(profile1.age - profile2.age) <= 2:
            score += 5
        if profile1.gender != profile2.gender:
            score += 5
        if profile1.city == profile2.city:
            score += 5
        if profile1.state == profile2.state:
            score += 5
        if profile1.relationship_preferences == profile2.relationship_preferences:
            score += 5
        return score
