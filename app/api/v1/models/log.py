from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class LogBase(BaseModel):
    status: int
    user_id: Optional[int]
    type: str
    message: str

    class Config:
        json_schema_extra = {
            "example": {
                "log_id": 1,
                "created_at": 1628078602,
                "status": "Information",
                "user_id": 0,
                "type": "app/api/v1/logs",
                "message": "Action performed"
            }
        }

class LogCreate(LogBase):
    pass

class LogInDB(LogBase):
    log_id: int

class LogResponse(LogInDB):
    pass