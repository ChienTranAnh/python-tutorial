from pydantic import EmailStr
from sqlalchemy.orm import Session

from . import format_date
from ..models import Student
from ..schemas import student as schemas

def get_students(db: Session, university_id: int, skip: int = 0, limit: int = 10):
    return db.query(Student).filter(Student.university_id == university_id).offset(skip).limit(limit).all()

def	create_student(db: Session, student: schemas.StudentCreate, university_id: int):
    db_student = Student(
        first_name=student.first_name,
        last_name=student.last_name,
        birth=format_date(student.birth),
        sex=student.sex,
        email=student.email,
        phone=student.phone,
        classes=student.classes,
        major=student.major,
        graduation_year=student.graduation_year,
        university_id=university_id,
        skill=student.skill
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student

# def get_employee(db: Session, company_id: int, staff_id: int):
#     return db.query(Student).filter(Student.enterprise_id == company_id, Student.id == staff_id).first()

def check_student(db: Session, email: EmailStr):
    return db.query(Student).filter(Student.email == email).first()

# def delete_employee(db: Session, company_id: int, staff_id: int):
#     staff = get_employee(db, company_id, staff_id)
#     if staff is None:
#         return

#     db.delete(staff)
#     db.commit()

#     return True

# tìm kiếm sinh viên
def search_students(db: Session, skill: str, major: str, graduation_year: int):
    db_students = db.query(Student)
    if skill:
        db_students = db_students.filter(Student.skill.like(f"%{skill}%"))
    if major:
        db_students = db_students.filter(Student.major.like(f"%{major}%"))
    if graduation_year:
        db_students = db_students.filter(Student.graduation_year == graduation_year)

    return db_students.all()
