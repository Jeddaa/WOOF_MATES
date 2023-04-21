"""
Contains the pydantic models for database model
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, HttpUrl, validator, conlist


class UserBase(BaseModel):
    username: str
    email: EmailStr
    profile_picture_url: HttpUrl


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    # dogs: List["Dog"] = []

    class Config:
        orm_mode = True


class DogBase(BaseModel):
    name: str
    age: int
    gender: str
    breed: str
    city: str
    state: str
    country: str
    description: str
    relationshipPreferences: str
    pictures_url: List[HttpUrl]

    @validator('pictures_url')
    def validate_pictures(cls, v):
        return conlist(HttpUrl)(v)


class DogCreate(DogBase):
    owner_id: int


class Dog(DogBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    owner: User

    class Config:
        orm_mode = True
