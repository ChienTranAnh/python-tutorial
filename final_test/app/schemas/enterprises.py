from pydantic import BaseModel, EmailStr

class EnterprisesCreate(BaseModel):
    company_name: str
    address: str
    phone: str
    email: EmailStr
    website: str
    industry: str
    scale: int
    about: str

class EnterprisesResponse(BaseModel):
    id: int
    company_name: str
    phone: str
    email: EmailStr
    address: str

    class Config:
        orm_mode = True
