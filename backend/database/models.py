from sqlalchemy import Column, Integer, String

from .database import Base


class Path(Base):
    __tablename__ = "path"
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String(length=255), unique=True)
