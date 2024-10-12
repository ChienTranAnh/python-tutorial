from pydantic import BaseModel, EmailStr

class StaffCreate(BaseModel):
    name: str
    birth: str
    sex: int
    phone: str
    position: str
    email: EmailStr
    password: str
    enterprise_id: int

class StaffResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    position: str
    phone: str

    class Config:
        orm_mode = True
