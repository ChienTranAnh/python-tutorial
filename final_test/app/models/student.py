from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship, declarative_base
from ..db.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(200), comment="tên sinh viên")
    last_name = Column(String(200), nullable=True, comment="họ đệm sinh viên")
    birth = Column(Date, comment="ngày tháng năm sinh")
    sex = Column(TINYINT(1), comment='giới tính')
    email = Column(String(255), unique=True, comment="thư điện tử")
    phone = Column(String(10), comment='điện thoại liên hệ')
    classes = Column(String(150), nullable=True, comment='lớp')
    major = Column(String(150), nullable=True, comment='nghành học')
    university_id = Column(Integer, ForeignKey('universities.id'), comment="mã trường đại học")
    skill = Column(String(255), nullable=True, comment="kỹ năng")

    university = relationship("University", back_populates="students")
    ungtuyen = relationship("Ungtuyen", back_populates="students")
