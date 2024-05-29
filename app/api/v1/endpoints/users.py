# app/api/v1/endpoints/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from typing import Annotated,List
from app.api.v1.models.user import UserCreate, UserUpdate, UserResponse
from app.crud.user import create_user, get_user, get_users, update_user, delete_user
from app.core.exceptions.exceptions import UserNotFoundException, DatabaseException
from . import endpoints
import logging

router = APIRouter()

# Logs
logger = logging.getLogger(__name__)

# Dependency
db_depency = Annotated[Session,Depends(get_db)]

# Endpoints
users = endpoints.USERS
notif = endpoints.NOTIFICATIONS

# Status Code
code_200 = status.HTTP_200_OK
code_201 = status.HTTP_201_CREATED

# Users

@router.post(users, response_model=UserResponse, status_code=code_201)
async def create_user_endpoint(user: UserCreate, db: db_depency):
    """
    Create user

    - **returns**: List of UserResponse objects with users' details
    """
    logger.info("Creating a new user")
    try:
        db_user = create_user(db, user)
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise DatabaseException()
    logger.info(f"User created with ID: {db_user.id}")
    return db_user

@router.get(users, response_model=List[UserResponse], status_code=code_200)
async def read_all_users_endpoint(db: db_depency):
    """
    Read all users.

    - **returns**: List of UserResponse objects with users' details
    """
    logger.info("Fetching all users")
    try:
        users = get_users(db)
    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        raise DatabaseException()
    logger.info(f"Fetched {len(users)} users")
    return users

@router.get(users + "/{user_id}", response_model=UserResponse, status_code=code_200)
async def read_user_endpoint(user_id: int, db: db_depency):
    """
    Read a user by ID.

    - **user_id**: The ID of the user to retrieve
    - **returns**: UserResponse object with user details
    """
    logger.info(f"Fetching user with ID: {user_id}")
    user = get_user(db, user_id)
    if not user:
        logger.error(f"User not found with ID: {user_id}")
        raise UserNotFoundException()
    logger.info(f"User found with ID: {user_id}")
    return user

@router.put(users + "/{user_id}", response_model=UserResponse, status_code=code_200)
async def update_user_endpoint(user_id: int, user: UserUpdate, db: db_depency):
    """
    Update a user by ID.

    - **user_id**: The ID of the user to update
    - **user**: UserUpdate object containing updated user details
    - **returns**: UserResponse object with updated user details
    """
    logger.info(f"Updating user with ID: {user_id}")
    db_user = get_user(db, user_id)
    if not db_user:
        logger.error(f"User not found with ID: {user_id}")
        raise UserNotFoundException()
    try:
        updated_user = update_user(db, db_user, user)
    except Exception as e:
        logger.error(f"Error updating user: {e}")
        raise DatabaseException()
    logger.info(f"User updated with ID: {user_id}")
    return updated_user

@router.delete(users + "/{user_id}", response_model=UserResponse, status_code=code_200)
async def delete_user_endpoint(user_id: int, db: db_depency):
    """
    Delete a user by ID.

    - **user_id**: The ID of the user to delete
    - **returns**: UserResponse object with deleted user details
    """
    logger.info(f"Deleting user with ID: {user_id}")
    user = get_user(db, user_id)
    if not user:
        logger.error(f"User not found with ID: {user_id}")
        raise UserNotFoundException()
    try:
        deleted_user = delete_user(db, user)
    except Exception as e:
        logger.error(f"Error deleting user: {e}")
        raise DatabaseException()
    logger.info(f"User deleted with ID: {user_id}")
    return deleted_user

# Notifications

@router.get(notif, status_code=code_200)
async def read_all_access():
    logger.info("Accessing notifications endpoint")
    return {"message": "Notifications endpoint"}