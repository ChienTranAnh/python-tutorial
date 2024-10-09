from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..core.config import settings

SQLALCHEMY_DATABASE_URL = settings.database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Xóa tất cả các bảng hiện tại và tạo lại bảng mới theo các model đã định nghĩa
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
