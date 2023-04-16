from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, Depends
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from woofmate.schemas.createSchema import ICreateProfile, ICreateUser, LoginUser, PasswordReset
from woofmate.models import User, DogProfile
from woofmate.functions.user_service import UserServices
from woofmate.functions.my_cloudinary import upload_image_to_cloudinary




class DogServices:
    async def createDog(db, dogProfile: ICreateProfile, dog_images, current_user: str):
        get_user = await UserServices.get_one_user(db, email=current_user)
        # check_email = await db.query(DogProfile).filter(User.email == user.email).first()
        if get_user is None:
            raise HTTPException(status_code=400, detail="Please Log in to your account")
        #  new_user = await User(email=user.email, hashed_password=password, firstName=user.firstName, lastName=user.lastName)
        if len(dog_images) != 3:
            raise HTTPException(status_code=400, detail="Please upload 3 images")
        dogURL = [await upload_image_to_cloudinary( 'WOOF_MATES_DOGS', image, f'{get_user.username}','dog_image') for image in dog_images
                  ]
        if not dogURL:
            raise HTTPException(
            status_code=500,
            detail="Failed to upload images to cloudinary"
        )
        new_profile = await DogProfile(email=get_user.email, username=dogProfile.username, age=dogProfile.age, city=dogProfile.city, state=dogProfile.state, relationshipPreferences=dogProfile.relationshipPreferences, breed=dogProfile.breed, gender=dogProfile.gender, pictureURL=dogURL)
        # username:str
        # age: int
        # city: str
        # state: str
        # RelationshipPreferences: Relationship
        # picture: Annotated[list[bytes], File()]
        # breed: Breed
        # gender: Gender
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)
        return jsonable_encoder({"message": "New profile created successfully"})
