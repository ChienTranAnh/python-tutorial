from pydantic import BaseModel

class JobCreate(BaseModel):
    job_title: str
    job_description: str
    skill_required: str
    job_position: str
    location: str
    salary_range: str
    job_type: str
    employee_id: int
    start_date: str
    end_date: str

class JobResponse(BaseModel):
    job_title: str
    job_description: str
    skill_required: str
    location: str
    salary_range: str
    job_type: str

    class Config:
        orm_mode = True
