# app/api/v1/endpoints/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from typing import Annotated,List
from app.api.v1.models.user import UserCreate, UserUpdate, UserResponse
from app.crud.user import create_user, get_user, get_users, update_user, delete_user
from app.core.exceptions.exceptions import UserNotFoundException, DatabaseException
from app.core.logging.log_manager import save_log
from . import endpoints

router = APIRouter()

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
    try:
        db_user = create_user(db, user)
        save_log(db, 1, db_user.user_id, "create_user", f"User {db_user.username} created.")
        return db_user
    except Exception as e:
        db.rollback()
        save_log(db, 0, None, "create_user", f"Error creating user: {e}")
        raise DatabaseException()

@router.get(users, response_model=List[UserResponse], status_code=code_200)
async def read_all_users_endpoint(db: db_depency):
    """
    Read all users.

    - **returns**: List of UserResponse objects with users' details
    """
    try:
        users_list = get_users(db)
        save_log(db, 1, None, "read_all_users", f"Fetched {len(users_list)} users.")
        return users_list
    except Exception as e:
        db.rollback()
        save_log(db, 1, None, "read_all_users", f"Error fetching users: {e}")
        raise DatabaseException()

@router.get(users + "/{user_id}", response_model=UserResponse, status_code=code_200)
async def read_user_endpoint(user_id: int, db: db_depency):
    """
    Read a user by ID.

    - **user_id**: The ID of the user to retrieve
    - **returns**: UserResponse object with user details
    """
    try:
        user = get_user(db, user_id)
        if not user:
            save_log(db, 1, None, "read_user", f"User not found with ID: {user_id}")
            raise UserNotFoundException()
        save_log(db, 1, user_id, "read_user", f"User found with ID: {user_id}")
        return user
    except UserNotFoundException as e:
        db.rollback()
        save_log(db, 0, None, "read_user", f"User with ID {user_id} not found.")
        raise e
    except Exception as e:
        db.rollback()
        save_log(db, 0, None, "read_user", f"Error retrieving user: {e}")
        raise DatabaseException()

@router.put(users + "/{user_id}", response_model=UserResponse, status_code=code_200)
async def update_user_endpoint(user_id: int, user: UserUpdate, db: db_depency):
    """
    Update a user by ID.

    - **user_id**: The ID of the user to update
    - **user**: UserUpdate object containing updated user details
    - **returns**: UserResponse object with updated user details
    """
    logger.info(f"Updating user with ID: {user_id}")
    try:
        db_user = get_user(db, user_id)
        if not db_user:
            save_log(db, 1, None, "read_user", f"User not found with ID: {user_id}")
            raise UserNotFoundException()
        updated_user = update_user(db, db_user, user)
        save_log(db, 1, user_id, "update_user", f"User updated with ID: {user_id}")
        return updated_user
    except UserNotFoundException as e:
        db.rollback()
        save_log(db, 0, None, "update_user", f"User with ID {user_id} not found.")
        raise e
    except Exception as e:
        db.rollback()
        save_log(db, 0, None, "read_user", f"Error retrieving user: {e}")
        raise DatabaseException()

@router.delete(users + "/{user_id}", response_model=UserResponse, status_code=code_200)
async def delete_user_endpoint(user_id: int, db: db_depency):
    """
    Delete a user by ID.

    - **user_id**: The ID of the user to delete
    - **returns**: UserResponse object with deleted user details
    """
    try:
        user = get_user(db, user_id)
        if not user:
            save_log(db, 1, None, "read_user", f"User not found with ID: {user_id}")
            raise UserNotFoundException()
        deleted_user = delete_user(db, user)
        save_log(db, 1, user_id, "delete_user", f"User with ID {user_id} deleted.")
        return deleted_user
    except UserNotFoundException as e:
        db.rollback()
        save_log(db, 0, None, "delete_user", f"User with ID {user_id} not found.")
        raise e
    except Exception as e:
        db.rollback()
        save_log(db, 0, None, "read_user", f"Error deleting user: {e}")
        raise DatabaseException()

# Notifications

@router.get(notif, status_code=code_200)
async def read_all_access():
    logger.info("Accessing notifications endpoint")
    return {"message": "Notifications endpoint"}