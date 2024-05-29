# app/utils/logger.py
from sqlalchemy.orm import Session
from app.models.log import Log
from app.api.v1.models.log import LogCreate

def create_log(db: Session, log: LogCreate):
    db_log = Log(**log.model_dump())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_log(db: Session, log_id: int):
    return db.query(Log).filter(Log.log_id == log_id).first()

def get_logs(db: Session):
    return db.query(Log).all()