"""
Contains the user routes and endpoints relating
to the users which is the dog owner
"""

from app.crud import Crud, hash_password, verify_password
from app.schemas import Dog, UserCreate, User
from app.mycloudinary import upload_image_to_cloudinary
from app.database import get_db
from app.config import settings
from datetime import datetime, timedelta
from fastapi import APIRouter, File, Form, HTTPException, Path, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from typing import Annotated, Optional, Union


router = APIRouter(
    tags=['Users']
)

crud = Crud()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post(
    '/register_user',
    response_model=User,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    profile_image: Annotated[bytes, File()],
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    """
    Sign up route to register user
    """
    if not username:
        raise HTTPException(status_code=400, detail="Username is required")
    if not password:
        raise HTTPException(status_code=400, detail="Password is required")
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")
    if profile_image is None:
        raise HTTPException(
            status_code=400, detail="Profile picture is required"
        )

    # Limits the file upload to 1MB
    if len(profile_image) > 1000000:
        raise HTTPException(
            status_code=400,
            detail="Profile picture shouldn't be greater than 1MB"
        )

    # Validates the user by checking if the email or username exists before
    existing_user = crud.get_user_by(db, username=username)
    if existing_user:
        raise HTTPException(
            status_code=400, detail=f"{username} already exists"
        )
    existing_email = crud.get_user_by(db, email=email)
    if existing_email:
        raise HTTPException(status_code=400, detail=f"{email} already exists")

    # Upload image to Cloudinary
    profile_image_url = await upload_image_to_cloudinary(
        'WOOF_MATES_USERS', profile_image, username, 'profile_image'
    )

    if not profile_image_url:
        raise HTTPException(status_code=500, detail="Failed to upload image")

    # Create user with the profile picture URL
    user = crud.create_user(db, username, email, password, profile_image_url)

    return user


@router.get("/users", response_model=list[User])
def read_users(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """
    Gets the users in the database and applies pagination using
    the skip and limit to avoid lagging and too much informations

    """
    users = crud.get_users(db, skip=skip, limit=limit)
    if len(users) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user(s) found"
        )
    return users


@router.get('/users/{user_id}', response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Gets the user in the database by filtering the user_id"""
    user = crud.get_user_by(db, id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
