from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from typing import Dict

mpp = FastAPI()

class Address(BaseModel):
    city: str
    dictrict: str
    yard: str

class User(BaseModel):
    name: str
    age: int
    address: Address
    email: Optional[str] = None

class UserResponse(BaseModel):
    name: str
    age: int

@mpp.post('/users', response_model=UserResponse)
async def create(user: User):
    return user
    # return {"message": f"User \'{user.name}\' created successfully!", "data": user}

@mpp.post('/data')
def process_data(data: Dict[str, int]):
    return {"processed_data": {key: value * 2 for key, value in data.items()}}
