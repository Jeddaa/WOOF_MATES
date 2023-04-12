"""
Contains the pydantic models for database model
"""

from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: Optional[str]
    email: Optional[str]


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    is_active: bool
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True


class DogBase(BaseModel):
    name: str
    age: int
    gender: str
    breed: str
    city: str
    state: str
    country: Optional[str] = "Nigeria"
    description: str
    relationshipPreferences: str
    pictureFilename: str
    picture: bytes


class DogCreate(DogBase):
    owner_id: int


class DogUpdate(DogBase):
    pass


class Dog(DogBase):
    id: int
    is_active: bool
    created_at: Optional[str]
    updated_at: Optional[str]
    owner: Optional[User]

    class Config:
        orm_mode = True


class UserWithDogs(User):
    dogs: List[Dog] = []

    class Config:
        orm_mode = True
