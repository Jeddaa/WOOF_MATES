from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, Depends
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from woofmate.schemas.createSchema import ICreateProfile, ICreateUser, LoginUser, PasswordReset
from woofmate.models import User, DogProfile
from woofmate.functions.user_service import UserServices
from woofmate.functions.my_cloudinary import upload_image_to_cloudinary


class DogServices:
    def get_one_profile(self, db, **kwargs):
        """
        Method to get one profile from the database depending on the
        search criteria e.g id, email, etc
        """
        profile = db.query(DogProfile).filter_by(**kwargs).first()
        return profile

    async def createDog(self, db, dogProfile: ICreateProfile, current_user: str):
        """
        Method to create a new dog profile and save it to the database
        only if the user is logged in.
        """
        get_user = UserServices.get_one_user(db, email=current_user)
        if get_user is None:
            raise HTTPException(
                status_code=400,
                detail="Please Log in to your account"
            )

        new_profile = DogProfile(
            **dogProfile.dict(),
            email=f"{get_user.email}",
            user_id=f"{get_user.id}"
        )

        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)
        return new_profile.id
        # return jsonable_encoder({"message": "New profile created successfully"})

    async def upload_dog_images(self, db, id, dog_images, current_user):
        """
        Method to upload images to cloudinary and save the url to the database
        """
        get_user = UserServices.get_one_user(db, email=current_user)
        confirm_profile = DogServices.get_one_profile(db, id=id)

        if get_user.id == confirm_profile.user_id:
            # Validate the number of images uploaded
            if len(dog_images) != 3:
                raise HTTPException(status_code=400, detail="Please upload 3 images")
            dogURL = [await upload_image_to_cloudinary(
                'WOOF_MATES_DOGS',
                image,
                f'{get_user.firstName} {get_user.lastName}',
                'dog_image'
                ) for image in dog_images
            ]

            # Checks that all images were uploaded successfully
            if not dogURL:
                raise HTTPException(
                status_code=500,
                detail="Failed to upload images to cloudinary"
            )
            confirm_profile.pictureURL = dogURL
            db.commit()
            return jsonable_encoder({"message": "images uploaded successfully"})

        return jsonable_encoder({"message": "kindly login and try again"})

    async def get_allProfiles_of_user(self, db, current_user):
        """
        Method to get all the profiles of a user after validating that
        the user is logged in and the current user is the owner of the dog
        """
        get_user = UserServices.get_one_user(db, email=current_user)
        get_all_profiles = db.query(DogProfile).filter_by(user_id=get_user.id).all()
        return get_all_profiles
