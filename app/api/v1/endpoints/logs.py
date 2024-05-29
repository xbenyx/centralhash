# app/api/v1/endpoints/logs.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.log import Log
from typing import Annotated,List
from app.crud.log import create_log, get_log, get_logs
from app.api.v1.models.log import LogCreate, LogResponse
from app.core.exceptions.exceptions import UserNotFoundException, DatabaseException
from . import endpoints
import logging

router = APIRouter()

# Logs
logger = logging.getLogger(__name__)

# Dependency
db_depency = Annotated[Session,Depends(get_db)]

# Endpoints
logs = endpoints.LOGS

# Status Code
code_200 = status.HTTP_200_OK
code_201 = status.HTTP_201_CREATED

# Logs

@router.post(logs, response_model=LogResponse, status_code=code_201)
async def create_log_endpoint(log: LogCreate, db: db_depency):
    """
    Create log

    - **returns**: List of LogResponse objects with logs' details
    """
    try:
        db_user = create_log(db, log)
    except Exception as e:
        raise DatabaseException()
    return db_user

@router.get(logs, response_model=List[LogResponse], status_code=code_200)
async def read_all_logs_endpoint(db: db_depency):
    """
    Read all logs.

    - **returns**: List of LogResponse objects with logs' details
    """
    logger.info("Fetching all users")
    try:
        users = get_logs(db)
    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        raise DatabaseException()
    logger.info(f"Fetched {len(users)} users")
    return users

@router.get(logs + "/{log_id}", response_model=LogResponse, status_code=code_200)
async def read_log_endpoint(log_id: int, db: db_depency):
    """
    Read a log by ID.

    - **log_id**: The ID of the log to retrieve
    - **returns**: LogResponse object with log details
    """
    logger.info(f"Fetching user with ID: {log_id}")
    user = get_log(db, log_id)
    if not user:
        logger.error(f"User not found with ID: {log_id}")
        raise UserNotFoundException()
    logger.info(f"User found with ID: {log_id}")
    return user