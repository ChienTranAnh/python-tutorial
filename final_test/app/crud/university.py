from pydantic import EmailStr
from sqlalchemy.orm import Session

from ..models import University
from ..schemas import university as schemas

def get_universities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(University).offset(skip).limit(limit).all()

def	create_university(db: Session, university: schemas.UniversityCreate):
    db_university = University(
        uni_name=university.uni_name,
        address=university.address,
        email=university.email,
        phone=university.phone,
        website=university.website
    )
    db.add(db_university)
    db.commit()
    db.refresh(db_university)

    return db_university

def get_university(db: Session, university_id: int):
    return db.query(University).filter(University.id == university_id).first()

def check_university(db: Session, email: EmailStr):
    return db.query(University).filter(University.email == email).first()

# def delete_employee(db: Session, company_id: int, staff_id: int):
#     staff = get_employee(db, company_id, staff_id)
#     if staff is None:
#         return

#     db.delete(staff)
#     db.commit()

#     return True

# tìm kiếm sinh viên
def search_universities(db: Session, location: str, major: str):
    db_universities = db.query(University)
    if location:
        db_universities = db_universities.filter(University.address.like(f"%{location}%"))
    if major:
        db_universities = db_universities.filter(University.major.like(f"%{major}%"))

    return db_universities.all()
