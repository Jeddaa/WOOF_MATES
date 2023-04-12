"""
Contains the dog routes and endpoints relating
to the dog
"""

from fastapi import APIRouter, HTTPException, Response, Status
from fastapi.params import Depends

router = APIRouter(
    tags=['Dogs']
)

@router.get('/')
def index():
    return {'detail': "Testing is successful"}