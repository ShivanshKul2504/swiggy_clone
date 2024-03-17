from pydantic import validator, BaseModel, EmailStr
from datetime import date, datetime


class UserRegistration(BaseModel):
    name : str
    mobile : int
    email : str
    dob : date
    password : str
    confirm_password : str
    
    
class UserBase(BaseModel):
    name : str
    email : str
    mobile : str
    dob : date
    is_active : bool
    password_hashed : str
    created_at : datetime
    updated_at : datetime


class UserSchema(UserRegistration):
    id : int
    
    class Config:
        orm_mode = True