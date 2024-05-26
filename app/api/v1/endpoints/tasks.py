# app/api/v1/endpoints/tasks.py
from fastapi import APIRouter
from . import endpoints

router = APIRouter()

@router.get(endpoints.CHUNKS)
async def read_access():
    return {"message": "Chunks endpoint"}

@router.get(endpoints.PRETASKS)
async def read_access():
    return {"message": "Pretasks endpoint"}

@router.get(endpoints.SPEEDS)
async def read_access():
    return {"message": "Speed endpoint"}

@router.get(endpoints.SUPERTASKS)
async def read_access():
    return {"message": "Supertasks endpoint"}

@router.get(endpoints.TASKS)
async def read_access():
    return {"message": "Tasks endpoint"}

@router.get(endpoints.TASKWRAPPERS)
async def read_access():
    return {"message": "Task Wrapper endpoint"}