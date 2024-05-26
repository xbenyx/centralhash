# app/api/v1/endpoints/hashlists.py
from fastapi import APIRouter
from . import endpoints

router = APIRouter()

@router.get(endpoints.HASHES)
async def read_access():
    return {"message": "Hashes endpoint"}

@router.get(endpoints.HASHLISTS)
async def read_access():
    return {"message": "Hashlists endpoint"}

@router.get(endpoints.GROUP_HASHLISTS)
async def read_access():
    return {"message": "SuperHashlists endpoint"}