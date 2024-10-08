from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import get_db
from ..crud import job as crud_job
from ..crud.enterprises import get_enterprise
from ..crud.job import update_job
from ..schemas import job as job_schemas

router = APIRouter()

@router.get('/enterprises/{enterprise_id}/jobs', response_model=list[job_schemas.JobResponse])
def read_recruitments(enterprise_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_company = get_enterprise(db, enterprise_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail='Company does not exist')

    return crud_job.get_jobs(db=db, company_id=enterprise_id, skip=skip, limit=limit)

@router.post('/enterprises/{enterprise_id}/jobs', response_model=job_schemas.JobResponse)
def create_recruitment(enterprise_id: int, recruitment: job_schemas.JobCreate, db: Session = Depends(get_db)):
    db_company = get_enterprise(db, enterprise_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail='Company does not exist')

    return crud_job.create_job(db=db, job=recruitment, company_id=enterprise_id)

@router.put('/enterprises/{enterprise_id}/jobs/{job_id}', response_model=job_schemas.JobResponse)
def update_recruitment(enterprise_id: int, job_id: int, recruitment: job_schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = update_job(db=db, company_id=enterprise_id, recruitment_id=job_id, recruitment=recruitment)
    if db_job is None:
        raise HTTPException(status_code=404, detail='Job not found')

    return db_job

@router.delete('/enterprises/{enterprise_id}/jobs/{job_id}')
def delete_recruitment(enterprise_id: int, job_id: int, db: Session = Depends(get_db)):
    db_job = crud_job.delete_job(db=db, company_id=enterprise_id, recruitment_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail='Job not found')

    raise HTTPException(status_code=200, detail='Delete job success!')
