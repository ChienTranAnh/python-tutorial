from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.mysql import TINYINT
from ..db.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(200), comment="tên sinh viên")
    last_name = Column(String(200), comment="họ đệm sinh viên")
    birth = Column(Date, comment="ngày tháng năm sinh")
    sex = Column(TINYINT(1), comment='giới tính')
    email = Column(String(255), unique=True, comment="thư điện tử")
    phone = Column(String(10), comment='điện thoại liên hệ')
    classes = Column(String(150), comment='lớp')
    major = Column(String(150), comment='nghành học')
    university_id = Column(Integer, comment="mã trường đại học")
    skill = Column(String(255), comment="kỹ năng")
