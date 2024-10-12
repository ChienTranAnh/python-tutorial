from pydantic import EmailStr
from sqlalchemy.orm import Session

from . import format_date, crypt_pass
from ..models import Employee
from ..schemas import employee as schemas

crypt_pass = crypt_pass()

def get_employees(db: Session, company_id: int, skip: int = 0, limit: int = 10):
    return db.query(Employee).filter(Employee.enterprise_id == company_id).offset(skip).limit(limit).all()

def	create_employee(db: Session, employee: schemas.StaffCreate, company_id: int) -> Employee:
    db_employee = Employee(
        name=employee.name,
        birth=format_date(employee.birth),
        sex=employee.sex,
        email=employee.email,
        password=crypt_pass.hash(employee.password),
        phone=employee.phone,
        position=employee.position,
        enterprise_id=company_id
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee

def get_employee(db: Session, company_id: int, staff_id: int):
    return db.query(Employee).filter(Employee.enterprise_id == company_id, Employee.id == staff_id).first()

def check_employee(db: Session, email: EmailStr):
    return db.query(Employee).filter(Employee.email == email).first()

def delete_employee(db: Session, company_id: int, staff_id: int):
    staff = get_employee(db, company_id, staff_id)
    if staff is None:
        return

    db.delete(staff)
    db.commit()

    return True
