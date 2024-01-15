from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Path(Base):
    __tablename__ = "path"
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String(length=255), unique=True)







# ---------------------------------------TEST DATA-----------------------------------------------------------#
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(225), unique=True, index=True)
    hashed_password = Column(String(225))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String(225), index=True)
    description = Column(String(225), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
