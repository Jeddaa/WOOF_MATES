from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, Depends
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from woofmate.schemas.createSchema import ICreateProfile, ICreateUser, LoginUser, PasswordReset
from woofmate.models import User, DogProfile
from woofmate.functions.user_service import UserServices
from woofmate.functions.my_cloudinary import upload_image_to_cloudinary




class DogServices:
    def get_one_profile(db, **kwargs):
        profile = db.query(DogProfile).filter_by(**kwargs).first()
        return profile

    async def createDog(db, dogProfile: ICreateProfile, current_user: str):
        get_user = UserServices.get_one_user(db, email=current_user)
        if get_user is None:
            raise HTTPException(status_code=400, detail="Please Log in to your account")
        new_profile = DogProfile(**dogProfile.dict(), email=f"{get_user.email}",user_id=f"{get_user.id}")
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)
        return new_profile.id
        # return jsonable_encoder({"message": "New profile created successfully"})

    async def upload_dog_images(db, id, dog_images, current_user):
        get_user = UserServices.get_one_user(db, email=current_user)
        confirm_profile = DogServices.get_one_profile(db, id=id)
        print(confirm_profile)
        if get_user.id == confirm_profile.user_id:
            print(type(dog_images))
            if len(dog_images) != 3:
                raise HTTPException(status_code=400, detail="Please upload 3 images")
            dogURL = [await upload_image_to_cloudinary( 'WOOF_MATES_DOGS', image, f'{get_user.firstName} {get_user.lastName}','dog_image') for image in dog_images
                    ]
            if not dogURL:
                raise HTTPException(
                status_code=500,
                detail="Failed to upload images to cloudinary"
            )
            confirm_profile.pictureURL = dogURL
            db.commit()
            return jsonable_encoder({"message": "images uploaded successfully"})

        return jsonable_encoder({"message": "kindly login and try again"})
