from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.database import Base

class User(Base):
    __tablename__ = 'users'
    userid = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    mobile = Column(String, unique=True, index=True, nullable=False)
    dob = Column(Date, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    password_hashed = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login_time = Column(DateTime, default = None)
