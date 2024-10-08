from sqlalchemy.orm import Session

from . import format_date
from ..models import Recruitment
from ..schemas import job as schemas

def get_jobs(db: Session, company_id: int, skip: int = 0, limit: int = 10):
    return db.query(Recruitment).filter(Recruitment.enterprise_id == company_id).offset(skip).limit(limit).all()

def	create_job(db: Session, job: schemas.JobCreate, company_id: int):
    db_recruitment = Recruitment(
        job_title=job.job_title,
        job_description=job.job_description,
        skill_required=job.skill_required,
        job_position=job.job_position,
        location=job.location,
        salary_range=job.salary_range,
        job_type=job.job_type,
        enterprise_id=company_id,
        start_date=format_date(job.start_date),
        end_date=format_date(job.end_date)
    )
    db.add(db_recruitment)
    db.commit()
    db.refresh(db_recruitment)

    return db_recruitment

def get_job(db: Session, company_id: int, recruitment_id: int):
    return db.query(Recruitment).filter(Recruitment.enterprise_id == company_id, Recruitment.id == recruitment_id).first()

def update_job(db: Session, company_id: int, recruitment_id: int, recruitment: schemas.JobCreate):
    job = get_job(db, company_id, recruitment_id)
    if job is None:
        return

    job.job_title = recruitment.job_title,
    job.job_description = recruitment.job_description,
    job.skill_required = recruitment.skill_required,
    job.job_position = recruitment.job_position,
    job.location = recruitment.location,
    job.salary_range = recruitment.salary_range,
    job.job_type = recruitment.job_type,
    job.enterprise_id = company_id,
    job.start_date = format_date(recruitment.start_date),
    job.end_date = format_date(recruitment.end_date)
    db.commit()
    db.refresh(job)

    return recruitment

def delete_job(db: Session, company_id: int, recruitment_id: int):
    recruitment = get_job(db, company_id, recruitment_id)
    if recruitment is None:
        return

    db.delete(recruitment)
    db.commit()

    return True
