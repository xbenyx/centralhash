# app/api/v1/endpoints/access.py
from fastapi import APIRouter
from . import endpoints

router = APIRouter()

@router.get(endpoints.ACCESS_GROUPS)
async def read_access():
    return {"message": "Access Groups endpoint"}

@router.get(endpoints.GLOBAL_PERMISSIONS_GROUPS)
async def read_access():
    return {"message": "Global Permissions Groups endpoint"}
