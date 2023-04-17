from pydantic import BaseModel
from typing import Optional
from woofmate.schemas.type import Breed, Gender, Relationship

class IUpdateProfile(BaseModel):
    firstName:Optional[str]
    lastName:Optional[str]
    username:Optional[str]
    age:Optional[str]
    city:Optional[str]
    state:Optional[str]
    RelationshipPreferences:Optional[Relationship]
    pictureFilename:Optional[str]
    picture:Optional[bytes]
    breed:Optional[Breed]
    gender:Optional[Gender]
