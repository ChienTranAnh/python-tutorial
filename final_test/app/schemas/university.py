from pydantic import BaseModel, EmailStr

# tạo mới
class UniversityCreate(BaseModel):
    uni_name: str
    address: str
    phone: str
    email: EmailStr
    website: str

# set thông tin trả về
class UniversityResponse(BaseModel):
    id: int
    uni_name: str
    phone: str
    email: EmailStr
    address: str

    class Config:
        orm_mode = True
