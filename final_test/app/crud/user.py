from pydantic import EmailStr
from sqlalchemy.orm import Session

from . import format_date, crypt_pass
from ..models import User
from ..schemas import user as schemas

crypt_pass = crypt_pass()

# danh sách người dùng
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# tạo mới người dùng
def	create_user(db: Session, user: schemas.UserCreate):
    db_user = User(
        name=user.name,
        birth=format_date(user.birth),
        user_name=user.user_name,
        password=crypt_pass.hash(user.password),
        email=user.email,
        role=user.role,
        acc_type=user.acc_type
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

# chi tiết người dùng
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# kiểm tra tồn tại người dùng
def check_user(db: Session, email: EmailStr):
    return db.query(User).filter(User.email == email).first()
