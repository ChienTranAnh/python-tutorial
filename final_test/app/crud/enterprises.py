from datetime import datetime
from pydantic import EmailStr
from sqlalchemy.orm import Session

from ..models import Enterprise
from ..schemas import enterprises as schemas

# danh sách doanh nghiệp
def get_enterprises(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Enterprise).offset(skip).limit(limit).all()

# đăng ký doanh nghiệp mới
def	create_enterprise(db: Session, company: schemas.EnterprisesCreate):
    db_company = Enterprise(
        company_name = company.company_name,
        address = company.address,
        phone = company.phone,
        email = company.email,
        password = company.password,
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
def get_enterprise(db: Session, enterprise_id: int):
    return db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()

# kiểm tra tồn tại doanh nghiệp
def check_enterprise(db: Session, email: EmailStr):
    return db.query(Enterprise).filter(Enterprise.email == email).first()
