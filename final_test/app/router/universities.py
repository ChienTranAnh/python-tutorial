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

# @router.put('/universities/{enterprise_id}')
# def update_enterprise(enterprise_id: int, enterprise: university_schema.UniversityCreate, db: Session = Depends(get_db)):
#     detail_enterprise = crud_university.get_enterprise(db, company_id=enterprise_id)
#     if detail_enterprise is None:
#         raise HTTPException(status_code=404, detail='Company not found')
    
#     return crud_university.update_enterprise(db=db, company_detail=detail_enterprise, company=enterprise)
