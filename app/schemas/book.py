from schemas.base_entity import BaseEntity, BookMode
from database import Base
from sqlalchemy import Column, Uuid, String, Enum, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship


class Book(Base, BaseEntity):
    __tablename__ = "books"

    title = Column(String(36), nullable=False)
    description = Column(String(255))
    mode = Column(Enum(BookMode), nullable=False, default=BookMode.DRAFT)
    rating = Column(SmallInteger, nullable=False, default=0)
    author_id = Column(Uuid, ForeignKey("authors.id"), nullable=False)
    owner_id = Column(Uuid, ForeignKey("users.id"), nullable=False)
    
    author = relationship("Author")
    owner = relationship("User")
