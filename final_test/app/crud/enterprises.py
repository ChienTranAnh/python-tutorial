from pydantic import EmailStr
from sqlalchemy.orm import Session

from . import crypt_pass
from ..models import Enterprise
from ..schemas import enterprises as schemas

crypt_pass = crypt_pass()

# đăng nhập
def authenticate_enterprise(db: Session, email: EmailStr, password: str):
    company = db.query(Enterprise).filter(Enterprise.email == email).first()
    if not company:
        return
    if not crypt_pass.verify(password, company.password):
        return False

    return company

# đăng ký doanh nghiệp mới
def	create_enterprise(db: Session, company: schemas.EnterprisesCreate):
    pass_save = crypt_pass.hash(company.password)
    db_company = Enterprise(
        company_name = company.company_name,
        address = company.address,
        phone = company.phone,
        email = company.email,
        password = pass_save,
        website = company.website,
        industry = company.industry,
        scale = company.scale,
        about = company.about
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)

    return db_company

# chi tiết doanh nghiệp
def get_enterprise(db: Session, company_id: int):
    return db.query(Enterprise).filter(Enterprise.id == company_id).first()

# cập nhật thông tin doanh nghiệp
def update_enterprise(db: Session, company_detail: schemas.EnterpriesUpdate, company: schemas.EnterpriesUpdate):
    company_detail.company_name = company.company_name,
    company_detail.phone = company.phone,
    company_detail.email = company.email,
    company_detail.address = company.address

    db.commit()
    db.refresh(company_detail)

    return company_detail

# đổi mật khẩu
def change_pass(db: Session, old_pass, new_pass, company_detail):
    if not crypt_pass.verify(old_pass, company_detail.password):
        return False

    new_pass = crypt_pass.hash(new_pass)
    company_detail.password = new_pass
    db.commit()
    db.refresh(company_detail)

    return True

# kiểm tra tồn tại doanh nghiệp
def check_enterprise(db: Session, company_email: EmailStr):
    return db.query(Enterprise).filter(Enterprise.email == company_email).first()

"""
# danh sách doanh nghiệp
def get_enterprises(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Enterprise).offset(skip).limit(limit).all()
"""
