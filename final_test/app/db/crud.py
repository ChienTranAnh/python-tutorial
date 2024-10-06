from datetime import datetime
from pydantic import EmailStr
from sqlalchemy.orm import Session

from .. import models
from ..schemas import user as schemas

def	create_user(db: Session, user: schemas.UserCreate):
    birth_obj = datetime.strptime(user.birth, '%d/%m/%Y')
    date_of_birth = datetime.strftime(birth_obj, '%Y-%m-%d')
    db_user = models.User(
        name=user.name,
        birth=date_of_birth,
        user_name=user.user_name,
        password=user.password,
        email=user.email,
        role=user.role,
        acc_type=user.acc_type
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def check_user(db: Session, email: EmailStr):
    return db.query(models.User).filter(models.User.email == email).first()