from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    f_name: Optional[str] = Field(None, max_length=50)
    l_name: Optional[str] = Field(None, max_length=50)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=6, max_length=256)
    remember_token: Optional[str] = Field(None, max_length=256)
    status: bool = Field(...)
    updated_at: int = Field(...)
    created_at: int = Field(...)
    session_max: int = Field(...)
    role: int = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "f_name": "John",
                "l_name": "Doe",
                "email": "johndoe@example.com",
                "password": "strongpassword123",
                "remember_token": "sometoken",
                "status": True,
                "updated_at": 1628078602,
                "created_at": 1628078602,
                "session_max": 5,
                "role": 1
            }
        }

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=1, max_length=50)
    f_name: Optional[str] = Field(None, max_length=50)
    l_name: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr] = Field(None)
    password: Optional[str] = Field(None, min_length=6, max_length=256)
    remember_token: Optional[str] = Field(None, max_length=256)
    status: Optional[bool] = Field(None)
    updated_at: Optional[int] = Field(None)
    created_at: Optional[int] = Field(None)
    session_max: Optional[int] = Field(None)
    role: Optional[int] = Field(None)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "f_name": "John",
                "l_name": "Doe",
                "email": "johndoe@example.com",
                "password": "newstrongpassword123",
                "remember_token": "sometoken",
                "status": True,
                "updated_at": 1628078602,
                "created_at": 1628078602,
                "session_max": 5,
                "role": 1
            }
        }

class UserInDB(UserBase):
    user_id: int

class UserResponse(UserInDB):
    pass
