from pydantic import BaseModel, EmailStr

# tạo mới doanh nghiệp
class EnterprisesCreate(BaseModel):
    company_name: str
    address: str
    phone: str
    email: EmailStr
    password: str
    website: str
    industry: str
    scale: int
    about: str

# set thông tin doanh nghiệp trả về
class EnterprisesResponse(BaseModel):
    id: int
    company_name: str
    phone: str
    email: EmailStr
    address: str

    class Config:
        orm_mode = True

# request thông tin đăng nhập
class EnterpriseLogin(BaseModel):
    email: EmailStr
    password: str

# request thông tin cập nhật doanh nghiệp
class EnterpriesUpdate(BaseModel):
    company_name: str
    phone: str
    email: EmailStr
    address: str
