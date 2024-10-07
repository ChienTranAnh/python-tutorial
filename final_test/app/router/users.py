from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db
from ..crud import user as crud_user
from ..schemas import user as user_schemas

router = APIRouter()

@router.get('/users/', response_model=list[user_schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    # Lấy danh sách người dùng
    users = crud_user.get_users(db, skip=skip, limit=limit)
    return users

@router.post('/users/', response_model=user_schemas.UserResponse)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    # Tạo người dùng mới trong database
    db_user = crud_user.check_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='User already exists')

    return crud_user.create_user(db=db, user=user)

@router.get('/users/{user_id}', response_model=user_schemas.UserResponse)
def user_detail(user_id: int, db: Session = Depends(get_db)):
    # Lấy thông tin một người dùng theo ID
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return db_user
