from fastapi import File
from pydantic import BaseModel
from typing import List, Annotated
from woofmate.schemas.type import Breed, Gender, Relationship
# from dtos.type import Breed, Gender, Relationship


class ICreateProfile(BaseModel):
    username:str
    age: int
    city: str
    state: str
    relationshipPreferences: Relationship
    # picture: Annotated[list[bytes], File()]
    breed: Breed
    gender: Gender
    class Config:
        orm_mode = True



class IProfile(BaseModel):
    user_id: int
    username:str
    age: int
    city: str
    state: str
    RelationshipPreferences: Relationship
    breed: Breed
    gender: Gender
    pictureFilename: str

    class Config:
        orm_mode = True


class ICreateUser(BaseModel):
    firstName:str
    lastName:str
    email: str
    password: str
    class Config:
        schema_extra={
            "firstname": "john",
            "lastname": "doe",
            "email": "johndoe@gmail.com",
            "password": "password"
        }
        orm_mode = True


class IUser(BaseModel):
    firstName:str
    lastName:str
    email: str
    is_active: bool
    dogprofiles: List[IProfile] = []
    class Config:
        orm_mode = True


class LoginUser(BaseModel):
    email:str
    password:str
    class Config:
        schema_extra={
            "email": "johndoe@gmail.com",
            "password": "password"
        }
        orm_mode=True

class PasswordReset(BaseModel):
    email: str
