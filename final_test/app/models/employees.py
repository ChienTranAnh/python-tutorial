from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from ..db.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(200), comment="họ tên nhân viên")
    birth = Column(Date, comment="ngày tháng năm sinh")
    sex = Column(TINYINT(1), comment='giới tính')
    email = Column(String(255), unique=True, comment="thư điện tử")
    password = Column(String(100), nullable=False, comment="mật khẩu")
    phone = Column(String(10), comment='điện thoại liên hệ')
    position = Column(String(20), comment='chức vụ')
    enterprise_id = Column(Integer, ForeignKey('enterprises.id'), nullable=False, comment="mã doanh nghiệp")

    enterprise = relationship("Enterprise", back_populates="employee")
    recruitment = relationship("Recruitment", back_populates="employee")
