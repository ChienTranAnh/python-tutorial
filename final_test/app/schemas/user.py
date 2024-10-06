from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    birth: str
    user_name: str
    password: str
    email: EmailStr
    role: int
    acc_type: int

class UserResponse(BaseModel):
    id: int
    name: str
    user_name: str
    email: EmailStr

    class Config:
        orm_mode = True
