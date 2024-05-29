# app/core/exceptions/handlers.py
from fastapi import Request
from fastapi.responses import JSONResponse
import logging
from app.core.exceptions.exceptions import UserNotFoundException, DatabaseException

logger = logging.getLogger(__name__)

async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    logger.error(f"User not found: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

async def database_exception_handler(request: Request, exc: DatabaseException):
    logger.error(f"Database error: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
