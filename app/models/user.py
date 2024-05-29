# app/models/user.py
from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    f_name = Column(String(50), nullable=True)
    l_name = Column(String(50), nullable=True)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    remember_token = Column(String(256), nullable=True)
    status = Column(Boolean, default=True, nullable=False)
    updated_at = Column(BigInteger, nullable=False)
    created_at = Column(BigInteger, nullable=False)
    session_max = Column(Integer, nullable=False)
    role = Column(Integer, nullable=False)
