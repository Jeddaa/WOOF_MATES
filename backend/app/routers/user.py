"""
Contains the user routes and endpoints relating
to the users which is the dog owner
"""

from fastapi import APIRouter, HTTPException, Response, Status
from fastapi.params import Depends

router = APIRouter(
    tags=['Users']
)

