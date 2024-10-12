from sqlalchemy import Column, Integer, String, Date, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base

class Recruitment(Base):
    __tablename__ = "recruitments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    job_title = Column(String(200), comment="tiêu đề tin tuyển dụng")
    job_description = Column(Text, nullable=True, comment="Nội dung")
    skill_required = Column(Text, comment="yêu cầu ứng viên")
    job_position = Column(String(100), comment="vị trí tuyển dụng")
    location = Column(String(100), nullable=True, comment="nơi làm việc")
    salary_range = Column(String(50), nullable=True, comment='mức lương')
    job_type = Column(String(50), nullable=True, comment='loại hình công việc')
    enterprise_id = Column(Integer, ForeignKey('enterprises.id'), nullable=False, comment="mã công ty")
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False, comment="mã nhân viên đăng tin")
    start_date = Column(Date, comment='ngày đăng tuyển')
    end_date = Column(Date, nullable=True, comment='ngày hết hạn')

    ung_tuyen = relationship("Ungtuyen", back_populates="recruitment")
    enterprise = relationship("Enterprise", back_populates="recruitment")
    employee = relationship("Employee", back_populates="recruitment")
