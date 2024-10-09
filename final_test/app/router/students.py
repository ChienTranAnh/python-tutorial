from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union

from . import get_db
from ..crud import student as crud_student
from ..crud.university import get_university
from ..schemas import student as student_schemas

router = APIRouter()

@router.get('/universities/{university_id}/students', response_model=list[student_schemas.StudentResponse])
def read_students(university_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_university = get_university(db, university_id)
    if db_university is None:
        raise HTTPException(status_code=404, detail='University does not exist')

    return crud_student.get_students(db, university_id=university_id, skip=skip, limit=limit)

@router.post('/universities/{university_id}/students', response_model=student_schemas.StudentResponse)
def create_student(university_id: int, student: student_schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud_student.check_student(db, email=student.email)
    if db_student:
        raise HTTPException(status_code=400, detail='Student already exists')

    db_university = get_university(db, university_id)
    if db_university is None:
        raise HTTPException(status_code=404, detail='University does not exist')

    return crud_student.create_student(db=db, student=student, university_id=university_id)

# @router.delete('/universities/{university_id}/students/{employee_id}')
# def employee_delete(university_id: int, employee_id: int, db: Session = Depends(get_db)):
#     db_student = crud_student.delete_student(db, company_id=university_id, staff_id=employee_id)
#     if db_student is None:
#         raise HTTPException(status_code=404, detail='Employee not found')

#     raise HTTPException(status_code=200, detail='Delete employee success!')
