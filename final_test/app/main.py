from fastapi import FastAPI
from .models import Base
from .db import database
from .api.endpoints import users

app = FastAPI(title="Auto Career", version='1.0.0')

Base.metadata.create_all(bind=database.engine)

app.include_router(users.router, prefix='/api', tags=['Users'])

@app.get('/')
def read_root():
    return {"message": "Welcome to the fastAPI Auto Career"}
