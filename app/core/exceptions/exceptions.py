# app/core/exceptions/exceptions.py

from fastapi import HTTPException, status

class UserNotFoundException(HTTPException):
    def __init__(self, detail: str = "User not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class DatabaseException(HTTPException):
    def __init__(self, detail: str = "Database error occurred"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)