from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db
from ..crud import enterprises as crud_company
from ..schemas import enterprises as company_schema

router = APIRouter()

    # Tạo mới doanh nghiệp
@router.post('/enterprises/', response_model=company_schema.EnterprisesResponse)
def create_enterprise(enterprise: company_schema.EnterprisesCreate, db: Session = Depends(get_db)):
    db_enterprise = crud_company.check_enterprise(db, company_email=enterprise.email)
    if db_enterprise:
        raise HTTPException(status_code=400, detail='Company already exists')

    return crud_company.create_enterprise(db=db, company=enterprise)

# đăng nhập doanh nghiệp
@router.post('/enterprises/login')
def login(enterprise_login: company_schema.EnterpriseLogin, db: Session = Depends(get_db)):
    detail_enterprise = crud_company.authenticate_enterprise(db, email=enterprise_login.email, password=enterprise_login.password)
    if detail_enterprise is None:
        raise HTTPException(status_code=404, detail='Company not found')
    if detail_enterprise is False:
        raise HTTPException(status_code=400, detail='Wrong password or email')

    return detail_enterprise

# cập nhật thông tin doanh nghiệp
@router.put('/enterprises/{enterprise_id}')
def update_enterprise(enterprise_id: int, enterprise: company_schema.EnterpriesUpdate, db: Session = Depends(get_db)):
    detail_enterprise = crud_company.get_enterprise(db, company_id=enterprise_id)
    if detail_enterprise is None:
        raise HTTPException(status_code=404, detail='Company not found')
    
    return crud_company.update_enterprise(db=db, company_detail=detail_enterprise, company=enterprise)

# đổi mật khẩu
@router.put('/enterprises/change-password/{enterprise_id}')
def change_password(enterprise_id: int, old_pass: str, new_pass: str, db: Session = Depends(get_db)):
    detail_enterprise = crud_company.get_enterprise(db, company_id=enterprise_id)
    if detail_enterprise is None:
        raise HTTPException(status_code=404, detail='Company not found')

    result = crud_company.change_pass(db=db, old_pass=old_pass, new_pass=new_pass, company_detail=detail_enterprise)
    if result is False:
        raise HTTPException(status_code=400, detail='Change password don\'t success')

    raise HTTPException(status_code=200, detail='Change password success')

"""
@router.get('/enterprises/', response_model=list[company_schema.EnterprisesResponse])
def read_enterprises(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    # Lấy danh sách daonh nghiệp
    enterprises = crud_company.get_enterprises(db, skip=skip, limit=limit)
    return enterprises
"""
"""
@router.get('/enterprises/{enterprise_id}', response_model=company_schema.EnterprisesResponse)
def enterprise_detail(enterprise_id: int, db: Session = Depends(get_db)):
    # Lấy thông tin một daonh nghiệp theo ID
    db_enterprise = crud_company.get_enterprise(db, company_id=company_id)
    if db_enterprise is None:
        raise HTTPException(status_code=404, detail='Company not found')

    return db_enterprise
"""
