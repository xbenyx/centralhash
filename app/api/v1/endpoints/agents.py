# app/api/v1/endpoints/agents.py
from fastapi import APIRouter
from . import endpoints

router = APIRouter()

@router.get(endpoints.AGENTS)
async def read_access():
    return {"message": "Agents endpoint"}

@router.get(endpoints.AGENT_STATS)
async def read_access():
    return {"message": "Agent Stats endpoint"}

@router.get(endpoints.AGENT_ASSIGNMENT)
async def read_access():
    return {"message": "Agent Assignements endpoint"}

@router.get(endpoints.VOUCHERS)
async def read_access():
    return {"message": "Vouchers endpoint"}

