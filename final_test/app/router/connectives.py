from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import get_db
from ..crud.enterprises import get_enterprise
from ..crud import connective as crud_connective
from ..schemas import connective as connective_schema
from ..crud.university import get_university

router = APIRouter()

# danh sách trường đại học đã kết nối
@router.get('/enterprises/{enterprise_id}/universities', response_model=list[connective_schema.ConnectiveResponse])
def read_universities(enterprise_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_company = get_enterprise(db, enterprise_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail='Company does not exist')

    return crud_connective.get_connectives(db, company_id=enterprise_id, skip=skip, limit=limit)

# doanh nghiệp gửi yêu cầu kết nối tới trường đại học
@router.post('/enterprises/{enterprise_id}/connect-universities/{university_id}', response_model=connective_schema.ConnectiveResponse)
def connect_universities(enterprise_id: int, university_id: int, connective: connective_schema.ConnectiveCreate, db: Session = Depends(get_db)):
    detail_enterprise = get_enterprise(db=db, company_id=enterprise_id)
    if detail_enterprise is None:
        raise HTTPException(status_code=404, detail='Company not found')

    detail_university = get_university(db=db, university_id=university_id)
    if detail_university is None:
        raise HTTPException(status_code=404, detail='University not found')

    check_connective = crud_connective.get_connective(db=db, company_id=enterprise_id, university_id=university_id)
    if check_connective:
        raise HTTPException(status_code=400, detail='Connection already exists')

    return crud_connective.create_connective(db=db, connective=connective, company_id=enterprise_id, university_id=university_id)

# ngắt kết nối vs trường đại học
@router.delete('/enterprises/{enterprise_id}/connect-universities/{university_id}')
def delete_connection(enterprise_id: int, university_id: int, db: Session = Depends(get_db)):
    db_connective = crud_connective.delete_connective(db=db, company_id=enterprise_id, university_id=university_id)
    if db_connective is None:
        raise HTTPException(status_code=404, detail='Connections does not exist')

    return HTTPException(status_code=200, detail='Delete connection success!')
