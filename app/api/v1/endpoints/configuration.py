# app/api/v1/endpoints/configuration.py
from fastapi import APIRouter
from . import endpoints

router = APIRouter()

@router.get(endpoints.AGENT_BINARIES)
async def read_agent_binaries():
    return {"message": "Agent Binaries endpoint"}

@router.get(endpoints.CONFIGS)
async def read_configs():
    return {"message": "Configs endpoint"}

@router.get(endpoints.CRACKERS)
async def read_crackers():
    return {"message": "Crackers endpoint"}

@router.get(endpoints.CRACKER_TYPES)
async def read_cracker_types():
    return {"message": "Cracker Types endpoint"}

@router.get(endpoints.HASH_TYPES)
async def read_hash_types():
    return {"message": "Hash Types endpoint"}

@router.get(endpoints.HEALTH_CHECKS)
async def read_health_checks():
    return {"message": "Health Checks endpoint"}

@router.get(endpoints.HEALTH_CHECK_AGENTS)
async def read_health_check_agents():
    return {"message": "Health Checks Agents endpoint"}

@router.get(endpoints.LOG_ENTRIES)
async def read_log_entries():
    return {"message": "Log Entries endpoint"}

@router.get(endpoints.PRE_PROCESSORS)
async def read_pre_processors():
    return {"message": "Preprocessors endpoint"}
