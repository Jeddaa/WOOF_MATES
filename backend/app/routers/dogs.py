"""
Contains the dog routes and endpoints relating
to the dog
"""

from fastapi import APIRouter, HTTPException, Response, status
from fastapi.params import Depends
from app.auth import Auth
from app.database import SessionLocal

db = SessionLocal()

auth = Auth(db)

router = APIRouter(
    tags=['Dogs']
)

@router.get('/')
def index():
    return {'detail': "Testing is successful"}