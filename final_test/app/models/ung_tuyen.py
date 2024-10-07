from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from ..db.database import Base

class Ung_tuyen(Base):
    __tablename__ = "ung_tuyen"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    recruitment_id = Column(Integer, ForeignKey('recruitments.id'), comment="mã tin tuyển dụng")
    students_id = Column(Integer, ForeignKey('students.id'), comment="mã sinh viên")
    date_apply = Column(Date, comment="ngày ứng tuyển")
    status = Column(TINYINT, comment="trạng thái 0: nhà tuyển dụng chưa đọc, 1: nhà tuyển dụng đã đọc, 2: từ chối, 3: chấp nhận")

    recruitment = relationship("recruitments", back_populates="ung_tuyen")
    student = relationship("Student", back_populates="ung_tuyen")
