from sqlalchemy.orm import Session
from app.api.v1.models.log import LogCreate
from app.crud.log import create_log

def save_log(db: Session, status: int, user_id: int, log_type: str, message: str):
    log_entry = LogCreate(
        status=status,
        user_id=user_id if user_id is not None else None,
        type=log_type,
        message=message
    )
    create_log(db, log_entry)
