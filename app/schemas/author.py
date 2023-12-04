import sys
from pathlib import Path
sys.path.append(".")
sys.path.append("..")

import uuid
from base_entity import BaseEntity, Gender
from database import Base
from sqlalchemy import Column, String, Uuid, Enum


class Author(Base, BaseEntity()):
   __tablename__ = "authors"
   
   id = Column(Uuid, primary_key = True, default = uuid.uuid4)
   full_name = Column(String(16))
   gender = Column(Enum(Gender), nullable = False, default = Gender.NONE)