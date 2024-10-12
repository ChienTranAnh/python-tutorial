from datetime import date
from pydantic import BaseModel, validator

class ConnectiveCreate(BaseModel):
    # enterprise_id: int
    # status: int
    date_apply: str
    description: str

class ConnectiveResponse(BaseModel):
    id: int
    university_id: int
    status: int
    date_apply: str
    description: str

    @validator('date_apply', pre=True)
    def format_date_apply(cls, value):
        if isinstance(value, date):
            return value.strftime('%m/%d/%Y')
        return value

    class Config:
        orm_mode = True
