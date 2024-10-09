from datetime import date
from typing import List
from pydantic import BaseModel, EmailStr, validator, root_validator

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    birth: str
    sex: int
    phone: str
    email: EmailStr
    classes: str
    major: str
    graduation_year: int
    university_id: int
    skill: List[str]

class StudentResponse(StudentCreate):
    id: int
    # first_name: str
    # last_name: str
    # birth: str
    # sex: int
    # phone: str
    # email: EmailStr
    skill: str
    name: str = ''

    @validator('birth', pre=True)
    def birth_format(cls, value):
        if isinstance(value, date):
            return value.strftime('%d/%m/%Y')
        return value

    class Config:
        orm_mode = True

"""
    @root_validator(pre=True)
    def full_name(cls, values):
        # Kiểm tra kiểu dữ liệu của `values`
        print(f"Values type: {type(values)}")
        if isinstance(values, dict):  # Kiểm tra nếu `values` là `dict`
            first_name = values.get("first_name", "")
            last_name = values.get("last_name", "")
            values["name"] = f"{first_name} {last_name}"
        return values
"""
    # @validator("name", pre=True)
    # def full_name(cls, value, values):
    #     first_name = value.first_name
    #     last_name = values.last_name
    #     return f"{first_name} {last_name}"
