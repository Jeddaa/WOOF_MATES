from datetime import datetime
from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional
from woofmate.schemas.type import Breed, Gender, Relationship
# from dtos.type import Breed, Gender, Relationship


class ICreateProfile(BaseModel):
    name: str
    age: int
    gender: Gender
    breed: Breed
    description: Optional[str] = None
    city: str
    state: str
    country: str
    relationship_preferences: Relationship
    dog_image_1: HttpUrl
    dog_image_2: HttpUrl
    dog_image_3: HttpUrl

    class Config:
        orm_mode = True


class ICreateTestProfile(BaseModel):
    name: str
    age: int
    gender: Gender
    breed: Breed
    description: Optional[str] = None
    city: str
    state: str
    country: str
    relationship_preferences: Relationship
    dog_image_1: HttpUrl
    dog_image_2: HttpUrl
    dog_image_3: HttpUrl

    class Config:
        orm_mode = True


class IProfile(BaseModel):
    user_id: int
    name: str
    age: int
    gender: Gender
    breed: Breed
    description: Optional[str] = None
    city: str
    state: str
    country: str
    relationship_preferences: Relationship
    dog_image_1: HttpUrl
    dog_image_2: HttpUrl
    dog_image_3: HttpUrl

    class Config:
        orm_mode = True


class ICreateUser(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    profile_picture: HttpUrl

    class Config:
        schema_extra= {
            "firstname": "john",
            "lastname": "doe",
            "email": "johndoe@gmail.com",
            "password": "password",
            "profile_picture": "https://cloudinary.com/"
        }
        orm_mode = True


class IUser(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    profile_picture: HttpUrl
    is_active: bool
    dogprofiles: List[IProfile] = []

    class Config:
        orm_mode = True


class LoginUser(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra= {
            "email": "johndoe@gmail.com",
            "password": "password"
        }
        orm_mode = True


class PasswordReset(BaseModel):
    email: EmailStr


class DogProfileResponse(BaseModel):
    id: int
    owner_id: int
    name: str
    age: Optional[int]
    breed: str
    gender: str
    description: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    relationship_preferences: Optional[str]
    dog_image_1: Optional[str]
    dog_image_2: Optional[str]
    dog_image_3: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class UserWithDogs(BaseModel):
    id: int
    email: str
    firstName: Optional[str]
    lastName: Optional[str]
    profile_picture: Optional[str]
    is_active: Optional[bool]
    created_at: datetime
    updated_at: Optional[datetime] = None
    dogProfiles: Optional[List[DogProfileResponse]] = []

    class Config:
        orm_mode = True
