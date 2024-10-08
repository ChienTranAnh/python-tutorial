from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union

from . import get_db
from ..crud import employee as crud_staff
from ..crud.enterprises import get_enterprise
from ..schemas import employee as staff_schemas

router = APIRouter()

@router.get('/enterprises/{enterprise_id}/employees', response_model=list[staff_schemas.StaffResponse])
def read_employees(enterprise_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    # Lấy danh sách nhân viên
    employees = crud_staff.get_employees(db, company_id=enterprise_id, skip=skip, limit=limit)
    return employees

@router.post('/enterprises/{enterprise_id}/employees', response_model=staff_schemas.StaffResponse)
def create_employee(enterprise_id: int, employee: staff_schemas.StaffCreate, user_id: Union[int, None]=None, db: Session = Depends(get_db)):
    # Tạo nhân viên mới trong database
    db_staff = crud_staff.check_employee(db, email=employee.email)
    if db_staff:
        raise HTTPException(status_code=400, detail='Employee already exists')

    db_company = get_enterprise(db, enterprise_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail='Company does not exist')

    return crud_staff.create_employee(db=db, employee=employee, company_id=enterprise_id, user_id=user_id)

@router.delete('/enterprises/{enterprise_id}/employees/{employee_id}', response_model=staff_schemas.StaffResponse)
def employee_delete(enterprise_id: int, employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud_staff.delete_employee(db, company_id=enterprise_id, staff_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee not found')

    raise HTTPException(status_code=200, detail='Delete employee success!')
