from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from ..db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(200), comment="họ tên người dùng")
    birth = Column(Date, comment="ngày tháng năm sinh")
    user_name = Column(String(100), comment="tên đăng nhập")
    password = Column(String(100), comment="mật khẩu đăng nhập")
    email = Column(String(255), unique=True, comment="thư điện tử")
    role = Column(Integer, nullable=True, comment="quyền tài khoản")
    acc_type = Column(Integer, nullable=True, comment="loại tài khoản")
