"""
Contains the user routes and endpoints relating
to the users which is the dog owner
"""

from fastapi import APIRouter, HTTPException, Response, status
from fastapi.params import Depends
from app.auth import Auth
from app.database import SessionLocal

db = SessionLocal()

auth = Auth(db)

router = APIRouter(
    tags=['Users']
)

