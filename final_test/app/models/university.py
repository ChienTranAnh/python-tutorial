from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from ..db.database import Base

class University(Base):
    __tablename__ = "universities"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    uni_name = Column(String(200), comment="tên trường")
    address = Column(String(255), comment="địa chỉ")
    phone = Column(String(10), comment='điện thoại')
    email = Column(String(255), unique=True, comment="thư điện tử")
    password = Column(String(100), comment="mật khẩu đăng nhập")
    website = Column(String(200), nullable=True, comment="trang web trường đại học")
    major = Column(Text, nullable=True, comment="các ngành học trong trường")

    student = relationship("Student", back_populates="university")
    connective = relationship("Connective", back_populates="university")
