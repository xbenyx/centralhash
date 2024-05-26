# app/api/v1/endpoints/files.py
from fastapi import APIRouter
from . import endpoints

router = APIRouter()

@router.get(endpoints.FILES)
async def read_access():
    return {"message": "Files endpoint"}