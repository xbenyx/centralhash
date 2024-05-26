# app/api/v1/endpoints/users.py
from fastapi import APIRouter
from . import endpoints

router = APIRouter()

@router.get(endpoints.NOTIFICATIONS)
async def read_access():
    return {"message": "Notifications endpoint"}

@router.get(endpoints.USERS)
async def read_access():
    return {"message": "Users endpoint"}
