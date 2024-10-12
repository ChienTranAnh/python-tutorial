from sqlalchemy.orm import Session

from . import format_date
from ..models import Connective
from ..schemas import connective as schemas

def get_connectives(db: Session, company_id: int, skip: int = 0, limit: int = 10):
    return db.query(Connective).filter(Connective.enterprise_id == company_id).offset(skip).limit(limit).all()

def	create_connective(db: Session, connective: schemas.ConnectiveCreate, company_id: int, university_id: int):
    db_connective = Connective(
        enterprise_id=company_id,
        university_id=university_id,
        status=0,
        description=connective.description,
        date_apply=format_date(connective.date_apply)
    )
    db.add(db_connective)
    db.commit()
    db.refresh(db_connective)

    return db_connective

def get_connective(db: Session, company_id: int, university_id: int):
    return db.query(Connective).filter(Connective.enterprise_id == company_id, Connective.university_id == university_id).first()

def delete_connective(db: Session, company_id: int, university_id: int):
    db_connective = get_connective(db=db, company_id=company_id, university_id=university_id)
    if db_connective is None:
        return

    db.delete(db_connective)
    db.commit()

    return True

# def update_job(db: Session, company_id: int, recruitment_id: int, recruitment: schemas.JobCreate):
#     job = get_job(db, company_id, recruitment_id)
#     if job is None:
#         return
#
#     job.job_title = recruitment.job_title,
#     job.job_description = recruitment.job_description,
#     job.skill_required = recruitment.skill_required,
#     job.job_position = recruitment.job_position,
#     job.location = recruitment.location,
#     job.salary_range = recruitment.salary_range,
#     job.job_type = recruitment.job_type,
#     job.enterprise_id = company_id,
#     job.start_date = format_date(recruitment.start_date),
#     job.end_date = format_date(recruitment.end_date)
#     db.commit()
#     db.refresh(job)
#
#     return recruitment
