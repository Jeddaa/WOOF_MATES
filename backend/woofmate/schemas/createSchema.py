from pydantic import BaseModel

from woofmate.schemas.type import Breed, Gender, Relationship
# from dtos.type import Breed, Gender, Relationship


class ICreateProfile(BaseModel):
    username:str
    age: int
    city: str
    state: str
    RelationshipPreferences: Relationship
    pictureFilename: str
    picture: bytes
    breed: Breed
    gender: Gender



class IProfile(ICreateProfile):
    # id: int
    user: int

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


class IUser(ICreateUser):
    # id: int
    is_active: bool
    profiles: list[IProfile] = []

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
