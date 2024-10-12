from typing import Union
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import get_db
from ..crud import university as crud_university
from ..crud.university import search_universities
from ..schemas import university as university_schema

router = APIRouter()

@router.get('/universities/', response_model=list[university_schema.UniversityResponse])
def read_enterprises(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_university.get_universities(db=db, skip=skip, limit=limit)

@router.post('/universities/', response_model=university_schema.UniversityResponse)
def create_university(university: university_schema.UniversityCreate, db: Session = Depends(get_db)):
    db_university = crud_university.check_university(db, email=university.email)
    if db_university:
        raise HTTPException(status_code=400, detail='University already exists')

    return crud_university.create_university(db=db, university=university)
