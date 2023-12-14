from schemas import BaseEntity, Gender
from database import Base
from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship

class Author(Base, BaseEntity):
   __tablename__ = "authors"
   
   full_name = Column(String(16))
   gender = Column(Enum(Gender), nullable = False, default = Gender.NONE)
   
   books = relationship("Book", back_populates="author")
