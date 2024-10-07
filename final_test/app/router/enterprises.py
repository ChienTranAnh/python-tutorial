from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import get_db
from ..crud import enterprises as crud_businesses
from ..schemas import enterprises as businesses_schema

router = APIRouter()

@router.get('/enterprises/', response_model=list[businesses_schema.EnterprisesResponse])
def read_enterprises(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    # Lấy danh sách daonh nghiệp
    enterprises = crud_businesses.get_enterprises(db, skip=skip, limit=limit)
    return enterprises

@router.post('/enterprises/', response_model=businesses_schema.EnterprisesResponse)
def create_enterprise(enterprise: businesses_schema.EnterprisesCreate, db: Session = Depends(get_db)):
    # Tạo daonh nghiệp mới trong database
    db_enterprise = crud_businesses.check_enterprise(db, email=enterprise.email)
    if db_enterprise:
        raise HTTPException(status_code=400, detail='Company already exists')

    return crud_businesses.create_enterprise(db=db, enterprise=enterprise)

@router.get('/enterprises/{company_id}', response_model=businesses_schema.EnterprisesResponse)
def enterprise_detail(company_id: int, db: Session = Depends(get_db)):
    # Lấy thông tin một daonh nghiệp theo ID
    db_enterprise = crud_businesses.get_enterprise(db, company_id=company_id)
    if db_enterprise is None:
        raise HTTPException(status_code=404, detail='Company not found')

    return db_enterprise
