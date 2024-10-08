from sqlalchemy import Column, Integer, String, Date, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base

class Recruitment(Base):
    __tablename__ = "recruitments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), comment="tiêu đề tin tuyển dụng")
    content = Column(Text, nullable=True, comment="Nội dung")
    candidate = Column(Date, comment="yêu cầu ứng viên")
    job_position = Column(String(100), comment="vị trí tuyển dụng")
    salary = Column(Float, nullable=True, comment='mức lương')
    company_id = Column(Integer, ForeignKey('enterprises.id'), comment="mã công ty")
    start_date = Column(Date, comment='ngày đăng tuyển')
    end_date = Column(Date, nullable=True, comment='ngày hết hạn')

    ung_tuyen = relationship("Ungtuyen", back_populates="recruitment")
    enterprise = relationship("Enterprise", back_populates="recruitment")
