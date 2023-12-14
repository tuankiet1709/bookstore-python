from schemas.base_entity import BaseEntity
from database import Base
from sqlalchemy import Column, String, Boolean
from passlib.context import CryptContext
from sqlalchemy.orm import relationship

bcrypt_context = CryptContext(schemes=["bcrypt"])

class User(Base, BaseEntity):
    __tablename__ = 'users'
    
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    
    books = relationship("Book", back_populates="owner")
    
def get_password_hash(password: str) -> str:
    return bcrypt_context.hash(password)
    
def verify_password(plain_password, hased_password) -> bool:
    return bcrypt_context.verify(plain_password, hased_password)