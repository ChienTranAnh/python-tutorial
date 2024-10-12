from sqlalchemy import Column, Integer, Date, ForeignKey, Text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from ..db.database import Base

class Connective(Base):
    __tablename__ = "connectives"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    enterprise_id = Column(Integer, ForeignKey('enterprises.id'), nullable=False, comment='mã doanh nghiệp')
    university_id = Column(Integer, ForeignKey('universities.id'), nullable=False, comment='mã trường đại học')
    date_apply = Column(Date, comment='ngày ứng tuyển')
    status = Column(TINYINT, comment='trạng thái 0: chưa kết nối, 1: kết nối, 2: từ chối')
    description = Column(Text, nullable=True, comment='mô tả')

    enterprise = relationship("Enterprise", back_populates="connective")
    university = relationship("University", back_populates="connective")
