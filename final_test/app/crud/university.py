from pydantic import EmailStr
from sqlalchemy.orm import Session

from . import crypt_pass
from ..models import University
from ..schemas import university as schemas

crypt_pass = crypt_pass()

def get_universities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(University).offset(skip).limit(limit).all()

def	create_university(db: Session, university: schemas.UniversityCreate):
    db_university = University(
        uni_name=university.uni_name,
        address=university.address,
        email=university.email,
        password=crypt_pass.hash(university.password),
        phone=university.phone,
        website=university.website,
        major=f"{university.major}"
    )
    db.add(db_university)
    db.commit()
    db.refresh(db_university)

    return db_university

def get_university(db: Session, university_id: int):
    return db.query(University).filter(University.id == university_id).first()

def check_university(db: Session, email: EmailStr):
    return db.query(University).filter(University.email == email).first()

# tìm kiếm sinh viên
def search_universities(db: Session, location: str, major: str):
    db_universities = db.query(University)
    if location:
        db_universities = db_universities.filter(University.address.like(f"%{location}%"))
    if major:
        db_universities = db_universities.filter(University.major.like(f"%{major}%"))

    return db_universities.all()
