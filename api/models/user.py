from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, EmailStr, Field
from enum import Enum as PyEnum
from typing import Optional

Base = declarative_base()

class Role(PyEnum):
    USER = "user"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(Role), default=Role.USER)
    device_id = Column(String, nullable=True, default=None)

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserInDB(BaseModel):
    id: int
    email: EmailStr
    role: Role = Role.USER
    device_id: Optional[str] = None