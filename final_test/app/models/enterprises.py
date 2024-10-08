from contextlib import nullcontext

from pydantic_core.core_schema import nullable_schema
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base

class Enterprise(Base):
    __tablename__ = "enterprises"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    company_name = Column(String(200), comment="tên công ty")
    address = Column(String(255), comment="địa chỉ công ty")
    phone = Column(String(10), comment='điện thoại công ty')
    email = Column(String(255), unique=True, comment='thư điện tử')
    password = Column(String(100), comment='mật khẩu đăng nhập')
    website = Column(String(200), nullable=True, comment='trang web công ty')
    industry = Column(String(150), nullable=True, comment='ngành nghề')
    scale = Column(Integer, nullable=True, comment='quy mô công ty')
    about = Column(String(255), nullable=True, comment='giới thiệu công ty')

    recruitment = relationship("Recruitment", back_populates="enterprise")
