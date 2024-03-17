from fastapi import APIRouter, Query, Response, status, HTTPException, Depends
from datetime import datetime
from .schemas import UserRegistration, UserBase
from src.database import get_db, SessionLocal
from .models import User
from passlib.context import CryptContext

auth_router = APIRouter(prefix='/auth', tags=["Users and Authentication"])
pwd_context = CryptContext(schemes = ['bcrypt'], deprecated = "auto")

@auth_router.post('/register', response_model=UserBase)
def register_user(user : UserRegistration, db = Depends(get_db)):
    db_user = db.query(User).filter(user.email == User.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail = "User with this email id already exists")
    if user.password == user.confirm_password:
        hashed_password = pwd_context.hash(user.password)
        new_user = User(name = user.name, email = user.email, mobile = user.mobile, dob = user.dob, is_active = 1, password_hashed = hashed_password, created_at = datetime.utcnow(), updated_at = datetime.utcnow())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        raise HTTPException(status_code=400, detail = "Both Passwords Do not Match")

