from fastapi import FastAPI
from .models import Base
from .db import database
from .router import users
from .router import enterprises
from .router import employees
from .router import jobs

app = FastAPI(title="Auto Career API", version='1.0.0')

Base.metadata.create_all(bind=database.engine)

app.include_router(users.router, prefix='/api', tags=['Users'])
app.include_router(enterprises.router, prefix='/api', tags=['Enterprises'])
app.include_router(employees.router, prefix='/api', tags=['Employees'])
app.include_router(jobs.router, prefix='/api', tags=['Jobs'])

@app.get('/')
def read_root():
    return {"message": "Welcome to the fastAPI Auto Career"}
