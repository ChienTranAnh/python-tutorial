from pydantic import BaseModel, EmailStr
from typing import List

# tạo mới
class UniversityCreate(BaseModel):
    uni_name: str
    address: str
    phone: str
    email: EmailStr
    password: str
    website: str
    major: List[str]

# set thông tin trả về
class UniversityResponse(BaseModel):
    id: int
    uni_name: str
    phone: str
    email: EmailStr
    address: str
    major: str

    class Config:
        orm_mode = True
