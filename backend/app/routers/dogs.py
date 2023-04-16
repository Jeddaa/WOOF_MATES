"""
Contains the dog routes and endpoints relating
to the dog
"""

from app.database import get_db
from app.crud import Crud
from app.schemas import Dog
from app.mycloudinary import upload_image_to_cloudinary
from fastapi import APIRouter, File, Form, HTTPException, Path, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import Annotated

router = APIRouter(
    tags=['Dogs']
)

crud = Crud()


@router.post('/users/{user_id}/dogs', response_model=Dog)
async def create_dog_for_user(
    dog_images: Annotated[list[bytes], File()],
    name: str = Form(...), age: int = Form(...), gender: str = Form(...),
    breed: str = Form(...), city: str = Form(...), state: str = Form(...),
    country: str = Form(...), description: str = Form(...),
    relationship_preferences: str = Form(...), user_id: int = Path(...),
    db: Session = Depends(get_db)
):

    """
    Creates a dog for a specific user after validating
    all the required inputs and constraints
    """
    if not name:
        raise HTTPException(status_code=400, detail="Name is required")
    if not age:
        raise HTTPException(status_code=400, detail="Age is required")
    if not gender:
        raise HTTPException(status_code=400, detail="Gender is required")
    if not breed:
        raise HTTPException(status_code=400, detail="Breed is required")
    if not city:
        raise HTTPException(status_code=400, detail="City is required")
    if not state:
        raise HTTPException(status_code=400, detail="State is required")
    if not country:
        raise HTTPException(status_code=400, detail="Country is required")
    if not description:
        raise HTTPException(status_code=400, detail="Description is required")
    if not relationship_preferences:
        raise HTTPException(
            status_code=400,
            detail="Relationship preferences are required"
        )

    existing_user = crud.get_user_by(db, id=user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="Owner not found")
    user_id = existing_user.id
    print(user_id)

    if len(dog_images) != 3:
        raise HTTPException(status_code=400, detail="Please upload 3 images")
    dog_images_url = [
        await upload_image_to_cloudinary(
            'WOOF_MATES_DOGS',
            image,
            f'{existing_user.username}',
            'dog_image') for image in dog_images
    ]
    if not dog_images_url:
        raise HTTPException(
            status_code=500,
            detail="Failed to upload images to cloudinary"
        )
    new_dog = crud.create_user_dogs(
        name, age, gender, breed, city, state, country, description,
        relationship_preferences, dog_images_url, user_id
    )
    return new_dog
