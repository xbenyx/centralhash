# app/api/v1/endpoints/auth.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/auth")
async def read_access():
    return {"message": "Auth endpoint"}